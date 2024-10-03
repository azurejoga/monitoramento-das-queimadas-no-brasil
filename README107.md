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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79769f8d-3ef4-38e3-acfb-72a795182b5e | -16.74675 | -57.47393 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e74f8cdb-be28-3e2a-8ec2-e71cfdb6b067 | -16.74611 | -57.477 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 7bd47c03-894f-324e-91fa-8f578836cda0 | -16.74548 | -57.48006 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| abc4d97f-2d98-3940-9492-3d0818dd3345 | -16.74485 | -57.48314 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 55eeda39-c083-3a6b-aaa4-4d356b180da0 | -16.74422 | -57.48621 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a061e6c9-617d-3762-aaac-2d0c663e90be | -16.74359 | -57.48927 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a4cd86d3-c5e5-3cdf-96fb-2e88d4a79dd9 | -16.74338 | -57.47196 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4429f220-a54b-3302-a660-a6f58f8154a6 | -16.74277 | -57.47503 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a4f9c5fb-841b-34f2-9511-ef969f86c92a | -16.74216 | -57.4781 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 4b16dff0-28f3-360a-badc-3370d4e3b324 | -16.73712 | -57.47702 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| c0326686-6db0-3ab8-9195-4402254f6781 | -16.69175 | -57.4673 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7e904f66-0c0c-3015-b035-bc4b13caa00c | -16.69112 | -57.47039 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 244250fd-e853-367c-81f6-51cde54661de | -16.81818 | -57.56326 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| bbe886f6-41be-3e64-abf4-4bf880ae7dd8 | -16.81755 | -57.56638 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| af6a4f0a-42e3-3a27-9105-7c9c6647b007 | -16.81249 | -57.56528 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2f030f06-d474-341a-a080-434881e81416 | -16.81187 | -57.5684 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0e9297f7-def1-39ac-b3f6-8ec7a693e45f | -16.76684 | -57.7392 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 04a08e94-eb19-3fd7-88ba-572ece10a8eb | -16.76618 | -57.74247 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| cb19db4a-b259-35a3-a740-d615d308e2ae | -16.76552 | -57.74573 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f61cfa73-6d1f-365c-b432-410f2078ee51 | -16.76487 | -57.74894 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 44cd2343-a5b9-3202-b9a8-4b8dc47854fa | -16.77626 | -57.43241 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4845c9c3-4017-3d8e-ace3-1837f85675e0 | -16.77564 | -57.43546 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 05851375-56ff-314e-9b36-d5946a4a0c7f | -16.77502 | -57.4385 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 0971611b-4106-36f2-ab7e-2d5ae196115a | -16.7744 | -57.44155 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| fe54d4d1-658a-37c6-bee1-905e471f4302 | -16.77378 | -57.44458 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ac3502ee-ae4d-3674-befb-013797ae0c18 | -16.77253 | -57.4507 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f445e43d-db3e-3435-beae-28d133f7ba56 | -16.77187 | -57.42829 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a8385009-0d61-39b7-99d1-e324295cd864 | -16.77124 | -57.43134 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3c41499b-236e-3b10-bb0f-6a2241bbbbc3 | -16.76875 | -57.44352 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| be131b21-1d97-3599-90d8-d5da78f3ca5f | -16.76813 | -57.44656 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| fb18423d-96c7-3a64-9808-ba9989f67705 | -16.7675 | -57.44962 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 422461a1-e1f5-35bf-89d6-034d59607fa3 | -16.76687 | -57.45267 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 5c71492d-e441-3f0e-9db5-9914922f9e79 | -16.76497 | -57.43636 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3f39c0e7-1aa5-33cb-9c40-e893f8b63202 | -16.76394 | -57.44764 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 501dbe76-68e8-37da-a91b-df6963c81281 | -16.76333 | -57.4507 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 4de3d76f-b66d-3e8d-9e96-746edca9c978 | -16.76247 | -57.44856 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 8c382f00-375b-3f65-9732-110b820dca7f | -16.76185 | -57.4516 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 59a65e82-4132-36a4-8577-f01fb2129f3b | -16.76132 | -57.43435 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 00c30109-4770-39b2-93b9-4819a4451bfd | -16.76072 | -57.43739 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| d9d8ee37-71e7-3f9c-8fed-3985267f1145 | -16.76057 | -57.43224 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d363407d-1785-32f4-af5f-c4634239ec73 | -16.75995 | -57.43529 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 62ae9308-0682-3382-959d-232dd53e01fb | -16.75891 | -57.44656 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| d2605329-0372-3994-ab3e-c7fba69769e8 | -16.75807 | -57.44443 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 19c5f795-6e3b-309c-afe7-ed26e6f8abb9 | -16.75744 | -57.44748 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b5133883-6f6f-31cd-9e37-9d0404552049 | -16.75388 | -57.44549 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ec56b011-3d13-3fb4-8bcd-727c213a7a3c | -16.75267 | -57.45159 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1662a5da-be1d-3073-ac9b-6e73c264750a | -16.75178 | -57.44947 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9d6e92f9-a5ec-3d8a-a4d5-cbbb2b59ba3d | -16.75116 | -57.45251 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0c9793bd-b912-3994-964f-634735793476 | -16.74885 | -57.44439 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e4e340b1-fe17-3104-9e28-960dcecfc1dc | -16.74824 | -57.44745 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| dd8974dd-aca3-36c5-9a5b-5c1539a86c4e | -16.74763 | -57.45051 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 40e8a5c0-8012-3e99-9eb4-59a07502ba23 | -16.74321 | -57.44637 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| c45a391c-c28e-3888-9f4a-8daeb3c6541c | -16.74261 | -57.44942 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| c3d0de3b-c3d1-3ca4-94e9-d97d2614f908 | -16.72751 | -57.44619 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b6f43814-df01-3642-be0f-924415a83808 | -16.7269 | -57.44924 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a7ca319c-ac19-343e-9c15-d87d38bd2709 | -16.71867 | -57.43792 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 76574061-0867-3516-a262-e5f784dd4460 | -16.71364 | -57.43685 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d2f85371-aad7-36d1-b167-0a7f21415fb7 | -16.82722 | -57.46558 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8eea0bd6-1be3-33be-9117-c4ec1e7b0fb9 | -16.82219 | -57.46451 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dd2c6d6a-75ca-37f9-9703-d0edb8fba823 | -16.7719 | -57.45375 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 7a5964b8-5158-32fa-8249-ac0472dd3866 | -16.77128 | -57.4568 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3b49a9f7-df9c-3c4d-937a-188d30f37e35 | -16.76625 | -57.45572 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| c86d537a-a671-3f53-a604-1151e03d6a12 | -16.76562 | -57.45878 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 5fdaf78a-5018-3655-92c8-51f4512d46f8 | -16.765 | -57.46184 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 9890e936-0822-3696-8283-f49f5adc6fd7 | -16.76273 | -57.45375 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| ece7e03e-d3d3-37d3-afe4-65f0837e1a5a | -16.76213 | -57.45681 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 0606fece-87f6-33a7-8b3d-9a6df0ef84c6 | -16.76152 | -57.45987 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c71814ba-dadf-3d22-9285-f8caa00b0c2d | -16.76122 | -57.45465 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| e331212c-41ea-39cb-865f-5431916aa8d8 | -16.76092 | -57.46294 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 7562e4e8-dc65-3bfb-bdd3-3a842437f72a | -16.7606 | -57.45771 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| bf5aad23-b079-3f7f-94a8-1d0514079989 | -16.75997 | -57.46076 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 67f9498f-a592-384d-b307-52165a55de2b | -16.75934 | -57.46382 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 65b7179e-860a-314e-9070-781476a68bea | -16.75649 | -57.4588 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c9b924fb-512d-3591-8859-39f397de757e | -16.75588 | -57.46186 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 1d41478e-7dc3-39c8-90e9-2c5eca2b88a1 | -16.75556 | -57.45665 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 01e4a0d2-c976-320d-9ff9-ebbb411a4bee | -16.75493 | -57.45971 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e406545e-73b8-38c6-b741-063668daed7a | -16.7543 | -57.46276 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f1f36b53-5609-338b-842c-75a925e8244e | -16.75367 | -57.46582 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 581b4dcb-3f4a-33d6-8341-840237664a46 | -16.75206 | -57.45465 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f4643437-04e0-32a8-b4ed-7236b340891b | -16.75145 | -57.45772 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 944de2ae-30e7-3e44-ab45-041e2feeff17 | -16.75085 | -57.46078 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e493b241-9058-3060-b891-a4264c3502f6 | -16.75053 | -57.45557 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b2dbb1da-042f-3577-870b-3d231fbd9c9f | -16.7499 | -57.45863 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1d7170de-7c6d-3df4-8685-09ba417cae9c | -16.74927 | -57.46169 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 788f4b46-fe82-31dd-ac67-268a5c93aee5 | -16.74864 | -57.46474 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f99669e8-dad1-310d-9282-b20bc3c3a1cb | -16.72506 | -57.45844 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| fcaed709-1fe8-353b-a5d4-14db79fd4e46 | -16.72445 | -57.4615 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7ae65b5c-804b-339b-8c95-e920568ca0c3 | -16.72384 | -57.46457 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f568672a-4a1f-356d-9b45-401c0970180f | -19.1089 | -57.48412 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 28134616-f84c-347b-add2-1fed61040658 | -19.10691 | -57.49396 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5a4da970-44d4-3299-a7a6-36372956bd6b | -19.10312 | -57.48784 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ad1ac232-b894-3714-ad64-3aea82c6cd1e | -18.69811 | -57.3064 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e34d2693-1b03-3062-9aae-6b48eede9349 | -18.69698 | -57.31197 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 73f48ccd-8de1-338c-a2cc-c7e79021a993 | -18.69586 | -57.31753 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b4bef049-94af-318d-8aa8-14a399eefe19 | -18.69331 | -57.30534 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 23f569e5-c5ad-3ad0-87bb-1a249f17efff | -18.69218 | -57.31092 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6ebb4502-2c2c-3ec5-bfa5-602bc40a6776 | -18.69105 | -57.31648 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e952f897-576d-3d81-a02f-3a6cee9af40f | -18.90751 | -57.71006 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e56b879f-87a8-3a2a-b3c8-e8ab26dd2547 | -16.60339 | -58.21643 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 211afcfa-6777-3e3b-b22d-82f8406a6eaa | -16.59995 | -58.21529 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |


[Clique aqui para ver as próximas entradas](README108.md)
