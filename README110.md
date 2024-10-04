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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77bb3d79-64e5-30e2-be1b-2bb33e380e71 | -10.5626 | -51.08443 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d128a8d7-cf61-3421-af03-cf25d0f963f1 | -10.55911 | -51.08382 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80471de9-5c7b-3960-b810-6fe5b9f7a1d5 | -10.55562 | -51.08323 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ee34c33-f8c7-3ec1-92cf-29f3952ea0f3 | -10.55213 | -51.08263 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8480f19b-d571-3eb2-a911-d2fbaf27508f | -10.54864 | -51.08202 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e83107b0-c7ef-32e8-a4e2-b214e8af30c5 | -10.54515 | -51.08143 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5ba697c-f261-38f6-8a19-18273c0e03b9 | -10.54432 | -50.97754 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 37f8af85-4ead-39ef-9447-b343272aaaca | -10.54368 | -50.9814 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56dc43c4-8624-3180-9d96-78f4dc3ec49c | -10.54339 | -50.96148 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8c2f9ad-8f65-3151-9967-56b555bb7d68 | -10.5423 | -51.07693 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b37001f0-c34c-3093-8b68-9c5f96e286e5 | -10.54084 | -50.97695 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e18e1ad7-776c-35d4-9a5c-f12e88abab8a | -10.54055 | -50.95701 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a3f0c90-f821-3f39-a8ec-8addc3994ff9 | -10.54021 | -50.98081 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9a885534-6242-3936-a4c9-ffe49901168c | -10.53991 | -50.96088 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00d01dea-3c5f-3eb7-80f2-b85e2da9415f | -10.53928 | -50.96476 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fa64a91-66a9-3db1-abd9-aa95dfbf10ce | -10.53881 | -51.07633 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f15cacdb-d5ca-3700-8073-c2fb6811f4f1 | -10.53864 | -50.96863 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d126fef-3cba-3106-af28-d6706ac3cfcd | -10.53772 | -50.95254 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3057c87f-de2d-3d88-ac38-a79373f9f181 | -10.53736 | -50.97636 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aee72eca-d666-3534-8e72-ff7a3e770d6a | -10.53673 | -50.98022 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b977ae60-b286-365a-98f0-e3171a83d60a | -10.5358 | -50.96416 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06fac104-e207-3a0a-92c3-19b073dbec24 | -10.53532 | -51.07573 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61b6a7b9-1bdb-3187-af31-3cf683ae0714 | -10.53516 | -50.96803 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13552b6e-ea99-35c3-9a7c-4557ab0534f2 | -10.53425 | -50.95195 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15da9278-f65a-3bc8-b21b-c95daceedcfa | -10.53183 | -51.07512 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca6b9b7d-e248-373f-9e44-9b08b8aff62d | -10.52899 | -51.07062 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 866ca170-9006-3609-b33a-fd72b7280c17 | -10.52835 | -51.0745 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 688f4160-3fde-3658-91fc-6cf340704dd5 | -10.52829 | -50.92319 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f67e3b1-f222-335a-a885-861729bc01c2 | -10.52486 | -51.07391 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f807e8fd-98af-31b0-9c57-3caaed0a9ad1 | -10.52482 | -50.9226 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1244ca3-3c69-3ce9-9e25-d6cd6ddd11c2 | -10.52135 | -50.92202 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d37c664-8909-3bfc-af3e-827dd6d90a31 | -10.51788 | -51.07272 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dce606f2-e2b7-35b9-ad01-60c361841b11 | -10.50961 | -51.07927 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11d14ab3-b7a3-3d65-b85e-525212a2faa1 | -10.50287 | -51.09827 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84129bf5-84ba-3504-81c8-a4fd3abaa568 | -10.50158 | -51.10608 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42b1ed83-4075-31fd-be03-19b1fddc36ce | -10.50093 | -51.10997 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e52bb51-89e5-312a-ba98-6076c5c6d45e | -10.49067 | -51.12844 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cefd6f1-7b6a-3245-b228-17ccde5beb79 | -10.48847 | -51.12003 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 433cfb62-659e-3279-a872-6b8b73ecad37 | -10.48782 | -51.12395 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d8fcd4d-2141-33db-9512-5d783cf92fa8 | -10.48717 | -51.12787 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7766e6a6-5d2d-3b07-bb70-4a1b183648c9 | -10.48432 | -51.12336 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc2c5e39-ac62-3d97-a374-73d8438af309 | -3.49708 | -50.81315 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60152027-ed8f-3b12-92cd-4281c7023d67 | -3.49481 | -50.80362 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b514da60-b1ee-351a-be5e-730e80a76e03 | -3.48961 | -50.80482 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29851e58-633c-3a2a-8c06-d0ae16a24385 | -3.49335 | -50.81252 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 111d670c-38ba-36fb-8185-15ee1575648d | -3.49107 | -50.80303 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c106e887-5218-3b70-b8aa-9377e2d2c738 | -3.49035 | -50.80747 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4b431db-cacb-3c4b-aaee-5fb7be5ddeea | -3.37053 | -51.2118 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a08038d4-2193-3a0f-8301-dff675bef672 | -3.36977 | -51.21652 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46ba513c-b080-3cdf-bc36-3c69d8ef4746 | -3.29657 | -50.76254 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5245e8ce-d042-3b33-af22-e5e29ce35651 | -3.25597 | -50.94042 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e057c6fe-6c9a-342d-b5d7-7474fee11530 | -3.2522 | -50.93982 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36ece64f-fd24-304d-8436-ba0fae9705bc | -3.54736 | -50.85783 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2f550069-86ea-3447-b2c9-fd8692344e00 | -3.49781 | -50.80869 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5a05b703-b3ec-3479-a4e1-6264a0250437 | -3.49408 | -50.80806 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fb3c094c-5e4f-3e7e-b587-ca07a19f9e83 | -3.48962 | -50.81191 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5116c6b-2932-3373-a491-29124d1a3c82 | -3.36671 | -51.21119 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffc64bee-30eb-31a1-b041-8f3cfc29f48e | -3.36595 | -51.2159 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef86a73d-5042-357a-a4f5-e78e6630ac85 | -3.31981 | -50.78464 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1bb825e-b119-3f41-9c26-ae4fb7e5acef | -3.29356 | -50.75748 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be018732-da97-3c45-b718-e550b1efb42d | -3.29283 | -50.76193 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fed58e3e-a636-3997-b896-8b07b15e247b | -3.28983 | -50.75689 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fc5fcb1-3b5f-3df7-92f8-bdcb2a417834 | -3.2891 | -50.76134 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85a54a1f-08b2-35f3-9774-b6d445baff1d | -3.25193 | -50.94204 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58909412-63a9-30c6-8a90-05e678c49289 | -3.22528 | -50.79428 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4226d421-598e-349d-b9ba-f80f3d13b8fc | -3.22153 | -50.7937 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03f3727e-3b51-36e8-8cdc-50c7a0e6d79e | -3.15595 | -50.88938 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29edc1f9-add1-38ef-a9fc-7fa282ef254a | -4.09562 | -51.11897 | 2024-10-04 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99ed920c-1bb8-39ca-b5f9-42c6f5c18c4a | -4.09184 | -51.11841 | 2024-10-04 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbe03966-d137-37b9-96cd-3108ede308e3 | -4.05397 | -51.11398 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aafdfa2a-4ba8-3d2b-a377-94c780e311e4 | -3.90227 | -51.26645 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 920adc82-b756-39da-9fe2-cd22c16472ae | -3.90152 | -51.27108 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42ae5cba-8e51-3611-8a5c-8829602d7470 | -3.87589 | -51.81933 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aff6d341-c89f-38f0-9850-d7993dbf4800 | -3.87259 | -51.37693 | 2024-10-04 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 210c4bf0-76a2-3ba9-9127-6ad667af672f | -3.82862 | -52.1803 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea4a244c-4039-32b5-979e-70783adf14b5 | -3.82517 | -52.17609 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab841215-8474-3e37-8178-c9da45ae0efb | -3.81159 | -51.18223 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 120ef2e9-e01a-3a45-b464-07754efb71bf | -3.79432 | -51.66089 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9814a09a-e245-3f31-a491-593dcbffb25c | -3.7871 | -52.2603 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20e22f12-fdb4-34f5-9acf-6a3287ecd2a0 | -3.75225 | -52.24364 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9451bd4-a0c3-37b4-a88d-8f92b7fca941 | -3.73532 | -51.36185 | 2024-10-04 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 733027bc-7944-3a5a-98e0-1e141a7ff3eb | -3.67429 | -51.3892 | 2024-10-04 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5118c676-529c-3b48-b4d5-47722778259d | -3.67044 | -51.38858 | 2024-10-04 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 874a0cb4-c773-3633-9b9a-609bed57ab3c | -4.04553 | -51.09435 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77e33110-31e5-30e1-8803-9a45b9b95f82 | -3.83266 | -52.18095 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 244283db-01e7-32b3-8160-fafdd237f7d9 | -3.83209 | -52.18444 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e738702-4d91-30d2-9941-94283622c64f | -3.82804 | -52.1838 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 529010e0-a63c-3deb-9182-2d9577c7758d | -3.82458 | -52.17964 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e24b4437-aa7b-3a3f-bbac-fdbd723f94e0 | -3.80778 | -51.18169 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 08d98536-bd64-3931-9175-9c3bf9b297e4 | -3.7935 | -51.66583 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41e0f036-c3c1-33ff-9bc1-b9dbf8a91909 | -3.78618 | -52.2606 | 2024-10-04 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 988a9963-e083-34bd-ac31-b2388f036f45 | -9.0715 | -53.25093 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a547045-de99-3c2e-ac57-8c9a718a684a | -9.07061 | -53.2561 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0469b64-5f5e-39ee-bd6e-35ae427ad081 | -9.06972 | -53.26131 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fcf2c09-edf1-3e39-ae00-fa43a0512981 | -9.06751 | -53.25023 | 2024-10-04 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 509e3a17-9c30-3303-9e1f-3b6fa34edaed | -9.06023 | -52.96851 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b38f16a1-882f-35eb-9b4b-0f4d6420c5be | -9.05713 | -52.96291 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b27bbf7-55b5-369b-8e9b-2afd8df44d76 | -9.0563 | -52.96788 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67a7e6ad-4f78-32a2-9da8-6843b5a5a586 | -9.05547 | -52.97283 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0d75e6f-3881-3248-be70-ed6bbcee2cf0 | -9.05465 | -52.97769 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README111.md)
