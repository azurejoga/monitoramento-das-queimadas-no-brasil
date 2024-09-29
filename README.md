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
| abb6fb11-0cab-39c9-87b9-5635ee6e75a3 | -7.84 | -44.62 | 2024-09-29 00:04:42 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 878d4832-7b2b-3647-b60a-e2395e38205e | -7.84 | -44.57 | 2024-09-29 00:04:42 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d6767b31-d608-371a-ad7e-c51b29e61a5c | -3.94 | -41.49 | 2024-09-29 00:05:05 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8a5c4dd7-4a9e-3e5f-8f26-2100f536c0ac | -22.783899 | -46.796799 | 2024-09-29 00:44:05 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fbcb1fce-3786-3c23-ab7a-70f1430a6625 | -22.785601 | -46.804901 | 2024-09-29 00:44:05 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff49ab9d-5de9-3a50-9291-dbbae996be99 | -22.772499 | -46.7911 | 2024-09-29 00:44:05 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5a13ad40-aaeb-3c0c-aa85-b33d5f9d0708 | -22.774099 | -46.799099 | 2024-09-29 00:44:05 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d3aa719-8ef7-308d-abe1-11979f6eb437 | -22.775801 | -46.807201 | 2024-09-29 00:44:05 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95d5b6f0-64b9-387a-91c9-518b49845cc2 | -23.373501 | -50.215599 | 2024-09-29 00:44:06 | METOP-C | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a13711d-721b-3829-83aa-63208613b4d2 | -23.3757 | -50.227501 | 2024-09-29 00:44:06 | METOP-C | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5687460f-b3d5-3f5c-bc82-ae6288f5c3ad | -22.374399 | -48.736401 | 2024-09-29 00:44:18 | METOP-C | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e94b3f2-c75b-3c54-8184-bd385cd1e23b | -22.376301 | -48.745998 | 2024-09-29 00:44:18 | METOP-C | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd75a485-4e5e-38bc-b544-504e0f4906a6 | -22.2857 | -48.6469 | 2024-09-29 00:44:19 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d66f7ea2-29b3-30e3-9078-53335d2aa779 | -22.295401 | -48.644798 | 2024-09-29 00:44:19 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 392c95d9-b831-35fd-8e07-42d3f97f6db4 | -22.297199 | -48.654202 | 2024-09-29 00:44:19 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99c7b650-52d6-3f43-bc6c-90513dc21f74 | -22.2875 | -48.6563 | 2024-09-29 00:44:19 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3c88a8a-789f-3c90-83dc-6b2b47150f62 | -22.2894 | -48.665798 | 2024-09-29 00:44:19 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0dc4011-a539-3213-93ac-72e4c9b1a869 | -22.2759 | -48.649101 | 2024-09-29 00:44:19 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39aa20da-bf41-3bf4-ab9b-ba0ec13b9226 | -22.2777 | -48.658501 | 2024-09-29 00:44:19 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 607e4871-96f3-3e04-8e3e-7772d7acb907 | -22.2796 | -48.667999 | 2024-09-29 00:44:19 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 08b837da-33a5-3fd7-ac08-5f458dc1ec1d | -22.2679 | -48.660599 | 2024-09-29 00:44:20 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b319ec42-471f-32ab-93e0-0640d62ce9b7 | -21.7073 | -46.3521 | 2024-09-29 00:44:21 | METOP-C | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eccc6443-acf7-3d6d-a634-28ab172d3b15 | -21.709 | -46.359699 | 2024-09-29 00:44:21 | METOP-C | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6645f1f-f20e-3c33-8d93-2276ecffd82d | -21.628 | -47.752499 | 2024-09-29 00:44:27 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 146f637f-c60d-3c23-ab57-294d946e47be | -21.616501 | -47.7463 | 2024-09-29 00:44:27 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0c4736f4-984d-3f77-8d1d-f996a880b1cb | -21.606701 | -47.7486 | 2024-09-29 00:44:27 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 37c7e979-e721-348b-b2bc-13058a24bb77 | -21.610201 | -47.765499 | 2024-09-29 00:44:27 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 978e1d85-f3c7-3caf-afb9-864fb5dac763 | -21.6119 | -47.773899 | 2024-09-29 00:44:27 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0e55cf53-d1cc-3b4b-bbd3-6230cfc51677 | -21.6136 | -47.782398 | 2024-09-29 00:44:27 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ececd55-5dec-362b-b8f6-a08fcd766be9 | -21.595301 | -47.742401 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e7a2bf84-36ac-3e50-98aa-85e768ace2d0 | -21.597 | -47.750801 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c1fe2f66-e421-3fec-8c9a-220f273ed731 | -21.5987 | -47.759201 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3ead950e-fd2c-359f-a52b-3ebacf5417e6 | -21.600401 | -47.7677 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a7a615d5-c8d4-3c2b-beec-e9ac9b83e475 | -21.6022 | -47.7761 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a5676e61-dd78-3f5e-9104-6035cf816c84 | -21.603901 | -47.784599 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 87f098ed-8cfd-331d-b8a8-2b89b11e3a68 | -21.5872 | -47.752998 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ceb825f4-4108-364a-9982-d24e01763f45 | -21.5889 | -47.761398 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b52de401-414f-37eb-8535-f42e45cf1e4b | -21.590599 | -47.769901 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 61edca6a-4b31-3819-98bb-9cc1dac0a740 | -21.5924 | -47.778301 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2472dd6c-4441-349e-81f6-6ca83250e4dd | -21.594101 | -47.7868 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 963d9d74-b707-3b28-99a3-7d5098b3d25d | -21.5774 | -47.755199 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d3d90eea-b365-352c-8621-8c09915bc088 | -21.579201 | -47.763599 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5528d6ff-29d7-3a33-908a-027dd6696d7e | -21.5809 | -47.772099 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 02ae3fa0-e0ae-3b29-98ec-75ad682279a8 | -21.5826 | -47.780499 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9b05ef71-2dc3-3b34-82cf-db2f6f16c532 | -21.584299 | -47.789001 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9af229ba-fdb7-3e6a-9ebe-615e0b64a353 | -21.5676 | -47.757401 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9e760a98-f76a-3f82-9437-1fc2cc1bf268 | -21.569401 | -47.7659 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9298bac6-ba9f-3474-8442-cc0505a140f2 | -21.5711 | -47.7743 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c527fdf2-da9f-3e8f-bfe0-07979dccb2fa | -21.5728 | -47.7827 | 2024-09-29 00:44:28 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| eab9850b-dbd6-3723-beef-bb2c5c661989 | -21.130301 | -47.024101 | 2024-09-29 00:44:33 | METOP-C | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7cd2e700-14f3-3e35-8ae4-93c95850d94e | -21.131901 | -47.031898 | 2024-09-29 00:44:33 | METOP-C | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f7427fe2-a0ef-3919-a297-3551dc056512 | -20.6397 | -46.256599 | 2024-09-29 00:44:38 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b60081e-7665-369a-8219-22cd6471f81d | -20.6413 | -46.264099 | 2024-09-29 00:44:38 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 25296a2b-a1bb-35a2-96b5-c2ada3b45c71 | -20.6429 | -46.271599 | 2024-09-29 00:44:38 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8efa621f-639b-31ec-90d0-b1917dd78f5a | -20.644501 | -46.278999 | 2024-09-29 00:44:38 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9c2d9113-ae3c-3ecf-8ad1-3a26cc6f812e | -20.6315 | -46.266399 | 2024-09-29 00:44:38 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4f331a77-9a03-3e3b-b423-1ac454e6752d | -20.633101 | -46.273899 | 2024-09-29 00:44:38 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 61a905a6-0d16-379b-a16b-81a2b2997cef | -20.634701 | -46.2813 | 2024-09-29 00:44:38 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07abc318-4beb-3460-9d19-f5febe76e257 | -21.153999 | -48.905201 | 2024-09-29 00:44:39 | METOP-C | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ec23a3d-2a33-3ea8-a218-0bb4bc65f534 | -19.1984 | -41.341999 | 2024-09-29 00:44:43 | METOP-C | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d01a34a-fbd8-35e7-aed8-d45a7f2ea077 | -19.4266 | -42.497101 | 2024-09-29 00:44:44 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed8e7707-16fd-3d82-912e-30f51d3ea532 | -19.4286 | -42.505501 | 2024-09-29 00:44:44 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e76d9f3-1eed-30b7-8849-03ac3bd91e46 | -19.430599 | -42.513901 | 2024-09-29 00:44:44 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fae84f50-9059-3407-9e18-c68d22587a9e | -18.944201 | -42.0844 | 2024-09-29 00:44:50 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f20896e1-cdb7-3b55-801b-90d48f6cb52c | -18.946301 | -42.0933 | 2024-09-29 00:44:50 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef9dc9e3-020d-341f-abe8-9ae09f3a4e81 | -18.934401 | -42.087002 | 2024-09-29 00:44:50 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2148ed60-b27e-373d-a96d-9a61fa161003 | -18.9366 | -42.095901 | 2024-09-29 00:44:50 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a113f984-33fd-3cc3-953f-1e48845f370a | -18.9387 | -42.104698 | 2024-09-29 00:44:50 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ebe2280c-d5a2-3440-8f8a-001ed8050ce2 | -19.049 | -42.954899 | 2024-09-29 00:44:52 | METOP-C | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e09c87cd-6b69-364f-ad80-f5bc9ca164d1 | -18.808901 | -41.911201 | 2024-09-29 00:44:52 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 76ffff7e-a482-3225-8972-b7a39d01957d | -18.8111 | -41.9202 | 2024-09-29 00:44:52 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d646d8f-432f-3d75-8611-8d3a80ca2209 | -18.797001 | -41.904701 | 2024-09-29 00:44:52 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a9e70d5-24ff-31c3-9a89-a4b2afe7979c | -18.7992 | -41.913799 | 2024-09-29 00:44:52 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 883d8160-1fc8-3ab5-9f7d-d19549a5c3b5 | -18.7873 | -41.907398 | 2024-09-29 00:44:52 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b45ced6d-78cb-3026-b4d6-2b0e29669011 | -18.789499 | -41.916401 | 2024-09-29 00:44:52 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d43703a8-7281-33b1-b45d-735ec6e468e3 | -18.7798 | -41.918999 | 2024-09-29 00:44:52 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b72c879-5dfe-3390-a6c4-c2a30aef8235 | -18.7819 | -41.928001 | 2024-09-29 00:44:52 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3bd8dcaa-5166-3a6c-a909-34ca9ce69618 | -18.5103 | -42.2178 | 2024-09-29 00:44:58 | METOP-C | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1c805d7-fae6-3d66-8e4f-3404689af7c9 | -18.5124 | -42.226601 | 2024-09-29 00:44:58 | METOP-C | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c06bba33-0df7-3592-959e-d60520b18a9f | -18.500601 | -42.220402 | 2024-09-29 00:44:58 | METOP-C | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 478d3d6e-64e8-3d5d-813a-f59f745b3fee | -18.502701 | -42.229099 | 2024-09-29 00:44:58 | METOP-C | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 927a524c-c53d-39be-92fa-e4132fa8dd12 | -18.287701 | -42.154099 | 2024-09-29 00:45:01 | METOP-C | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 819d00f4-8232-3158-8114-a02debadd1f4 | -18.2899 | -42.162998 | 2024-09-29 00:45:01 | METOP-C | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30d78182-4af3-3a10-97e1-a842621a327e | -18.348801 | -42.751999 | 2024-09-29 00:45:02 | METOP-C | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 06c0736d-7371-3d61-a21f-36ff0e8fa0b7 | -18.3508 | -42.7603 | 2024-09-29 00:45:02 | METOP-C | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e721018a-1b86-3f51-9a5b-3486d9d4c4d8 | -18.3999 | -43.360001 | 2024-09-29 00:45:04 | METOP-C | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 17b7d296-a4e1-37e6-881b-6aa1ff07f6a6 | -18.1042 | -42.6814 | 2024-09-29 00:45:06 | METOP-C | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 131322fe-9499-3f3c-ab74-10c6d3f36bcc | -17.9814 | -42.300499 | 2024-09-29 00:45:06 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e1e0d8e-c340-3a03-9154-6ed22979d9f6 | -18.0488 | -44.381401 | 2024-09-29 00:45:13 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3cee0dc0-cf1c-332d-aa93-7477b307ae5e | -18.050501 | -44.388901 | 2024-09-29 00:45:13 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 34ba897c-6299-3a89-91cb-4ab8c0ef7197 | -17.7833 | -43.289001 | 2024-09-29 00:45:13 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b342ce33-163b-35c7-aaf5-02b01247622d | -17.7871 | -43.305099 | 2024-09-29 00:45:13 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b7c6d8db-6ffd-3f0c-86ae-d620bee7a086 | -17.7754 | -43.299599 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 85209e73-26eb-3250-9b95-30590e9ca9e6 | -17.765699 | -43.302101 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fd8bff6e-cadb-38cf-b5c2-a6fa13d2b69e | -17.767599 | -43.310101 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc1e099e-6f86-3dcf-bb52-16c8c5245889 | -17.769501 | -43.3181 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7f58774-dc1c-3c6f-bcdf-a73c18390234 | -17.7714 | -43.326199 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d91533af-e2d5-3294-98e3-2b093ae91966 | -17.773199 | -43.334202 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 655f76f7-6e6d-3a09-b728-059659e889fe | -17.775101 | -43.342201 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 928aa924-6549-3221-8cfc-08f011c482f5 | -17.755899 | -43.3046 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
