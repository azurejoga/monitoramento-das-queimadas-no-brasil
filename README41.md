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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66768bf2-4f88-390e-9844-5e012187f93e | -13.29395 | -43.67533 | 2026-09-13 04:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 279c7f56-79f7-3a1f-b293-43becc64e9a7 | -8.05801 | -54.84631 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60754827-9cde-3126-b35e-b042906ee24f | -7.86271 | -54.70076 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78090277-4abe-32c0-8dcf-44fd959e8f08 | -6.38128 | -58.28997 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6383b4bc-6a17-36b5-a354-1a4b900d9406 | -6.16439 | -57.72585 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31346a63-e110-3674-b3bf-b3c93dc57e52 | -11.71701 | -46.73717 | 2026-09-13 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7a93b40-ac61-3a50-9fa5-b59ae2baa478 | -8.05172 | -54.85526 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93e56485-516f-3412-ab84-34daeff8e2ce | -9.39873 | -50.13726 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d2dd9a3-9274-3cae-9688-ce7f9018cf73 | -6.59623 | -58.85324 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f49295d6-919f-30c3-a813-9c04b702a5a2 | -8.92072 | -45.43699 | 2026-09-13 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38afb8af-fbb2-3a16-ac39-12e723ec24e1 | -11.19238 | -42.7812 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7e8d7d06-80c5-3614-ab92-8ad94eb66867 | -8.77462 | -61.40256 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f819ae67-54a2-3119-865d-3823445340fb | -13.79036 | -48.79995 | 2026-09-13 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87d9bae5-aca1-3779-be0a-d1c68a2fb33e | -10.93788 | -47.9077 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59d142d2-5094-3449-a12f-e7305f96b485 | -10.69401 | -54.17014 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 600ca508-4e0a-3d70-8861-b925f8d7dbbc | -8.05678 | -54.85335 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 946c9e48-c3df-36d0-9920-b28d8a927b03 | -13.38845 | -48.00947 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f4200b7-b810-36e3-ba9a-b692f6634800 | -6.10114 | -55.6783 | 2026-09-13 04:51:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffca2a6b-b50e-325d-8e43-c3ff0ad9969e | -13.33077 | -51.62162 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0e29bce-7278-3069-8299-4fa599a2e68a | -13.6041 | -47.88094 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f368930-d38f-3bec-a9a5-9321bd5e6a3e | -6.66391 | -58.87971 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93c0f9fb-39f1-3c3e-b7ea-703f93749766 | -11.34921 | -48.16509 | 2026-09-13 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f24083d6-604f-3c35-8532-750d5f8efe22 | -8.74916 | -46.43484 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7505f49b-8add-37d5-93de-c3d2ed3a1ab9 | -7.96618 | -43.99044 | 2026-09-13 04:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1246048b-c443-3254-bf29-3f9fcefc77cc | -7.85855 | -54.69321 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 784b339a-89c1-3433-a963-b40ac6b12b04 | -7.87067 | -54.70236 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90e97e1b-8381-3368-a477-148879d84c0a | -9.84948 | -48.51704 | 2026-09-13 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6d01be8-818c-32c2-8e8b-76e03e3d6cf2 | -8.21274 | -47.8653 | 2026-09-13 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e13bc0a6-97e8-34f0-8309-b2653f0e3e4c | -13.46301 | -48.48835 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4edd3fd-722e-3bb0-9b00-5e59c285a89f | -20.8258 | -45.73172 | 2026-09-13 04:53:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0b84ad9c-3c4b-3331-b451-9b83193c35cf | -18.48002 | -42.81533 | 2026-09-13 04:53:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad32bc2b-61fd-3ed9-8f4c-803fa650e3ae | -15.55242 | -53.79966 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13693d0a-ba3c-39a7-b679-75cf409c6824 | -14.95594 | -47.52723 | 2026-09-13 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b00ae760-3e93-3c0d-a1ad-f0bc3dceca66 | -13.4033 | -57.03211 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e683e95-f6c5-36cc-8e65-e804425def48 | -15.56035 | -53.83745 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e175fe27-164f-34e1-9218-8a34d783741c | -13.98514 | -54.07024 | 2026-09-13 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 827c7ae0-f587-36fd-a686-b1a213fbbeaa | -16.26389 | -50.22787 | 2026-09-13 04:53:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2b6b535-2e42-3618-99e2-c1804c04ced5 | -15.54484 | -53.80233 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d7ef74f-147b-3301-b6d8-19966a8330ee | -13.40662 | -57.02822 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c6bdb7b-3187-3116-b6fc-c3469f2f81e0 | -15.55177 | -53.80355 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f32ba98-e8ac-3e93-8972-16836ed93175 | -18.49109 | -42.81351 | 2026-09-13 04:53:00 | NPP-375D | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7903578d-65ec-33d7-a57a-21608aae1ebc | -15.07312 | -48.15405 | 2026-09-13 04:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5aa3b3f4-6c4d-35f0-9228-5b49c94fcf44 | -18.48536 | -42.81618 | 2026-09-13 04:53:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b48006fa-7399-3876-954c-f339ea2aad2b | -15.55439 | -53.78799 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9b89f62-ca44-3c24-9fb8-045c20729f9f | -15.07279 | -48.15172 | 2026-09-13 04:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9f799afa-e64e-3f30-afa3-6f4514d7dbf6 | -20.04577 | -45.19655 | 2026-09-13 04:53:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c34e0455-dd4a-3a2f-8bd3-515e99e2441b | -20.84399 | -45.7347 | 2026-09-13 04:53:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12580fe8-657d-3566-8bc2-8a5c155571c0 | -19.20415 | -46.79329 | 2026-09-13 04:53:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e798b4-7f9c-3af6-96d5-81118509dac4 | -18.60504 | -48.66209 | 2026-09-13 04:53:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 591de89f-5a86-3b44-8111-2fa34fe7d09a | -14.95682 | -47.52446 | 2026-09-13 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ed8e6ea-15ca-3b2c-a732-a1ef19f81bd9 | -15.55093 | -53.78737 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6bc93e5-69d9-3dba-aa9c-bfadd314e623 | -13.39977 | -57.02728 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e9b8fbb-54d6-3bc7-9207-6936736efdea | -13.40588 | -57.03223 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84e43007-05eb-32aa-8803-fd30a0bb37c6 | -13.98799 | -54.07503 | 2026-09-13 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57057965-c21e-3d0b-8ef7-bbac00fc59f6 | -20.04112 | -45.1957 | 2026-09-13 04:53:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62625fcf-2959-38f2-93b0-ccf0a9d7904e | -19.20832 | -46.79382 | 2026-09-13 04:53:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6213e4e5-7cf1-364b-847b-2fbe8f76033a | -18.60568 | -48.65747 | 2026-09-13 04:53:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 450f5494-44e8-3def-aecb-20bb5dc5c2bd | -20.84914 | -45.73217 | 2026-09-13 04:53:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f0a7d7d-f412-33b8-8a5a-ddc9c2519fe8 | -13.40238 | -57.0274 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f94a1c6-f040-3aac-8bc9-240288d53c2f | -15.28122 | -46.5843 | 2026-09-13 04:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe8e0962-76c6-3373-a02a-5e826cfa1dac | -20.82132 | -45.73042 | 2026-09-13 04:53:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a9de186-5250-3daa-ba6a-f289a0a7d41e | -15.55785 | -53.78861 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bbf57e2-1979-317e-bbcb-97739410b48b | -15.52155 | -53.9401 | 2026-09-13 04:53:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d540abbd-aee1-34ef-8daf-11d72d157264 | -15.91315 | -42.55438 | 2026-09-13 04:53:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 823549f8-9f20-38dc-b5ab-476ae44e7334 | -20.84451 | -45.73035 | 2026-09-13 04:53:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 369c8c33-7cd2-3877-834b-4bd6abce3502 | -15.56101 | -53.83352 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0410141-6ce8-3787-8504-9332e127b2d0 | -13.98869 | -54.0709 | 2026-09-13 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d47d177-ab88-32d8-b5cd-a97b9cede75d | -20.8491 | -45.73075 | 2026-09-13 04:53:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 389e1aed-4a81-3c71-9ba2-1167a512328a | -13.40402 | -57.02808 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc3e9498-1bff-3906-90b7-307ba650f734 | -13.98444 | -54.07436 | 2026-09-13 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b773c56a-4e92-36b7-99db-b9ff6d20a269 | -13.40826 | -57.02892 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c3b2847a-8ef0-3803-a201-6724a6fdc23b | -13.40089 | -57.0354 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b563467f-8ebd-3dcd-a239-332fa198e0b2 | -16.26332 | -50.23162 | 2026-09-13 04:53:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ce4352d-2029-358e-8620-8f89c319039f | -16.26729 | -50.22842 | 2026-09-13 04:53:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b574111-9837-309d-a71e-7007c294a58d | -15.56955 | -53.78265 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5e8e045-80e3-3c5f-94b8-159f2a9349a2 | -13.40164 | -57.03139 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c0529a9-31f9-356d-a7b4-9c957dfe8504 | -18.60874 | -48.6627 | 2026-09-13 04:53:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ed3a2c32-e9f5-3547-be48-f3b9f2aba3f7 | -15.57582 | -53.78778 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c471d530-7400-3e29-ba84-f19d2df07d24 | -19.27311 | -46.4568 | 2026-09-13 04:53:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30ec9c63-3991-3d20-8c34-16a982071a32 | -18.33805 | -51.95469 | 2026-09-13 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb796cf-84ac-3b16-ac23-762bc351018b | -15.28525 | -46.58471 | 2026-09-13 04:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d4e0738-47a3-36c6-a2bc-9011e867622a | -13.39906 | -57.03128 | 2026-09-13 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d98e7a7c-8fb5-3ab2-9fd3-72f15c9c095a | -20.84965 | -45.72767 | 2026-09-13 04:53:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 648c9cd1-c212-383f-9c7a-6ca72e6d239d | -16.27264 | -51.54565 | 2026-09-13 04:53:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e361b0b-579e-3e72-b3c2-9fb5afafc652 | -19.2721 | -46.45492 | 2026-09-13 04:53:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5730b814-b48f-38be-9216-632139aacbab | -15.91381 | -42.55467 | 2026-09-13 04:53:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7c52576c-1cc1-3d34-8728-d07c3fd7ce31 | -14.95613 | -47.52924 | 2026-09-13 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87df7658-b2a7-339f-a8d8-6406d3d1d874 | -17.36677 | -42.34877 | 2026-09-13 04:53:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 021bd3d3-cfbc-370d-bc9c-908b94e5b7d6 | -15.57236 | -53.78717 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec2d1703-6f6e-3277-865e-91438275e817 | -15.5689 | -53.78656 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fa675dc-e593-3b4b-9df3-8ea58fb6e4bf | -14.95972 | -47.52773 | 2026-09-13 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8bb748bc-901b-3919-a1d1-d20a04d56773 | -15.63204 | -43.33007 | 2026-09-13 04:53:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f99b67f6-1b14-3a6c-9283-3306d1ab3896 | -15.55045 | -53.8114 | 2026-09-13 04:53:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bbe946e-4ceb-3968-ad0b-f3a95d02be8c | -16.67035 | -41.85107 | 2026-09-13 04:53:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 56c10a2b-06ba-3030-91a9-82ebb2084c48 | -16.67075 | -41.84743 | 2026-09-13 04:53:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ca5cf1bd-a1a0-3f24-8980-ad500671eb3e | -21.0973 | -49.21706 | 2026-09-13 04:55:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5d2bae2f-51f6-371f-8933-1065a0108822 | 2.66906 | -51.0432 | 2026-09-13 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d78ab1ac-4e04-34c9-81f8-702bc3ee103b | -1.02615 | -53.74163 | 2026-09-13 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4e6a192-ec81-3483-b299-920a95cc14ae | 2.51129 | -50.84901 | 2026-09-13 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de0eb933-02f1-38d2-a9b4-fa25dc5d2b37 | 0.14317 | -51.46833 | 2026-09-13 05:08:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README42.md)
