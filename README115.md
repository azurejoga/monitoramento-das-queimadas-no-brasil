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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa631805-5c43-3c12-abfb-ea4583f79ab1 | -11.0505 | -47.81743 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fbe4703-da60-3ed3-a27d-8cdf38567b38 | -11.47255 | -45.01395 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51b1876e-def5-3317-8f4a-c4681d5326eb | -9.7707 | -47.74868 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a8b1c189-feb4-337b-b943-ad112a402618 | -15.35915 | -56.97836 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29dec4e4-ec9d-3aa4-a35e-09e85781cde4 | -11.67432 | -47.4987 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42740f8f-483c-3cbe-bd2b-0ed6ed241239 | -12.66981 | -48.57336 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dc222bfe-01b7-305b-a68d-7e29b3b257fb | -12.50257 | -50.24944 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 588a2ff4-21b7-3326-b1d5-cb2974d3d307 | -11.14011 | -43.3874 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81892b68-b17b-348c-9212-a5f37960b338 | -12.86807 | -47.00522 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5127f829-cdc4-39fd-b80c-dcf96ea8994e | -11.15016 | -47.19578 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8c529ed-3a59-3ccd-96c5-312966246caa | -11.85034 | -48.04908 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0aa5bf64-5f90-3a1c-ad4a-cae4cab8136a | -13.75622 | -47.96899 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9d4ea0f1-cd4d-31d6-8e3a-769aa7be6349 | -10.41735 | -51.66623 | 2025-10-02 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e46f0b6b-21e7-3217-8de1-152eed452b89 | -12.91176 | -47.17334 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f496254-4326-3ad4-8ad9-1e72e774060f | -11.8135 | -47.68831 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f296e96-2f19-3215-b10f-c916927af41c | -11.06802 | -47.81514 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3501dbb-c58f-37e7-90a2-2c3bdeb56101 | -10.26074 | -50.31845 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e4f79b97-0f85-37ac-86eb-8aa6c41809b8 | -13.38834 | -46.94825 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 257068f9-29a9-3fa2-8df9-15523042402f | -13.53116 | -47.25546 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00966c54-4abc-3bfd-8fe3-e3d32e79ba06 | -11.19434 | -47.7746 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bbc66e5-846a-3927-bc6f-8caea64d7eb8 | -10.86418 | -47.82297 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ec534de-6597-3dff-bae6-0d821fae2ddc | -13.32311 | -47.23155 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c995b42-109e-3d85-a49f-8cead03534b6 | -12.6888 | -46.91356 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 000d03ba-c44d-3ddc-afe5-d48b2e1537c2 | -15.24578 | -48.08845 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2991ce23-8ea3-3f07-8788-61ef5e0e234a | -15.22377 | -48.73608 | 2025-10-02 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f8e009b-0fc4-32dc-abcd-7718c045ecce | -12.88758 | -46.92774 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b6b65d6-b77a-3e99-9a8d-33353299ee33 | -9.80402 | -47.82626 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e11e62c-9395-35ad-8e2e-05b63ec26c25 | -9.45117 | -50.90438 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ea64044-1bad-3726-b778-4938d1ce1a74 | -13.29903 | -50.6777 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aee7b12-b4a1-3c25-9b3e-0ce5f4579a65 | -11.06323 | -47.81864 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14433dbc-45af-3068-89ff-5d3d99543bcc | -10.68232 | -48.57944 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8fa0d881-2132-3f97-adfc-aacffe6523f3 | -16.03618 | -50.85844 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7bbdede3-3d1c-3aac-b7d5-dc470b45dc60 | -14.97621 | -46.86919 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 514cd2c4-082d-30c4-a2c9-668f936e64a4 | -11.86248 | -45.0047 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82a2de67-f086-34bc-9789-ea9e219e33ba | -15.35127 | -46.28141 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ccea705-99ae-3b38-8304-40367c367732 | -12.70792 | -48.59256 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 90311de0-0ef3-39ea-93e9-287cc2df8064 | -14.68255 | -48.11472 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eed82b27-57ce-35cb-bb6b-c61b6dd614cf | -10.32663 | -45.25341 | 2025-10-02 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67a6d250-8ef4-37ba-b9a6-99c0f451d50d | -12.25491 | -47.80072 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2306c3bb-52c3-35a4-8012-20a19bdc0833 | -14.8363 | -54.78158 | 2025-10-02 04:51:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f28e1d16-c9dc-3397-a819-3b659d97e808 | -13.76037 | -48.69336 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a68c3d4d-28fa-36c5-9836-d5a9170c5f17 | -10.83007 | -46.63805 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2d53ff2b-c140-3cb8-b9fe-fb4836768f7f | -14.89699 | -48.33445 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7e35876-38bb-3ce5-8c05-27e034cc5f2a | -14.36823 | -45.95283 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ca6d848-49e5-3e55-8683-5ab434c51bb1 | -15.02504 | -55.27969 | 2025-10-02 04:51:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54920c8d-b93f-30ec-ab2c-2c8db4e950e8 | -11.4451 | -43.50117 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f805c3f-55c6-33c6-975c-f63d55d3e2cd | -14.90183 | -48.33085 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc0c9094-98ac-3372-8228-2059a34796e9 | -14.31891 | -45.98268 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dddcf62f-1922-3ef7-8f00-da4714d387d7 | -14.4761 | -48.43364 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 381f5f75-a31f-3be4-8159-895245e57b33 | -10.82614 | -46.63272 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8184694-8f94-37a5-82b2-1dd80732f6cc | -9.92863 | -43.71539 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 415887a5-332c-35fa-9953-21913f4aa8f5 | -14.03471 | -48.00241 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d77a453b-b7ea-36e1-8ed9-aec155c2948f | -9.8567 | -44.60676 | 2025-10-02 04:51:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4157a837-170f-399c-a6c5-6b38928696a7 | -13.31149 | -47.00442 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1dd40c7-c1a5-3d3a-9ffa-41b2a6be37dc | -13.16057 | -47.84195 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e108a58c-907e-3b04-b92e-190882fc9a83 | -12.25089 | -47.82986 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 942582cc-60e4-3f24-9e85-217f134e9780 | -13.15451 | -47.82072 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9731e096-2a5a-3070-ba1d-46ddbaecccc9 | -16.36587 | -47.07482 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df37968a-dcfe-3614-969f-b7d57de79431 | -16.00664 | -50.90609 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4b360fe-e7d0-376e-9b8f-f35e65c6ef02 | -11.0066 | -46.57474 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a3e9fdd-4f49-3c94-b842-01093295c5eb | -15.26042 | -49.29863 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67d5160c-b4e6-3561-9a6c-8334cae09846 | -11.59371 | -47.23096 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a98509a-d662-3e0b-abed-d994921155d7 | -10.68436 | -48.5648 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8277a484-3dd5-3d06-889c-f25c331ab37a | -13.55989 | -47.28338 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d48f8ea-8a23-3d5f-84ff-d8a514f4724e | -13.38768 | -46.95343 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23345bb0-742f-32d7-8d6b-53d5d50c42bc | -14.47241 | -48.42875 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48feb43f-663a-334b-b9b1-ab49c399fc54 | -10.35238 | -48.20869 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b33c0b75-d445-3db4-8afc-c5c6da779bd4 | -15.9348 | -46.2454 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3936b6a0-c8f1-399c-8ac7-730bf339fe0c | -11.81405 | -47.58745 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad301e5f-f61e-32e2-9556-f7c0922c067d | -10.48927 | -49.37106 | 2025-10-02 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 215ede71-2845-36d1-a87e-09e26dd4e556 | -11.64866 | -45.31361 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d6d0f80-9737-397f-a0d4-95854fda6d88 | -11.81484 | -45.00779 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f069b47a-edc1-3a43-a0f0-0dd749f98169 | -15.22953 | -50.1133 | 2025-10-02 04:51:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f30812cc-70ea-3639-af3b-1279ce07ce0f | -11.71251 | -44.46612 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ae88c40-15a8-35a2-ab20-ad2b25cb3dda | -14.8932 | -48.32988 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4042232e-7a5f-3c94-b95f-0f187229320b | -11.47554 | -44.99005 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd7769cf-c308-36f8-bd50-91fe48ada082 | -9.81775 | -48.25805 | 2025-10-02 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ea09151-1d08-3eed-aac8-4231dc628cc0 | -15.34508 | -46.29134 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ebb6a3a8-e186-3439-8eef-92d3bcc6e2bf | -13.69358 | -48.62582 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4e22073-12bb-34cd-928f-5328e39e29f2 | -11.85791 | -45.04016 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07507606-f136-3a3f-9eb4-1137e6c20457 | -10.23201 | -50.31413 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f421e238-3bf4-31ed-a415-e16fa2468d81 | -10.29298 | -51.07439 | 2025-10-02 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ff15823-95b0-3e3c-b801-a62f0162ea6d | -14.6495 | -48.13047 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2d0faf7-6238-3b6e-ad4d-2eccebe49889 | -10.83895 | -46.60607 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01f73c74-ca5f-30b4-ab1c-0b6a9641409f | -9.70852 | -48.95271 | 2025-10-02 04:51:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4af9112-8777-3c95-95d2-976571f86e9c | -15.31701 | -46.39144 | 2025-10-02 04:51:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8145b276-cde5-3c50-bff2-bb59152c3e07 | -11.82757 | -44.99006 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37c3caca-5e05-3d76-9aee-d34886caeea0 | -14.08673 | -46.66162 | 2025-10-02 04:51:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0bc3a788-caa2-3298-883c-bbae4a4e0188 | -12.41265 | -47.50163 | 2025-10-02 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 133a93e0-39e0-3ba9-beb1-65ad0e0f6336 | -12.58698 | -49.89905 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10d3108a-06ac-3f97-845f-931879e3a55e | -14.89494 | -48.33258 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4419e978-e1a5-37a6-a766-b6b4ea978db7 | -13.94977 | -48.09578 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3020867a-c214-36b8-b32e-a47156a07c4e | -13.30863 | -47.83539 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b294766e-009b-3d0a-bb34-74fa825feb86 | -12.84221 | -46.95325 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98279cb0-3554-3d64-ac14-44d955897d71 | -11.26887 | -47.82776 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b417b6e-7c0d-3edc-824d-46937ac8488b | -11.58456 | -47.66007 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f569ea1f-7fed-3c4a-90ea-708379526f4b | -16.04797 | -51.03075 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 175358ad-7c82-3d84-8ff5-85b35523e166 | -10.66574 | -48.52268 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c437d30-3dd1-3ddf-9751-6c7faf5344b3 | -10.44421 | -48.08547 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ebae46d1-4c3d-3983-a261-b18eb5c921b5 | -15.16591 | -52.80029 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README116.md)
