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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a8f78ea-7731-3423-b81d-b905d7a55cc5 | -15.90095 | -57.48393 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 37c7ab5d-4e0f-3d7d-ba08-4bb8538ae138 | -15.88928 | -57.47056 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227bcbe3-ffcc-3db9-8389-94264a6a6b37 | -15.88649 | -57.4664 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efe1289b-0956-3003-b091-47cf04a23866 | -15.88561 | -57.49303 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4c883b3-f860-3c0a-95c2-ad04d6a7f05c | -15.88313 | -57.46583 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a93fd42-b1da-34c4-99db-0400ed6ab193 | -15.88034 | -57.46166 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69183ae5-5c31-3b6d-b607-5c59065afb07 | -15.87857 | -57.47252 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29ac68d4-e759-3d9d-b7ee-a88aa47b9f81 | -15.87794 | -57.47632 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e32d010-8757-338e-a7db-53dd26ca6cbf | -15.87732 | -57.48011 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7c49580-ffed-383d-8843-29b6a9287397 | -15.87698 | -57.46106 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed4a974b-edba-3fe8-818d-192824914736 | -15.8758 | -57.4683 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00299b4e-eba8-3e34-8e7f-0b375b43b5f7 | -15.87457 | -57.47578 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc17be0a-eded-3f6e-adfa-b866176372ba | -15.56533 | -57.46505 | 2024-10-08 04:59:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4465f4f-3c29-3b3a-a42c-158fb2f4e5e0 | -15.56195 | -57.46446 | 2024-10-08 04:59:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87c49513-d75f-35f2-9b09-efd68fb9d9b9 | -15.55919 | -57.46018 | 2024-10-08 04:59:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4527e8c-c07e-39b5-bcb4-75c104b41fc5 | -17.19717 | -57.33609 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f9fd8720-d2c0-3090-87c1-aee36fdb667f | -17.19383 | -57.3355 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 8b9b22a5-ea9f-3b1a-a9ab-d479607c4fec | -17.19265 | -57.34281 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8379a606-1a93-39f4-81d2-1faae21d03ac | -17.19108 | -57.33126 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 97c78518-ffe3-3c1c-bd62-7d168def8e7b | -17.18871 | -57.34588 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 7a23f252-0bb3-3c01-bcae-eeb79ae9f2ce | -17.18812 | -57.34953 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| e9a856bc-1f46-331a-b495-a48ce23301e9 | -17.18773 | -57.33068 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1820d30b-b029-3c7d-9fe3-e70ce9de40ee | -17.18714 | -57.33434 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6a6b81d7-6131-3a60-9360-d2ad10f1003f | -17.1838 | -57.33375 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a3badb90-a77b-3108-aa8a-dfb1ebf2c82c | -17.1783 | -57.32527 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| b797a521-be33-3081-85c2-9aa8e256d2bd | -17.17652 | -57.33624 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 161cd68e-39a5-3e2b-aca2-2d8d3be0f8dd | -17.17495 | -57.32469 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d612d948-010f-32ff-81de-202a50490921 | -17.17318 | -57.33566 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cdc423e3-ff44-38ea-b0e8-9341d713dcfb | -17.17297 | -57.35817 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 834dc51f-a69e-3092-b2b3-cbee7ed205d2 | -17.16687 | -57.35334 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2d1d6107-c4df-3595-971b-60e08dbc1318 | -17.16628 | -57.357 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 651c9787-4131-3e55-875e-ede267bd0fe7 | -17.16596 | -57.34942 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2de18689-eff3-30db-a73b-67ee240317fa | -17.16537 | -57.35308 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3f6f4e42-a4a5-33ef-8687-75edbab59f4b | -17.16379 | -57.34152 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6f7b54b7-1707-3809-b267-60bf484466bc | -17.16261 | -57.34883 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e7680836-8bd2-3c1b-a551-d3883de0dfb9 | -17.16202 | -57.3525 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 60e09884-2daa-366e-ac90-1b5987a338ad | -17.16072 | -57.41249 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9c316e60-e609-3a64-92c6-4ea8c6037026 | -17.16012 | -57.41615 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2ea31684-88e7-34d4-882e-d22ab18a1521 | -17.15927 | -57.34825 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c5963650-d2b9-3ae3-bfcf-2710d8a42078 | -17.15678 | -57.41556 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 64ddf4dd-da54-381e-9f3e-d5fa5f8d115e | -17.15143 | -57.4184 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4660d562-4dec-3f32-8173-b21fe0092ca0 | -17.15084 | -57.42206 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 23073e0e-ad1b-3443-bfec-bc3ac7f53461 | -17.15041 | -57.33918 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 37c618a9-6e31-3e08-86d5-ca0c107f5936 | -17.14765 | -57.33495 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| d4b874f2-9a7e-3a4a-9df5-9127803768a5 | -17.14707 | -57.3386 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0cf7c74d-25fc-3363-878b-e21b49b17ffa | -17.14631 | -57.4288 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3da7a9ec-6789-3048-af7f-24ca8afb3997 | -17.14471 | -57.35323 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b1ee0ef4-5e55-3b8f-b58d-a6364a38fc2d | -17.14296 | -57.42822 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8fd7dbcc-af01-35cb-82f4-d9251ef8c63c | -17.14237 | -57.43188 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bc0795db-623a-347c-a016-1eece23ebea5 | -17.14137 | -57.35265 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d3d33bd8-782b-3f73-b65c-2611547b337c | -17.13962 | -57.42764 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f3d9c800-9441-37e8-b6be-f2a4833de041 | -17.13902 | -57.4313 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3fda76a2-f309-3465-89b3-8929cb2cabc9 | -17.13861 | -57.34841 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d37f63ce-d828-375e-94e3-b8b5a32f57ca | -17.13627 | -57.42705 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f484bb1c-f4d6-351a-8b64-09e20845cce3 | -17.13585 | -57.34417 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a7d65318-fc8d-3df1-8f58-e78181f63215 | -17.13527 | -57.34782 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 40902b31-92cb-375e-b615-560cd6940e56 | -17.12228 | -57.42837 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| abe5f2a7-a31e-3760-be43-653a4d56165f | -17.11953 | -57.42412 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 4e863bcf-ee05-35ca-8661-6f17372b40b9 | -17.11893 | -57.42778 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 67441337-a43e-3006-af79-d4ba00c1eb69 | -17.11834 | -57.43145 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| ed45739e-cdd3-33ff-9619-a3e85ecc1fd5 | -17.11618 | -57.42353 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 235163e4-0b69-3b60-9307-643c515f568c | -17.11559 | -57.42719 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 76c6ba9b-f5fa-3934-8f6a-839afa6ae1a0 | -17.11499 | -57.43086 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 8eefdee2-67ca-3248-bb77-20db7cb6da00 | -17.1144 | -57.43453 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 09afd116-fb96-3a81-8b77-173bb8be66bb | -17.11224 | -57.42661 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f386dd6e-0f3a-374e-a858-80ba9fe01532 | -17.11164 | -57.43027 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| aee51432-0a1c-32d1-b8eb-1af860ad301d | -17.11105 | -57.43394 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0ea924c1-590f-3d0a-8133-47d6bc600ec8 | -17.10889 | -57.42603 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5ac255a2-8a6d-30a6-9d3c-be36b6fe1053 | -17.1083 | -57.42969 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4b636d36-71b7-31bf-826a-2ab2b3f4d8a3 | -17.10162 | -57.36451 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 314e997b-669e-30e0-9cc6-bf176c4481bb | -17.10103 | -57.36816 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| db694288-b65e-36cd-8aa2-214384282bab | -17.10044 | -57.37181 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c73bd24b-1704-3f31-a51b-2347139ea30a | -17.09985 | -57.37547 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fea343dd-dd90-3db5-aa17-580c3977f7fa | -17.09828 | -57.36392 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 729bd950-273f-3562-b596-2b0939e55e15 | -17.09825 | -57.42793 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 713c19a5-affe-301b-8ed7-79e0d02600bf | -17.09769 | -57.36758 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9aeee91a-5b39-39c1-a49e-a3587bfcfe04 | -17.0971 | -57.37124 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a4ad18c6-6364-3984-b1ee-ff236fff58a1 | -17.0965 | -57.37489 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bcb1879f-7996-3cb5-8df8-9958d151add6 | -17.09434 | -57.367 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 944bcb1d-dd73-3f75-a350-7f63d793427f | -17.09375 | -57.37065 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| bc9dc2f0-3363-3881-a08a-9f39429bc820 | -17.08821 | -57.42617 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f08335df-1e79-3f7e-9b58-1b37c9b6c142 | -17.08545 | -57.42192 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 21254c52-69cb-3606-988b-b3f0a94d1e78 | -17.08486 | -57.42559 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5675a2b8-451b-3c0e-b558-16e5ccb36155 | -16.68536 | -57.10985 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 5bd21382-7f5d-3982-aacd-55aabf1a8361 | -16.68477 | -57.11348 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7a6ebb8f-a1a8-326b-b7ea-8c373323404c | -16.6826 | -57.10564 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 37f9f6df-7545-3c26-992a-b4c197641462 | -16.68202 | -57.10927 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| f14366bc-cdc8-3cd7-9463-b74bbbbfd009 | -16.67926 | -57.10506 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 0f4277e7-c579-3bf7-9c45-276c974d192e | -16.67651 | -57.10085 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 840a7b7c-492a-3c4d-91ca-6dcc4812c987 | -16.67634 | -57.12323 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 8324654e-78a5-33f5-b05b-d612aacf9fdb | -16.67593 | -57.10448 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 011741e1-71aa-33ae-91c7-fa672d395fdf | -16.67575 | -57.12687 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| e6cc7ed1-c82b-37cd-be8d-79fc3592ed51 | -16.67516 | -57.1305 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 5a85ad28-8107-3442-a69c-6306d1f7b2ab | -16.67458 | -57.13414 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 94ed1165-6c17-3cd3-bf94-0c45c9762133 | -16.67358 | -57.11902 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d7129725-981f-32bf-8a26-b122031bae0f | -16.67317 | -57.10027 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 7756907a-8646-36bb-8116-adc5916abd67 | -16.673 | -57.12265 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 38dbc112-201d-33bb-9cd6-d2e96c61d09c | -16.67241 | -57.12629 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e0668e02-5995-3cb3-8db8-e8ffd329838d | -16.672 | -57.10754 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 18276b94-9dc6-394e-929d-3690e983a860 | -16.67182 | -57.12992 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |


[Clique aqui para ver as próximas entradas](README103.md)
