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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 021a1fab-af0c-3231-86af-b59e8413158c | -18.2043 | -54.455299 | 2024-10-08 00:59:05 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| edb8bd1f-4b46-3c23-8c48-1e632b546fb9 | -18.074499 | -54.312302 | 2024-10-08 00:59:06 | METOP-C | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 55d71bd2-5979-3a20-a2e2-fc63b3d8640b | -17.685801 | -52.634899 | 2024-10-08 00:59:07 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f49941ab-4ea8-3266-90f0-5c77ac9c91d7 | -18.6035 | -57.229099 | 2024-10-08 00:59:07 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3a49c56c-e82b-31d2-bc01-1151f069ff19 | -18.6066 | -57.245998 | 2024-10-08 00:59:07 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 577f61c0-e978-3b45-a373-e9116c0654be | -17.780899 | -53.0494 | 2024-10-08 00:59:07 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dd131aef-02a9-36f9-a04b-156cc66e1d1e | -17.247101 | -50.707298 | 2024-10-08 00:59:08 | METOP-C | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cc08578b-33a6-3c80-a196-0782502d8c34 | -17.248699 | -50.714699 | 2024-10-08 00:59:08 | METOP-C | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 287f8be5-6808-3f2e-b22f-52b8b61d4c52 | -17.7167 | -53.034901 | 2024-10-08 00:59:08 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f3d7394-4116-3b92-9c56-a5d81a89d5a2 | -17.7185 | -53.043999 | 2024-10-08 00:59:08 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6ee98bd7-34fe-356a-834f-0825c71db4b0 | -17.7069 | -53.036999 | 2024-10-08 00:59:08 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 16c72e5f-53cb-39f6-a71b-eb8bd9f877b8 | -17.7087 | -53.046101 | 2024-10-08 00:59:08 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 593c5926-c4f9-3a79-916c-f7790ab41121 | -16.183599 | -46.418999 | 2024-10-08 00:59:09 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c72c4d24-a3d8-39ff-b9a5-97bb83a4dde0 | -16.1856 | -46.427601 | 2024-10-08 00:59:09 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d6f1b51e-c8d6-365c-8f5a-1e83ce80c06d | -17.664101 | -53.0275 | 2024-10-08 00:59:09 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c26b2f9a-687f-388a-be66-ccf433a17409 | -17.8328 | -53.760799 | 2024-10-08 00:59:09 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f2d3fc63-df1a-34f6-871d-653b010690f6 | -17.8347 | -53.770699 | 2024-10-08 00:59:09 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 842a8fbb-3f0f-3a0a-8989-9c983ff263e9 | -17.3673 | -51.9902 | 2024-10-08 00:59:10 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f30fd95f-db5c-3524-a869-c678a8d47c88 | -17.368999 | -51.998299 | 2024-10-08 00:59:10 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9311b804-2d17-32c5-97f1-a85b6e6ec5ed | -17.3575 | -51.992401 | 2024-10-08 00:59:10 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1cb691a-cfef-3cec-a78c-520b70df5d9c | -17.3592 | -52.0005 | 2024-10-08 00:59:10 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fea59ee9-4932-3f77-91c9-439583948d22 | -17.360901 | -52.008499 | 2024-10-08 00:59:10 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a9413337-7246-3bce-bb8c-69369717b5f5 | -17.158199 | -51.679901 | 2024-10-08 00:59:13 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df52e5c4-d032-3073-b2b2-9a517eb73384 | -17.1598 | -51.687801 | 2024-10-08 00:59:13 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b65db34d-f671-3a2f-8c57-f9da08a0ec53 | -17.161501 | -51.695599 | 2024-10-08 00:59:13 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7bca7250-3fbc-3e0d-b9be-4b111ee4b867 | -17.15 | -51.689899 | 2024-10-08 00:59:13 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 574eed36-bb49-3f69-870b-7883fbf66eb9 | -15.745 | -46.017101 | 2024-10-08 00:59:15 | METOP-C | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3b22f12d-1e81-3694-ac2c-53dcc06dd790 | -15.7352 | -46.0196 | 2024-10-08 00:59:15 | METOP-C | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 10da755d-55bc-39bf-8d34-736be9c150cc | -16.2332 | -48.745602 | 2024-10-08 00:59:17 | METOP-C | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 196a4b6f-374c-3b5a-a7eb-090bdabd41c1 | -16.4063 | -49.924 | 2024-10-08 00:59:19 | METOP-C | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 600bd329-55e7-382c-bc46-5efc8b3e09da | -17.334801 | -54.9995 | 2024-10-08 00:59:21 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0bbcf5fa-5c40-3cbf-bac3-f2f1e3f15ca9 | -17.337 | -55.011002 | 2024-10-08 00:59:21 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a26ebc0f-4b4d-3f9f-bab2-097705a058e8 | -17.325001 | -55.001499 | 2024-10-08 00:59:21 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d5aa999d-7ff2-3c1b-b0a5-6e60813c0c04 | -17.3272 | -55.013 | 2024-10-08 00:59:21 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39df47dd-ddd1-3267-83e5-008e842ddd20 | -14.5343 | -43.2066 | 2024-10-08 00:59:23 | METOP-C | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc2df649-f615-3de4-971d-c0f2e05ddb77 | -16.4112 | -51.880699 | 2024-10-08 00:59:25 | METOP-C | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c7623c60-882c-397f-92bd-ce3a44c9a127 | -16.093599 | -50.184799 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ccc1a393-f319-3020-818f-ad2b866a96fc | -16.0952 | -50.191898 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 08ff3ef3-bbdc-3f8c-a252-b62c078910b9 | -16.0968 | -50.199001 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 151b0e77-7e02-382e-8411-03cf62edbc2d | -16.0984 | -50.2062 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 01bee4c6-cbe2-35d0-b326-e38798b5c669 | -16.1 | -50.213299 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a7379677-3976-342b-8063-c98a23474bea | -16.101601 | -50.220501 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3c9b0204-61da-31ce-9c5d-365c92780d41 | -16.1031 | -50.2276 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed299c3-c8ae-3cee-b9b6-d2cf97234924 | -16.0839 | -50.187099 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb400b7-88fd-3cf6-bf6f-d0caaa1cfc11 | -16.085501 | -50.194199 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 196e8fb0-e9a8-33ab-a5d1-ac53f9a890c8 | -16.087 | -50.201302 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9db9756d-c176-3217-8333-edc160dbd6f5 | -16.0886 | -50.2085 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0e77fbf5-66ec-3192-be1f-80b774f709f9 | -16.0902 | -50.215599 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fc67ba3a-a776-3a0b-8379-8f3cd7e4a197 | -16.0709 | -50.175098 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 024c57e1-a089-3946-9395-b50ded7d3378 | -16.0725 | -50.182201 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3d3c17e2-39f1-3194-965d-55d733b764f9 | -16.0741 | -50.1894 | 2024-10-08 00:59:25 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6bc729e6-a94c-3eb6-b29e-807ab6e765a8 | -16.3078 | -51.446098 | 2024-10-08 00:59:26 | METOP-C | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 701f0c85-6073-35ea-8441-c49768d78692 | -16.309401 | -51.453602 | 2024-10-08 00:59:26 | METOP-C | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0304b6e2-a070-3288-9913-29efc19e485a | -16.298 | -51.448299 | 2024-10-08 00:59:26 | METOP-C | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 62107064-2b9b-3d08-92f4-58af5305c97a | -16.299601 | -51.455799 | 2024-10-08 00:59:26 | METOP-C | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c2ea9a3-da96-3dcf-955b-b4cca3f3f214 | -16.0676 | -50.439098 | 2024-10-08 00:59:26 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f093700a-2433-378f-877a-9f205ed3c00d | -17.1537 | -56.110699 | 2024-10-08 00:59:27 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d55bc85f-f187-300b-b348-c4f5e6c92932 | -17.1563 | -56.124199 | 2024-10-08 00:59:27 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7849c61e-824f-3f63-9c8f-e2c4c9fb9e19 | -14.7024 | -45.144001 | 2024-10-08 00:59:28 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f02fe69f-313d-3464-b6eb-de517bfa4a40 | -15.766 | -49.962299 | 2024-10-08 00:59:29 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c6239ad8-86a5-3e51-b934-c3c2760fe2eb | -15.7676 | -49.969398 | 2024-10-08 00:59:29 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4963d014-42d3-3cea-b0db-bee05d987edf | -17.117201 | -56.826199 | 2024-10-08 00:59:30 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81394ad6-3b8a-30c2-a202-824136ac28c2 | -17.003099 | -56.649502 | 2024-10-08 00:59:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 122e376f-4fbb-3f06-b398-9a34ff5fa24b | -17.0058 | -56.664101 | 2024-10-08 00:59:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 391002ed-6558-3ecc-8637-2ca87b140603 | -16.996 | -56.666 | 2024-10-08 00:59:32 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a72672ef-218c-3129-8d2a-3b1506a4c183 | -16.9988 | -56.680599 | 2024-10-08 00:59:32 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 947323d6-624e-346e-a4c8-9a49489236e8 | -16.9891 | -56.682598 | 2024-10-08 00:59:32 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3678a2c7-9c5c-352e-bcfc-e03c5c9c99d0 | -16.9821 | -56.6991 | 2024-10-08 00:59:32 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 288058e5-a6ba-3889-a33d-5998ee78ef15 | -16.9848 | -56.713799 | 2024-10-08 00:59:32 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9606b916-787a-3325-ab85-abcec4a0d6c4 | -14.1157 | -44.083302 | 2024-10-08 00:59:33 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d888554-fc9a-3c34-b94e-3aecf5ebdc16 | -14.1188 | -44.0956 | 2024-10-08 00:59:33 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01144c2c-b68f-325e-9d82-20c37c92f8b8 | -15.9443 | -52.240799 | 2024-10-08 00:59:34 | METOP-C | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8534e585-5e06-3fd3-824b-d7be45b209c2 | -15.9329 | -52.235001 | 2024-10-08 00:59:34 | METOP-C | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b4faa852-e2af-32c2-9e42-63fd01e01070 | -15.9345 | -52.242901 | 2024-10-08 00:59:34 | METOP-C | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ba3c91d-8a43-3165-83d2-5b326e23deed | -13.4712 | -42.4603 | 2024-10-08 00:59:37 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c024cbf5-7110-3974-8eaf-df64d9f5946c | -13.4753 | -42.476398 | 2024-10-08 00:59:37 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 98b71d89-dbea-3936-a01e-aeaa3c600233 | -13.9476 | -44.608501 | 2024-10-08 00:59:38 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 566e0526-adc7-35ab-8da1-3eca753da474 | -13.761 | -43.990799 | 2024-10-08 00:59:38 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2330ef36-030a-33d5-b81b-caad6fa4141d | -13.4172 | -43.778702 | 2024-10-08 00:59:43 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 942e4f74-9514-3526-8e9a-16d7c75f3d67 | -13.4206 | -43.791901 | 2024-10-08 00:59:43 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2cefc10c-70a0-327e-bf8c-3459edbf81ea | -13.3814 | -43.759998 | 2024-10-08 00:59:44 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f41ccfb0-8427-317f-8a57-7245828f899b | -13.3683 | -43.749298 | 2024-10-08 00:59:44 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6748e9b0-8412-3417-903a-38eb2fda3238 | -13.3717 | -43.7626 | 2024-10-08 00:59:44 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97cc789f-1c95-3b1a-a30b-33d843d5e6ff | -15.0429 | -51.251701 | 2024-10-08 00:59:45 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 52e3ea34-314f-3ef1-9833-8f8575e7af51 | -15.0445 | -51.258999 | 2024-10-08 00:59:45 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0cd230ab-d111-39e5-86a3-103180832327 | -15.4877 | -53.379398 | 2024-10-08 00:59:46 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d39bbd6-2325-360b-8a36-b1283fa4d1c2 | -14.8013 | -50.762199 | 2024-10-08 00:59:48 | METOP-C | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7780b1a0-57b1-3b98-baec-705d4d59ad2b | -14.8029 | -50.769299 | 2024-10-08 00:59:48 | METOP-C | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44e95b49-d55a-3453-a348-6cfdbcfb5a44 | -14.7915 | -50.7645 | 2024-10-08 00:59:48 | METOP-C | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e8960f8e-7a3c-3517-a3bb-c608c029170a | -14.7931 | -50.771599 | 2024-10-08 00:59:48 | METOP-C | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 36f46928-ee2f-3151-bd62-efd9d28b9359 | -14.7947 | -50.778702 | 2024-10-08 00:59:48 | METOP-C | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b02008a-8d1e-3bf2-8de0-b003551f66eb | -14.1577 | -49.685299 | 2024-10-08 00:59:54 | METOP-C | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab22027d-9b3b-3581-9969-46855c3f58dd | -14.8128 | -53.919498 | 2024-10-08 00:59:58 | METOP-C | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a9e85d9-1e08-3495-af00-37432b6738ea | -14.803 | -53.9216 | 2024-10-08 00:59:59 | METOP-C | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54fd1d8e-9ad3-33de-b407-65e7be913951 | -14.8049 | -53.930801 | 2024-10-08 00:59:59 | METOP-C | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 673b7cd0-cbe1-309d-a4cc-eb1d3ec16f85 | -12.9961 | -46.203201 | 2024-10-08 01:00:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aee69157-ffe7-3bb7-8dd7-1eda55a241f3 | -13.5319 | -49.4744 | 2024-10-08 01:00:03 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dedda2ed-d4a3-384b-b2cd-86578ae9d852 | -13.5303 | -49.4673 | 2024-10-08 01:00:03 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 85561bbf-d13b-3f91-a3c4-3cd50d170edc | -13.5336 | -49.481499 | 2024-10-08 01:00:03 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 99bd5dde-09ab-3feb-9087-071228064b3c | -13.887 | -51.2799 | 2024-10-08 01:00:04 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)
