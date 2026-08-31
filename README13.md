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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1830860-aa8e-3d19-9d2b-d1ca6a069e3b | -5.2363 | -55.8914 | 2026-08-31 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| a5b6948a-f7e1-3ef3-81a9-228db592734b | -5.2362 | -55.9112 | 2026-08-31 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| d4596668-386c-3698-b90f-60e2ed79979e | -5.2547 | -55.9105 | 2026-08-31 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 330.6 |
| dda1b71d-f5d5-31c7-b919-a31eda4647b8 | -6.6036 | -58.5972 | 2026-08-31 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 27981c36-8228-3db1-8fab-b03e89b4dfae | -11.3615 | -45.1955 | 2026-08-31 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| d4790319-5f30-3d6c-8590-fc8c0d9fcadb | -9.4721 | -57.0156 | 2026-08-31 00:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 2f9f3c8e-0cdf-3a49-ba80-827b9629382e | -19.154 | -57.3978 | 2026-08-31 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 40f961de-c319-3416-ae63-9cadc261cb5c | -6.9367 | -55.636 | 2026-08-31 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a74b7f5e-9b68-3889-862c-df92c91f4d3e | -18.2904 | -52.6818 | 2026-08-31 00:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ae1f678b-8dff-35a5-99a9-0d683e33aaa0 | -5.2363 | -55.8914 | 2026-08-31 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 205e376d-555b-34e5-9444-fb4a4e7f58ff | -5.2362 | -55.9112 | 2026-08-31 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 78c453e3-5495-3f9c-b6a8-17c2cb370ea2 | -7.3487 | -60.5883 | 2026-08-31 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 7c190164-a308-3eb6-9a69-6a04fe0a62df | -18.2904 | -52.6818 | 2026-08-31 01:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ea2d36ed-27dc-3ace-9cb3-371f2d2b568f | -7.3301 | -60.6081 | 2026-08-31 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 117f20e5-9bd0-356c-af17-a08ec64d6d62 | -7.3302 | -60.589 | 2026-08-31 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c99deb7d-aa7c-3e4a-86c5-7799f391ff81 | -5.2731 | -55.9098 | 2026-08-31 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 48c64f9e-edd7-3949-9121-7cf5707352bf | -5.9451 | -57.6906 | 2026-08-31 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 57bcf095-f54f-35ee-ac2f-132a30995d07 | -6.6035 | -58.6166 | 2026-08-31 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1d74726c-92a2-3146-9d38-3c4018353076 | -4.85 | -55.8266 | 2026-08-31 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| fa95e1e8-2211-3816-a693-027822ac2ea2 | -8.7442 | -46.4437 | 2026-08-31 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 3030c020-55f0-3426-a977-b7dcb58a5252 | -1.6042 | -54.415 | 2026-08-31 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 5a40b498-18e9-3f13-a8e1-054081927c77 | -5.2546 | -55.9303 | 2026-08-31 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bfce35a7-3fe4-3d1c-9a8f-0be3e29060f4 | -5.2547 | -55.9105 | 2026-08-31 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 310.0 |
| 2c0a90fd-67ce-3345-b6ce-9ff2ea5c8775 | -7.3118 | -60.5897 | 2026-08-31 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| af462ecf-5fc0-346d-814c-17d257c08f46 | -6.9367 | -55.636 | 2026-08-31 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9343664d-41ba-336f-88ca-a7fb8c546473 | -4.1515 | -60.7068 | 2026-08-31 01:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 580bfbd9-f9d5-3b9d-ba48-7080e7e2d675 | -6.6036 | -58.5972 | 2026-08-31 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 65f3013e-7382-3e8b-9525-013976b67699 | -19.154 | -57.3978 | 2026-08-31 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 3a09f89e-3d94-3dcd-9efc-d2612a407519 | -5.2548 | -55.8907 | 2026-08-31 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 167.7 |
| 796890f6-caab-3d36-856a-391633dbe088 | -8.799 | -62.4905 | 2026-08-31 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| fec3287b-a8b5-3423-8887-ef3f46ba7b77 | -5.2362 | -55.9112 | 2026-08-31 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| dd067867-dad0-3db8-9536-f237ce312345 | -7.3302 | -60.589 | 2026-08-31 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 5a05fcb6-8179-3f4d-b09f-54f3e33b0aec | -7.3118 | -60.5897 | 2026-08-31 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| cef94437-4111-32f8-a4f4-8dd4e3a3c7c8 | -6.6035 | -58.6166 | 2026-08-31 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 5de9cf42-6b6f-3a05-9a38-c1ba24939609 | -1.6042 | -54.415 | 2026-08-31 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 06ad0942-2b9e-3917-a2a8-d87e8d5365dd | -6.9367 | -55.636 | 2026-08-31 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 8d686695-9f10-34dc-9697-f5d713cc4557 | -7.3301 | -60.6081 | 2026-08-31 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 91ff617e-e2df-32e7-b262-1c935024d44e | -15.4231 | -52.7049 | 2026-08-31 01:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 0e5dadcb-2afc-335c-b89f-78b02216e731 | -8.799 | -62.4905 | 2026-08-31 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 5e5d3731-1e26-33eb-b3cf-0be86fec8f46 | -6.9176 | -55.7166 | 2026-08-31 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 6cd0985c-b6df-30b5-b730-e07cd81d136f | -14.1831 | -52.8667 | 2026-08-31 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| b0468a75-84a1-324b-b2c4-2136eb6b1efd | -6.6036 | -58.5972 | 2026-08-31 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| c3a5f26e-8934-395b-b488-e0dc687b7182 | -5.2548 | -55.8907 | 2026-08-31 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 62e6e18f-ae21-3ea5-8d7d-96bc56217ad3 | -5.2546 | -55.9303 | 2026-08-31 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 407357f8-e31e-365d-a4c5-9e730b2fd68d | -5.2547 | -55.9105 | 2026-08-31 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 306.0 |
| 2aa425d9-f707-3b58-af44-d16fe48290ef | -4.1515 | -60.7068 | 2026-08-31 01:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 0a100722-22d8-3475-ad6c-4195a8c054a3 | -14.1828 | -52.8878 | 2026-08-31 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8e923b96-ec4d-397d-9279-7e80cf9a6edb | -5.2363 | -55.8914 | 2026-08-31 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| a9d37a2a-0d6d-3e46-b055-3cb8bc613d89 | -14.241 | -52.8595 | 2026-08-31 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 46734425-21da-3d27-827f-21277a36ada6 | -18.2904 | -52.6818 | 2026-08-31 01:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 78199214-ae7d-3261-ac7b-0d2322dc09c1 | -11.37 | -45.23 | 2026-08-31 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3d439b9-c2e4-38c9-a2d7-f2b26ffb184a | -11.34 | -45.17 | 2026-08-31 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17ef9d6a-6ad5-3698-aae0-665da3dec88f | -11.37 | -45.18 | 2026-08-31 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b82d13c4-55c9-3564-b80b-3714751d08f9 | -11.34 | -45.22 | 2026-08-31 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e19ba005-e8a4-30e0-8ff6-4d28da47284c | -5.2548 | -55.8907 | 2026-08-31 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 0c78e99a-298c-3382-805b-2aa1e7dc1519 | -14.1831 | -52.8667 | 2026-08-31 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 8dfbb122-0550-3ec9-ac83-6f84b9ab40bd | -5.2363 | -55.8914 | 2026-08-31 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 1f1cc8c5-e90f-3dd9-9481-089a5400aa34 | -6.6036 | -58.5972 | 2026-08-31 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 8e68b852-f049-3c21-b3c0-bf4cf42ff738 | -7.3301 | -60.6081 | 2026-08-31 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| bf6b948e-9e2c-31e2-b931-6b83678eb2a4 | -6.9546 | -55.7147 | 2026-08-31 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| d99941bb-df11-3c60-80ec-347012f68ca9 | -6.6035 | -58.6166 | 2026-08-31 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 65282a5c-09a7-346c-bbc7-95dd226d44a3 | -5.2731 | -55.9098 | 2026-08-31 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| fd7cd88b-ddb0-3bfb-8462-bea300dd0303 | -7.3302 | -60.589 | 2026-08-31 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 2d201e3e-62d0-3d67-a845-e2ab0998b011 | -14.1828 | -52.8878 | 2026-08-31 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9edae05e-5f39-3813-8ba3-f53b11dddcb8 | -6.9367 | -55.636 | 2026-08-31 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 87404fd7-d432-30bd-9fbe-fa4efdc91d7a | -10.7407 | -54.0401 | 2026-08-31 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 1d2f4585-e816-389e-bbe0-58b3fd0400ab | -5.2362 | -55.9112 | 2026-08-31 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 75eb6da1-9003-3479-a491-3ee4dc53405b | -6.9548 | -55.6948 | 2026-08-31 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| befdc38f-01fc-3de3-87f1-01792f4629fa | -5.2547 | -55.9105 | 2026-08-31 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 294.4 |
| daa6c3cf-0098-366e-a5c9-fd8849095cef | -11.6837 | -47.6154 | 2026-08-31 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| b2e6a400-baab-36bc-8d0a-027af24a5f66 | -19.15131 | -57.39362 | 2026-08-31 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| ec2bf9df-8e69-39cc-94ea-ec65c15f3e65 | -9.15798 | -59.53968 | 2026-08-31 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| b38034d1-cf4a-3d2f-8eaa-569c7ffcb46c | -7.45713 | -60.75214 | 2026-08-31 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 0da2999d-2c67-33f1-8c37-7f373d9f28f1 | -8.60638 | -71.55659 | 2026-08-31 01:24:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 94fe81f1-3484-3ea6-a174-1374d4536640 | -8.94202 | -62.06394 | 2026-08-31 01:24:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a4ce7ce8-5c8c-38fd-9447-a945fedc27f4 | -8.60985 | -70.21534 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80e800b6-0e7f-38dc-af23-0c5654a8b988 | -8.63181 | -70.57527 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 34755e55-b382-357a-9ab3-bf94e302c907 | -8.79487 | -62.50575 | 2026-08-31 01:24:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.7 |
| c5f3d2c9-2aab-3d1f-998a-af1906c854e8 | -9.15532 | -59.54727 | 2026-08-31 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 94523730-ce7e-39fb-95c9-430e5e06d7fc | -8.93854 | -62.07019 | 2026-08-31 01:24:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 20.5 |
| d2a5a29c-ecbf-3aa1-801e-b4feb2027862 | -8.60105 | -70.21658 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0413616-be76-3f6a-bc77-5b7c44b79962 | -8.67993 | -66.53143 | 2026-08-31 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c9b5549e-2e7f-3895-8666-25a1d70c9ba4 | -7.30792 | -60.60517 | 2026-08-31 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 7767f9e8-55f3-378b-a840-d0a72e42d1a3 | -8.78464 | -71.0281 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62d36559-db36-3e88-8023-f50002c0fb53 | -9.05752 | -65.41292 | 2026-08-31 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 304afbf0-02a0-3daf-88ff-5251eae8c407 | -8.8689 | -66.77132 | 2026-08-31 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0729378d-b93c-3e60-9701-88311db6e2e5 | -7.34052 | -60.59978 | 2026-08-31 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.6 |
| c09bbaf7-34f8-3253-9f42-d394b513b099 | -9.84559 | -64.98837 | 2026-08-31 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 847a7e62-f71f-3692-bc4e-22572c8279a0 | -8.88764 | -71.24975 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc1749ff-ed41-3161-8a59-b1294a1ef804 | -10.668 | -68.11449 | 2026-08-31 01:24:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e2b70e5-6f5d-3514-bbe9-63f43df05d6b | -9.85756 | -64.97993 | 2026-08-31 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 630bbd70-829a-3340-9013-0d4b9535fe99 | -8.42491 | -70.14545 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 24c1a2b0-7add-352d-8b3a-27c2041f67f8 | -10.10091 | -68.40591 | 2026-08-31 01:24:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f44a5c52-3242-3892-9373-2db01a08146c | -9.8566 | -64.98661 | 2026-08-31 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| ec1c3092-89c1-385e-9e94-eb4526b8db55 | -8.60864 | -70.20647 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ec632688-a922-30dd-8eb6-a4938baae13a | -8.79116 | -62.48225 | 2026-08-31 01:24:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 843bea0f-81b3-35c1-b465-2fae96859649 | -8.59984 | -70.20773 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 98934ed5-6bb8-3dca-82b5-27079c010368 | -8.80112 | -62.49912 | 2026-08-31 01:24:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e5eaab4d-eef4-3c08-9e0b-23ad3df7c163 | -9.8598 | -64.9943 | 2026-08-31 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9bb4485f-f1ab-3257-b162-fe463e578392 | -8.87054 | -66.78255 | 2026-08-31 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |


[Clique aqui para ver as próximas entradas](README14.md)
