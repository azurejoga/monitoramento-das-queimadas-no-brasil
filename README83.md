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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 880a5379-38df-31de-bfdd-7ceceadf5274 | -8.33536 | -47.53738 | 2026-09-22 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f01ccc9-bc1b-3814-aec4-9b0d06e4020d | -14.17916 | -47.88038 | 2026-09-22 05:23:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9508e0b5-c88b-38f0-9a60-22f87600f98a | -6.16477 | -57.72401 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a013aef-783d-3996-91ee-3050c3c69c0a | -3.23531 | -53.95084 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7e6266da-6a80-38cf-9544-f242ca40fd17 | -10.20916 | -68.75149 | 2026-09-22 05:23:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2982f595-25cb-301f-9c88-5eb4f8516438 | -6.25632 | -57.78485 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce098705-2c2d-3209-8319-173d003d7d22 | -3.46574 | -59.55045 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a3243f9-fb25-37b0-b4e7-b9991add858b | -4.29901 | -56.26624 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 827ad211-b31b-37aa-8592-9d56108df219 | -6.68511 | -58.45499 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c709b842-fddf-3dbf-8d52-9f2a926598a4 | -6.67954 | -50.95024 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5536cf1a-d2df-3e2f-9c4a-78ca11469643 | -9.56311 | -66.03488 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2691e8f1-916f-35c8-b233-7ded4b135924 | -6.52359 | -55.38395 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5594ef5d-6dad-3517-bf11-b94c94673b28 | -10.15108 | -58.76038 | 2026-09-22 05:23:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc0bd278-4f91-3d45-a4cc-89defd2a3710 | -6.28448 | -59.91935 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 239967bb-8079-3753-9fc6-4d1d10342fe4 | -8.79288 | -69.02254 | 2026-09-22 05:23:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38bc2ae6-00f9-3534-8462-0cb263a3f94a | -5.77122 | -57.45472 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3bfe1c27-440a-3cc3-94f0-16db7a558041 | -4.68328 | -55.62376 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 54ed0617-71cb-3a1f-bb16-f7c9b53f6fc7 | -6.13905 | -55.66444 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e4e0f5a-e0b6-3a49-adcc-0eb6bae8ca20 | -7.5737 | -57.69175 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98504ef0-ecfc-3dfa-8d6a-5585d2a8a43e | -9.13689 | -67.94892 | 2026-09-22 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2df02546-e15f-338e-9386-164a4befa483 | -3.06874 | -61.28677 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b5dffa6-e637-32f5-82b9-b0b6744a9692 | -13.86783 | -48.58236 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 251998eb-9a5e-36c0-9ba2-31b98ec11297 | -11.70353 | -50.98876 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 2fb138ff-d12b-354f-b6f5-369965ff4dcd | -3.77468 | -51.35186 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02184bd0-472e-3c4f-8181-42f89edbf1f4 | -5.75115 | -51.93115 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50e76017-334f-361d-8a7f-0d38e94011ba | -6.81023 | -55.83358 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c1b268d-960b-3962-8c33-ee44eaa19b7d | -5.9829 | -57.69884 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d7b33d1-7344-3dfa-a3e4-faeb3d4aa7be | -6.92328 | -59.6263 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69f6ea5b-1e2c-3842-b0c3-180e4de2f3bb | -7.23498 | -55.59476 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b07cac-4759-317d-8a38-06fc35f354fd | -4.06128 | -56.31431 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb5ead92-3d9c-3181-885b-19335cb564e1 | -3.1741 | -58.59724 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 542049b0-16d4-300f-8532-fca480dd1e40 | -6.29685 | -57.7449 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4780d371-2d1d-340d-92bb-3034bc4093c5 | -11.99356 | -52.46423 | 2026-09-22 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f2cfda6-a892-3793-8cac-93c5ff25d260 | -4.38195 | -55.02948 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d824ce1e-9e7b-3559-934a-bbb3543ebfeb | -5.75718 | -45.08303 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 51dc50c5-8b91-3ddf-8854-66d339fdd575 | -2.41078 | -58.28115 | 2026-09-22 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c79304b-4fdc-33c0-96ab-27e6a1cdc6de | -7.33006 | -55.60889 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79fe24e2-bf9f-379e-a740-72175638642e | -6.08222 | -57.62538 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a913c1a4-8e6e-399e-b7a1-4fc35b3b6878 | -5.76288 | -45.08971 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00c66bb7-6f88-3b47-84cb-ada4c49240c3 | -2.67142 | -54.96539 | 2026-09-22 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 600deef9-9b57-3c1e-b5dd-645c8871afb3 | -7.87986 | -54.72742 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e59a0c99-cbac-3b1a-9ddc-761770fe2125 | -6.35458 | -57.76835 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f990ce6d-a866-3887-ac4f-dd766c0a37c9 | -2.78308 | -51.35546 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc9f8919-9b10-337a-982b-44130f912188 | -6.73608 | -55.07245 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b9cedc1-ec3a-3ae7-83f5-e27057fd11ad | -6.20028 | -57.77966 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c99c83c-a0cd-3114-b9c8-33b2d77a1063 | -3.07332 | -54.3878 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 721e9961-72da-3314-95ae-2f0b47710383 | -6.33304 | -59.95035 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d10412e6-8cd2-3190-921e-2a14fb1fbb64 | -6.09111 | -57.69807 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f5671695-2ae2-312b-83d6-7425acf155cf | -12.92902 | -50.92813 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 18f7efa4-35e5-3d70-997a-010736eed5ec | -3.45502 | -50.60588 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7641e517-cdb6-348d-a946-6cfe17949dc1 | -3.4599 | -58.40315 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbc121c4-d4c3-3d94-b523-7d35f5023363 | -6.34011 | -59.95146 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd492fdc-7f79-348e-ae03-c3f406282ca1 | -3.36424 | -50.46566 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 778723c5-8892-3e17-a54e-9d40ac62e7d1 | -13.33373 | -51.28595 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72ebedc0-b948-315f-a9e0-58e08930afcd | -6.14106 | -59.9332 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c442613-177c-3781-b7a2-48abc3ca1e24 | -7.58922 | -57.67995 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5c7e9f61-1abd-3f60-9faf-5d66ae8198b6 | -6.51833 | -55.38002 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bbb6923-8fa2-349e-9a37-0b8f1ce6bb10 | -2.90044 | -60.05176 | 2026-09-22 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a0bd887-8cbf-3ccd-840a-c50ca60ee5a8 | -4.55902 | -54.91889 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fcd05bdc-133d-3f26-9bb1-7174ce9f5a67 | -6.46017 | -59.99105 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dc0a62d2-df23-31a8-9d09-8f34749fb941 | -3.7202 | -57.27216 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b036981-38cc-31e9-865e-fac1b128853e | -5.85337 | -53.53363 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab47e95d-0289-326f-947f-199f07098ce0 | -9.55821 | -66.03398 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6449d238-9d2e-35c8-81a3-51b2b892645d | -3.602 | -59.44374 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9a7f4a6-ec1e-3687-bc64-92175251b732 | -8.78814 | -44.27341 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ea57ddf6-5c79-3368-8558-84192d87608d | -9.18424 | -65.85582 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 00740791-247d-3ab4-8bef-57d9573cf53c | -5.8393 | -52.11974 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15f711b8-5180-3e53-a566-ee1eb442c371 | -6.79566 | -59.13862 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6a73bbb-31f0-3073-aeb9-789d4a356f52 | -3.68844 | -42.95462 | 2026-09-22 05:23:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cb5f20d6-4d57-338a-a5ec-7cd906485f15 | -3.48374 | -58.9227 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d969fd1-29ca-3371-88d9-87c86bdebf1e | -3.69314 | -60.56831 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d42c9be-c950-3adb-af3f-c9cc02c54415 | -12.88346 | -50.9332 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 016fe6e0-33cd-3cdd-8bd1-1d8dc26375fd | -3.0581 | -54.41668 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93c1659c-e44e-300a-9b17-431f2eed8470 | -6.81079 | -55.82992 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d70e63a0-5d6a-3c32-91a6-5dbe2a43c17d | -10.45673 | -61.31194 | 2026-09-22 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4294555-4cc9-3aa2-a7d0-61834da46ebd | -6.13621 | -59.94057 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 770c2445-4666-34f5-835c-16c57408014f | -14.66756 | -45.66984 | 2026-09-22 05:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 69328775-7403-3cc7-9516-f1f9e4ce5c18 | -3.68864 | -60.5722 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 05903d27-7350-3cba-b018-d6156b7b31c6 | -9.36745 | -68.65884 | 2026-09-22 05:23:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c948d207-3873-306f-87b2-865f0490be31 | -7.57259 | -57.6773 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4395012a-c560-37da-8eef-541c480595b0 | -5.99687 | -55.67997 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac1eedb7-d72c-3d6b-9eb8-1fe6f20e748e | -13.33925 | -51.2813 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0815b2e3-e144-357e-9310-7bc112416e7f | -3.5205 | -58.76184 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b99bf507-ae73-381d-8db1-4b056aef3234 | -5.98401 | -57.7133 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03c77bd3-5a72-315d-810f-a789a9c3293f | -6.69641 | -56.16143 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a3775bf6-7045-37e9-b279-c92476d5dc22 | -3.194 | -60.43321 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 559489f2-a4f3-3a3c-b73f-ab08ba279901 | -5.89444 | -53.64006 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6090059-8937-32fc-a4ca-6cab8088b377 | -7.33639 | -55.6136 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5db888f4-904e-314f-9745-cbfe46d81ffc | -4.56476 | -54.92747 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 460aa7d9-e8b1-3518-ba88-c080b064b65f | -6.34866 | -57.88598 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 889c9eed-3648-3995-aea0-5895d7a7ceb3 | -4.33615 | -55.03001 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85ec067a-1208-347d-9755-7586642f2c4b | -3.92886 | -56.05433 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f52fa6a-4806-3607-9744-cf87386fba0f | -6.29629 | -57.74838 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a928ae62-9f0e-33ab-83ee-d4bd3c9cc903 | 0.30407 | -60.4447 | 2026-09-22 05:23:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af105408-4967-3b1a-90fe-16da13e64d54 | -6.33696 | -55.28337 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4aa2e6f4-41f5-3048-bc6a-58783f4597d2 | -3.34196 | -59.85937 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d4566c1-17f3-34a9-91ee-028df9603baf | -6.58135 | -44.14592 | 2026-09-22 05:23:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8040f136-4f2f-35eb-88ed-93dd99568bf5 | -3.28825 | -57.85857 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c249209f-f570-38fe-90cc-7550eb94d308 | -5.87084 | -53.6452 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e98399-b280-33df-91f0-49d10f571ad0 | -6.08501 | -57.69353 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README84.md)
