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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01146587-4fe8-3855-8f4a-2befd05d1b0c | -3.32521 | -50.12897 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a53d2fb-c195-3b35-8f29-a0b12dec6254 | -3.32244 | -50.12501 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41317cd8-7806-3881-961d-ee1198a6f332 | -3.32189 | -50.12846 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 805c48c5-0d0d-3c56-bc6a-3925e11d591e | -3.3091 | -50.10173 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85f109e1-33f5-3d14-b896-a0165a0842c2 | -3.252 | -50.01519 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba0418a2-db35-316f-aeac-b6381bb5edf0 | -3.22819 | -50.18814 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 240463cb-398f-3b7c-bd20-7294800b7ed9 | -3.22542 | -50.18417 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afe5ee0a-8c81-3d37-b393-e66d08fb8886 | -3.22487 | -50.18762 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87d3b78e-6b99-3b95-b788-6487458fcd09 | -3.22433 | -50.19107 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dab88eb2-4794-3f33-8391-5ad132e9a8e4 | -3.22264 | -50.18021 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4177107-658e-3aca-8c71-b9320580e2c1 | -3.2221 | -50.18366 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1142c88-63c8-3b42-a21f-27e724134117 | -3.22156 | -50.1871 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 791f58f3-1393-3e2c-a1d2-3671e79a33c0 | -3.21878 | -50.18314 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c1ca575-855d-356b-8104-5f80c766e54e | -3.20627 | -49.89488 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| face9839-34c8-372e-9d5d-7b187bccbf4b | -3.20573 | -49.89833 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 385dd589-5910-36cf-bcbe-f90083029b90 | -3.60759 | -49.86198 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62404e72-d188-3380-ba15-ff497a8c7e50 | -3.57045 | -50.03329 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b89216c9-b248-39b6-bff3-8d55b57728d5 | -3.5699 | -50.03675 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4d72b15-6da8-3db5-8174-9c480315530a | -3.56713 | -50.03278 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fce7e8ef-e503-394c-95be-96737ad1edb8 | -3.56658 | -50.03624 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23a1a721-da43-3ca8-8082-5e9fd4d2b857 | -3.5552 | -50.30313 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b975a1e7-7a62-3de5-81be-fd03172cb430 | -3.55466 | -50.30658 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83ab0e27-cb12-3781-ad60-602c2b8e4cda | -3.52721 | -50.37297 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d371ea00-033f-35aa-8eb4-9593d341ab9f | -3.52443 | -50.369 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce90527b-345e-3423-b710-f16df663fe1d | -3.52317 | -49.23041 | 2024-10-30 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02d44404-ed53-3f1f-98f1-5e0b71d87d19 | -3.52263 | -49.23394 | 2024-10-30 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fee4401a-7284-3425-97ab-2d557738d477 | -3.51478 | -50.47355 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f552962d-b0dd-3bea-a328-64375eff376a | -3.51423 | -50.477 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 540bb766-0562-30f0-abf5-dca4157cea51 | -3.51146 | -50.47303 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17cab05d-cda6-3509-9434-ce0e0476ad4c | -3.51091 | -50.47648 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47ce3485-b4d5-3f4f-b254-b0c8afb8016a | -3.51037 | -50.28554 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 153584ce-c481-31b9-8427-47567a79b340 | -3.50928 | -50.29243 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc1398f-7322-37d7-9b1c-6bc649720bbd | -3.50814 | -50.47251 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bada53e4-211e-3385-a3c0-5ef6745b799a | -3.50596 | -50.29192 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29f58f6b-db7a-33a1-9e7e-feef076ca08d | -2.97269 | -49.10202 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ce8219d-1e1c-3f31-807b-6978a4d6fe24 | -2.97214 | -49.10555 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc05b9ee-d8d2-319c-83a4-93cf289722d4 | -2.96879 | -49.10503 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8664a39f-2f60-3b1a-9219-a516f7b56f94 | -2.88539 | -49.24332 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d71efc4-54a2-3c12-a8de-f2443edc803c | -2.8787 | -49.24229 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5293f901-ae3c-321e-bbd1-504e52c77fec | -2.86921 | -49.23722 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6c4196b-1c15-3bf0-9f4e-9db885e50397 | -2.86532 | -49.24022 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a54315a-0dc9-3fc1-83d4-b8a8f3f85828 | -2.86198 | -49.23969 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71df7bad-c7c6-3992-82a2-b2cd15b4531a | -2.84189 | -49.24389 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| abd07e08-9a16-3907-b114-536f6eea9c4d | -2.83854 | -49.24337 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 367c70be-57bd-3b81-9e22-9da1c57f81c1 | -2.83575 | -49.23935 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0678f59f-2d40-3394-8070-4292114521bd | -2.83186 | -49.24233 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ed5f0fcd-ccc5-3590-b8f1-8bfab89a75a5 | -2.83016 | -49.23131 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b337fe34-7d7c-3156-9eec-9c9663be9cdf | -2.82682 | -49.23079 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 08c4fc23-6977-30d5-9804-fd662b65ffa6 | -2.82627 | -49.23429 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62fa703b-9cc8-3b46-b9d1-2c10d735949e | -2.82572 | -49.2378 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbff8e3a-54dc-3197-8fbd-d161a7985f01 | -2.82237 | -49.23728 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fd42ea0-eec6-3d6a-8372-3ffdcc49c463 | -2.81734 | -49.22573 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 612fbca7-efef-3cb7-95ef-754edbeca91a | -2.8084 | -49.21717 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4a41ce8a-b9b3-32b7-a7ea-9557726d9b92 | -2.8073 | -49.22418 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71e3f900-e56d-3828-b965-59a2b04ea413 | -2.80007 | -49.22665 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 122411b6-403c-3901-84d3-b1e436145e2e | -2.79672 | -49.22613 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d339b6fb-8d26-36a3-9b0b-28a965942817 | -2.70867 | -49.05446 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d652e43-a5c4-3352-9789-fc8d039bd736 | -2.70532 | -49.05394 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d0495a2-a84f-3368-b8f6-36cd3933d31c | -2.70197 | -49.05342 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b16204dc-a678-366f-9ccf-2c6159120d46 | -2.59194 | -49.19481 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b7e30c4-4929-382b-b449-99c84e93f3a1 | -2.58258 | -49.23278 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27ba9294-ac6f-39fa-b8a9-c1ea2fd974c7 | -2.56757 | -49.24119 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 782d1b80-1ed0-38e9-95b5-6a26d533b19a | -2.52704 | -49.09462 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49ac32d4-b7c1-332d-930b-779d2d195618 | -2.52424 | -49.09059 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5be8862-25e0-322f-8bd8-83b7c11776e8 | -2.51755 | -49.08956 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3539284-d434-3c53-91d6-92adc326c248 | -2.517 | -49.09307 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ff63240-bc09-3ff2-a1b4-04c203f81732 | -2.51217 | -49.18926 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89738c47-ddbb-39dd-beca-544d1fc6ec4a | -2.49775 | -49.21568 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac83380c-a320-3643-8992-18a484c131a1 | -2.45809 | -49.16296 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b232c506-1220-349d-a5e6-e3e07bdb4476 | -2.45774 | -48.91074 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d68d7fc-4e91-3916-9798-1ee3584745f9 | -2.45475 | -49.16244 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c499307a-2476-3135-9cf7-5471f578b4d0 | -2.38788 | -49.1808 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b3f76e2-f2b2-37e9-8203-b228b12c6bb5 | -2.38786 | -48.93974 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08ee251c-bec1-3bdb-8712-5f5bc95d84e1 | -2.38731 | -48.94328 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7260c46e-dc15-3779-aebf-cb78130a12c9 | -2.36425 | -49.09106 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afef0e55-ba58-3dd0-b218-2684f603c029 | -2.36146 | -49.08703 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c32d0340-bb1a-3e4d-a864-e919147959e3 | -2.35811 | -49.08652 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9edaafd2-ee99-328d-be7e-3c7565cc961b | -2.70697 | -49.28418 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ef5963-9bbd-3527-8558-9aef67cad113 | -2.6709 | -49.31792 | 2024-10-30 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d1d7b20-4fb7-3c1b-bb6f-cbc37b356369 | -2.65998 | -49.83798 | 2024-10-30 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a9b9d89-5e23-3ea4-850e-a75b7c4469c3 | -2.65572 | -49.26192 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a6752fb-d773-3a5b-bd1d-0b798f4a0811 | -2.64386 | -49.38157 | 2024-10-30 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 995b97d7-3ea0-38ac-8859-27ffbb6faa54 | -2.63242 | -49.08966 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cccf059c-ecfb-348b-b30d-4299f5cffc2d | -2.62206 | -50.07927 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b065b7-2077-311b-93fd-f39c533c353a | -2.60377 | -50.02719 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84380766-cdb5-39f1-bb39-edd19313319d | -2.59474 | -49.19883 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 289480b7-5b24-3867-b7a8-eb2963f9f8f4 | -2.58871 | -49.23731 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8e19b2b-2841-36f4-a8c0-9ec2220198e3 | -2.58592 | -49.23329 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 694bf550-1382-3706-8233-bc5cc5daef2a | -2.58312 | -49.22928 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de4ab49c-3dbc-38bc-8bf0-8d177b371fef | -2.56423 | -49.24067 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86eff4ee-7a9d-3475-bfcb-ea1021c08795 | -2.56204 | -49.45085 | 2024-10-30 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42057d7e-9167-3cd4-a1aa-0cec1f76f910 | -2.55983 | -49.07122 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb1396e4-dd40-3673-8c60-2610303e23a2 | -2.55423 | -49.63065 | 2024-10-30 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d508425-7419-30aa-bf86-e006c4dabe56 | -2.54645 | -49.80989 | 2024-10-30 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dc44103-4a4b-37ab-975b-9679ecdeff75 | -2.52759 | -49.09111 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d89c0c0-d481-3802-bcd6-0bb32c3c965b | -2.5248 | -49.08708 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7a71a909-2499-3982-908b-964a215aabe4 | -2.52369 | -49.0941 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a9af6e5-f2b1-3b30-a3e8-9a795eb0631e | -2.52145 | -49.08656 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6eac95b5-efbb-3c2f-acff-2b4ce9fc5ea2 | -2.5209 | -49.09007 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4b3e8e8-da7c-3961-85ba-e5f73a08264d | -2.52034 | -49.09359 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README59.md)
