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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0b79e21-0940-3965-a3a9-23f96c8a548d | -6.1108 | -57.7035 | 2026-08-16 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| ddaf7faf-db3b-3e49-ad6d-2aa6e1bd7d21 | -14.4109 | -51.9269 | 2026-08-16 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a06f030a-1e70-3732-9767-71136c39fda5 | -6.8385 | -56.4542 | 2026-08-16 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| cd6666ae-972e-3c80-95e9-fbfa8455c153 | -12.7017 | -48.4753 | 2026-08-16 00:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 81694cb0-7df0-3aa8-97df-1a2e9348eedf | -6.6198 | -58.9836 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5bb79153-dd6d-313c-aba3-779a1f5b2b21 | -6.7122 | -58.9606 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 7944a11e-b730-35a4-82bc-eecc99e5aa14 | -14.1125 | -53.6717 | 2026-08-16 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| a3b44c83-bd62-3371-8d0b-0a7b7be8cbb7 | -7.4259 | -60.01 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| e6719116-891a-3ad7-b071-934dfd016010 | -6.6937 | -58.9613 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.0 |
| e4336d3b-1fc0-3d57-88f9-13500abe2704 | -6.7123 | -58.9412 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 244.3 |
| 0c39f8ed-e001-37a9-9300-770391c72005 | -6.8202 | -56.4353 | 2026-08-16 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| a77699c2-138c-3e94-a707-dcbdb04c6372 | -6.6378 | -59.0602 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 379.8 |
| f13ebb6e-3086-37f8-9d82-cfd37463a4b4 | -14.1122 | -53.6926 | 2026-08-16 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 55645d2c-5c8a-377e-bfe8-83b41df773b2 | -8.9041 | -60.5577 | 2026-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| ede38da2-12be-37e3-8f43-4719e9668bd5 | -6.6377 | -59.0795 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 761.2 |
| f89bc1cf-d490-38df-9022-0d0a4018b68e | -6.8572 | -56.4335 | 2026-08-16 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| de5d7a8e-bc05-3b29-a1b0-7a4748f0b2c7 | -6.8412 | -58.9746 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| ce66320d-f81e-3c38-9ccb-40f32eb886c1 | -6.6014 | -58.9844 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 3b9a7160-a4b8-3778-96f4-9a8fc754f6e2 | -8.9039 | -60.5769 | 2026-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 798f36a6-664b-3748-aef7-5b3b1bc05b44 | -14.3915 | -51.9294 | 2026-08-16 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4dfd4919-8652-3534-bf6a-0e3f0f3c75de | -6.0923 | -57.7238 | 2026-08-16 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e32530a6-acd8-3bf2-a103-91fe226e3b26 | -6.8598 | -58.9545 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f3e1bf72-b441-37ee-83f9-db44a7fb3b1e | -6.8387 | -56.4344 | 2026-08-16 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 6705f0b9-e344-3619-b314-b87743131823 | -14.3923 | -51.8867 | 2026-08-16 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| dbad2756-dbba-3e22-beef-21b26d312ef7 | -6.6193 | -59.0802 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 492.1 |
| a13d6c06-e81e-3323-b312-daa1fe4df387 | -8.8854 | -60.5778 | 2026-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8a2ce1ae-7f09-3847-b92c-58c02569ad70 | -6.8597 | -58.9738 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 268.8 |
| 3a9f8c49-8e7d-3127-af4a-de563765bf7f | -8.9038 | -60.5962 | 2026-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 0ad24fc7-5123-36bb-88b8-adc4e27acd4e | -8.8852 | -60.5971 | 2026-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 6198fda0-1ef6-337f-87ee-f1545ddc5cb3 | -6.1107 | -57.723 | 2026-08-16 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 6b09cfa5-392d-38d2-a88f-9e8f9a7ba091 | -13.8034 | -53.7911 | 2026-08-16 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| b8ea2d2d-9dc3-3128-874b-a9dc7e0077a5 | -13.7845 | -53.7725 | 2026-08-16 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 781f1d60-b010-356a-bdeb-b7e3d5777617 | -6.6938 | -58.942 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 258b75b6-03b2-3cc0-850b-f4b92bd206bb | -14.3919 | -51.9081 | 2026-08-16 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 5ef5082b-9f14-3745-b9e6-1a13686dfc59 | -6.3137 | -43.6178 | 2026-08-16 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| d974401f-295f-3d0c-aac4-557ff2b6b9a2 | -6.8781 | -58.973 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c93795b6-bc0a-3380-9bb0-5df82522924c | -6.82 | -56.4551 | 2026-08-16 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 169.6 |
| e7348602-cc16-3be3-a461-e1c7095e41ac | -14.4112 | -51.9055 | 2026-08-16 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 610e1dbc-cb93-39ad-a90d-2e718397e92a | -12.2873 | -45.8864 | 2026-08-16 00:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| df2e012f-32d1-33b6-b14e-501fcaa20fa3 | -6.7307 | -58.9405 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b083e74c-b52b-3acf-b3f1-d9478f86c4c5 | -6.6192 | -59.0996 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0860793f-b125-37cb-addc-854561f41302 | -8.8855 | -60.5586 | 2026-08-16 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d227b10b-ff7f-328d-b043-2e7c1a033217 | -14.1315 | -53.6903 | 2026-08-16 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b68a7cb0-b99a-3096-8094-617c77c86801 | -6.6376 | -59.0988 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 981f0f44-dd3d-38d5-8818-85656d8687bd | -6.6194 | -59.0609 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 280.1 |
| 425778d9-fc09-30c8-aea8-38cb5f574b87 | -6.8596 | -58.9931 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 35985ddd-63e9-30e4-b96a-0fcec202bfde | -6.7124 | -58.9219 | 2026-08-16 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0c0b4da8-648a-3a63-bb96-d3ed65343225 | -6.1107 | -57.723 | 2026-08-16 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| a0ea7608-1eb0-3219-8a56-aaee121e01aa | -6.6378 | -59.0602 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 253.1 |
| cda917a7-821a-3e8f-9da9-9b104cbb3e1c | -13.8034 | -53.7911 | 2026-08-16 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 694926da-4983-3d82-b658-0208fe5aae4d | -6.8412 | -58.9746 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4b9643cf-0053-3bfa-bff6-845f1434ff06 | -14.0801 | -58.7632 | 2026-08-16 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 2b56f190-b254-337c-b25c-80e38dd9122d | -6.6938 | -58.942 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 0cdec580-b0da-3459-b38e-447b66cd596b | -6.0924 | -57.7043 | 2026-08-16 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 40958c38-04c5-3bd7-87ce-2a650f1c3531 | -6.8572 | -56.4335 | 2026-08-16 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d62b6f6a-b6de-3332-a177-7c6b9f5ff5ee | -6.82 | -56.4551 | 2026-08-16 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| f72dc8c3-492a-3665-8a29-75973d4fc030 | -7.5485 | -61.1722 | 2026-08-16 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 52c67602-e35a-32e0-b896-67c5a69b6e3c | -6.6193 | -59.0802 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 556.8 |
| 41f3ab94-f39b-35da-85f4-f6816b647d9b | -14.3919 | -51.9081 | 2026-08-16 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d825a2f8-c969-38c4-b18a-c149f82074bf | -6.8598 | -58.9545 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 05aca623-7fab-384e-8881-fefd9067d9e8 | -14.0612 | -58.7449 | 2026-08-16 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 30a36731-72f7-3fb9-b4dc-0e935e97238c | -14.4109 | -51.9269 | 2026-08-16 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 75833286-5974-3fe4-8214-5617f79ed6ce | -6.6198 | -58.9836 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| fb050c94-65d5-3021-b24f-9493d50d250c | -14.3923 | -51.8867 | 2026-08-16 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1ae05dff-c881-3b93-8547-7fbb11d822c0 | -6.8387 | -56.4344 | 2026-08-16 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| f6e5d8e1-a990-3c7c-b13e-092fb3b26474 | -6.7307 | -58.9405 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 21b07b46-828f-30d2-b96d-0821ecd9456e | -6.8597 | -58.9738 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 243.6 |
| 0c265af0-375d-32f5-b89f-97e3042a5ac4 | -14.0803 | -58.7433 | 2026-08-16 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e0a0b107-3e1c-34d7-bb21-3ebc4fc5d8d5 | -6.8202 | -56.4353 | 2026-08-16 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 7c0c998e-3691-3d4a-9670-ac8f7e7350e6 | -8.9041 | -60.5577 | 2026-08-16 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 9f00ee26-e699-3d73-a309-d5a5b93d9bf5 | -6.8596 | -58.9931 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c653268f-6a55-3fdc-9223-11aa8fe0485f | -6.8385 | -56.4542 | 2026-08-16 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| ed1d2c7d-cda2-300c-9bd2-15f8818ef880 | -6.6192 | -59.0996 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| cb63fdd0-8607-3d2c-9794-871a375ec877 | -6.6937 | -58.9613 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| acec6d66-8a6c-3754-8a16-a63a2845975f | -6.1108 | -57.7035 | 2026-08-16 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 8848f797-94a7-365e-bb5a-31df1fa9fdb2 | -8.9039 | -60.5769 | 2026-08-16 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 47e8ff21-cf55-335d-b444-c671698e0341 | -14.0609 | -58.7649 | 2026-08-16 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 1e1237a5-0ba8-3bab-9579-3df86a57cffc | -6.7122 | -58.9606 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 82545ba1-81dc-3b0b-b279-f434678f971b | -6.7124 | -58.9219 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b4614645-b10a-38cd-9f9d-9bd0e4f3553d | -12.7017 | -48.4753 | 2026-08-16 00:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| c7bb2414-b3f9-39ef-bba8-36eb096ff8b2 | -6.0923 | -57.7238 | 2026-08-16 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| d76d34cd-7356-360f-9116-b24b1d171640 | -6.6014 | -58.9844 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ee653682-4e4c-336f-aed5-fde19e43d6c4 | -14.4919 | -54.0225 | 2026-08-16 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f112c453-0d38-3334-9869-b8431e9deee5 | -6.7123 | -58.9412 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 217.3 |
| bfa9b758-d257-3c74-8df6-05d7e9fae67c | -8.9038 | -60.5962 | 2026-08-16 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 5c7a827e-fa64-3140-bfcf-2f0ed4726a04 | -12.6825 | -48.4779 | 2026-08-16 00:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 7ef08d37-f88f-35a4-b1b7-b3c23f395e3b | -6.6377 | -59.0795 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 444.9 |
| 5be12348-ce42-32f4-81a5-bb57657cc0fc | -6.6194 | -59.0609 | 2026-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 315.6 |
| 1ab5691b-4ed2-39ff-a006-bd52339b37a7 | -7.5871 | -60.8845 | 2026-08-16 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| bdeef9e0-c059-3613-8c1b-c6222c7e8533 | -8.98 | -60.54 | 2026-08-16 00:15:00 | MSG-03 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01168f85-456c-3dae-b64b-8f848bb1427e | -6.6378 | -59.0602 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 301.9 |
| 85b4c978-b8ee-3da6-b946-acfb6ebe12fe | -6.7124 | -58.9219 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 3fa171a6-2e58-301c-8367-38c19e1acd75 | -6.8385 | -56.4542 | 2026-08-16 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 28bde734-0b8d-3984-9d3c-a54f179f2a0b | -8.9039 | -60.5769 | 2026-08-16 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 89b50728-8f0a-3e10-8a11-2726b1fe0289 | -6.8387 | -56.4344 | 2026-08-16 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 8677f3ae-0da2-373b-bc57-8dbb21abd335 | -8.9038 | -60.5962 | 2026-08-16 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 38bafa6b-749e-329a-83d1-b740ab3cb28f | -6.82 | -56.4551 | 2026-08-16 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| c4214c19-7a3b-3029-9664-cd49769136a9 | -6.8412 | -58.9746 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 04662b37-68a2-3724-b37d-301b8fe0fd19 | -6.8598 | -58.9545 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| fbe01808-df01-3045-88f5-036abe2669c6 | -14.0803 | -58.7433 | 2026-08-16 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |


[Clique aqui para ver as próximas entradas](README2.md)
