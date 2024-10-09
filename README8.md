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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baf4e4fb-6bae-3012-9881-0f5b1bef8347 | -21.6322 | -47.712101 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c496b906-4bab-3e87-8c98-a690376c391f | -21.6127 | -47.663399 | 2024-10-09 00:37:20 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e02e14da-3778-3b25-99eb-fdb3ec6c5094 | -21.6147 | -47.673599 | 2024-10-09 00:37:20 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0a27d8aa-d627-308c-99dc-a6593e1aadcf | -21.6166 | -47.683701 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ab5ff3bb-e90b-3758-856d-394613561b1e | -21.618601 | -47.693901 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 185688c1-ade6-3498-8213-3d2036e189f5 | -21.6206 | -47.704102 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9323b663-006e-3332-9ead-a4e934916553 | -21.622499 | -47.714298 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 972aa92f-11e4-3586-b111-b3fe80942e10 | -20.6616 | -43.0811 | 2024-10-09 00:37:20 | METOP-C | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d06083c-d3d6-38e0-b292-a6f7c400116a | -21.645901 | -47.677399 | 2024-10-09 00:37:20 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 953b0cfc-7293-3864-8b75-ccd01252b15d | -21.6479 | -47.687599 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 46c6c14c-f089-3d1f-8d70-81d069fbb2bb | -21.6499 | -47.6978 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 159a620c-b06d-30c7-9666-948a9c46e858 | -21.6518 | -47.708 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0d9c7997-b4a9-32c4-8dc7-4f600dbab156 | -21.653799 | -47.718201 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b0a0f17b-6062-303a-b4f8-867e696b2702 | -21.634199 | -47.669399 | 2024-10-09 00:37:20 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bb766138-9dee-320f-895d-373ee7739ef5 | -21.6362 | -47.679501 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a44d5bda-d3e3-327f-9333-20d7cd5e7e46 | -21.6381 | -47.689701 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9d717d93-4601-3e14-912b-0c5a34f4a988 | -21.6401 | -47.699902 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a9598719-88e4-3b14-89a1-0860e4652025 | -21.603001 | -47.665501 | 2024-10-09 00:37:21 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5002d4d5-8860-3a27-944f-81421740f377 | -21.6049 | -47.675701 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b359986e-036f-33cc-a948-55828266925b | -21.606899 | -47.685799 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dd4c3fce-d8bc-3a1d-b0d5-ec88b442f103 | -21.608801 | -47.695999 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ba612332-0384-337d-9427-ae6abe0c3fcf | -21.6108 | -47.7062 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8bccfbb5-2d56-3a6d-a6d6-349d476d6ea8 | -21.6127 | -47.7164 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e326b9b6-ce20-3192-af22-0041bdb3d61c | -21.5951 | -47.677799 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f4716060-5b82-3134-892d-7e7028e626d8 | -21.597099 | -47.687901 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 64b5ab78-90dc-35a4-9c95-1395f8bd3d88 | -21.599001 | -47.698101 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d4a640b6-643f-310d-b519-3ee1d48658c1 | -21.601 | -47.708302 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9e8304c9-37e4-3963-8ab8-4393b69fc6a4 | -21.6029 | -47.718498 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c3e5e893-d23f-31d8-9278-67c7c8091c82 | -21.587299 | -47.689999 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 47877a4b-4d47-3ee8-8cdc-ca55c0e610ff | -21.589199 | -47.700199 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e226b708-9e35-334a-8422-bfe63996c659 | -21.5912 | -47.7103 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 834cf317-d6cf-364e-bd37-76e5aac4c52e | -21.5931 | -47.720501 | 2024-10-09 00:37:21 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0423675f-27b0-34df-a6a8-fa02f8990c6a | -21.831499 | -49.152901 | 2024-10-09 00:37:21 | METOP-C | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 416d848a-acdd-3ff1-b7dd-c4b1ee565291 | -21.833799 | -49.165401 | 2024-10-09 00:37:21 | METOP-C | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5745d8e1-4541-3130-aabb-ec0615e09567 | -21.5818 | -47.873001 | 2024-10-09 00:37:22 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dc957006-46fd-33eb-aaf5-b008c6c4de85 | -21.57 | -47.8647 | 2024-10-09 00:37:22 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 02b82f97-5ca0-31a8-a566-093dc5135ae8 | -21.572001 | -47.875099 | 2024-10-09 00:37:22 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5aff288a-cb7d-3dff-a73a-4dcd5c925656 | -21.573999 | -47.885502 | 2024-10-09 00:37:22 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9f709094-0d74-3273-b7d1-d5d325ec49f7 | -21.576 | -47.895901 | 2024-10-09 00:37:22 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8ee68faa-aa82-3686-ad6b-39a848fafc6e | -21.577999 | -47.9063 | 2024-10-09 00:37:22 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ef71b5e5-7c1e-3b84-aa6d-8bfded273dc3 | -21.564199 | -47.8876 | 2024-10-09 00:37:22 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5dd880ae-cf97-39ac-b686-6b98a17c1da8 | -21.5662 | -47.897999 | 2024-10-09 00:37:22 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a31e154f-e4a1-3005-a706-4e8ec1721e4d | -21.568199 | -47.908401 | 2024-10-09 00:37:22 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c8b1f925-5bd2-376c-bf35-d7531b0210e9 | -20.2892 | -41.847698 | 2024-10-09 00:37:22 | METOP-C | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e64a2613-c7d6-387b-80da-d562c21547eb | -20.290899 | -41.8554 | 2024-10-09 00:37:22 | METOP-C | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6102f4a-b88b-3e63-9970-e6e04e772526 | -21.8195 | -49.142399 | 2024-10-09 00:37:22 | METOP-C | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f0f3a55-8f5d-322b-afe5-0cb8e2d42481 | -21.8218 | -49.1549 | 2024-10-09 00:37:22 | METOP-C | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a764089b-8693-389c-a5aa-88ebe6850f5f | -21.8241 | -49.167301 | 2024-10-09 00:37:22 | METOP-C | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92a47c0f-c06b-3108-b13b-0091c00cff53 | -20.715099 | -43.8386 | 2024-10-09 00:37:22 | METOP-C | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f77501e-c25f-3616-8891-e223f7365922 | -20.5555 | -43.3461 | 2024-10-09 00:37:23 | METOP-C | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 59a9ca02-8564-39d9-ac93-b21c8cbbaa4d | -20.5571 | -43.353401 | 2024-10-09 00:37:23 | METOP-C | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1fa26ff-3254-35bc-b857-225e64d47400 | -21.004601 | -46.088001 | 2024-10-09 00:37:25 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d15176b-3e7d-35a0-82ba-185b2c610e7d | -21.0063 | -46.096401 | 2024-10-09 00:37:25 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8d5d21c-0f95-3456-961d-a50190eca6fe | -21.009701 | -46.113201 | 2024-10-09 00:37:25 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3503eb9b-989f-3114-9c74-474baa044df9 | -20.994801 | -46.090199 | 2024-10-09 00:37:25 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1ad2c50-da7e-31a0-bb0b-b5474faf6003 | -20.9965 | -46.098598 | 2024-10-09 00:37:25 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1aba4ab6-d0d1-3452-a1fe-55611a3ed801 | -20.434799 | -43.921902 | 2024-10-09 00:37:27 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2dd7dbb3-7d92-3604-a230-a02bfd503dd2 | -20.436399 | -43.929199 | 2024-10-09 00:37:27 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ffb88363-6183-39b5-ad55-72a2e6a186fc | -20.426701 | -43.931599 | 2024-10-09 00:37:27 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f71ae08e-9185-3820-9dc6-77813475583c | -20.428301 | -43.9389 | 2024-10-09 00:37:27 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9541e3a0-f1d5-3aea-a400-48778a7966a8 | -20.416901 | -43.933998 | 2024-10-09 00:37:27 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e867b98-f83b-3f3d-ad91-62690f49977f | -20.6866 | -44.999298 | 2024-10-09 00:37:27 | METOP-C | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b87123b-2b08-3525-b388-4691fabd0a6c | -21.107401 | -47.212898 | 2024-10-09 00:37:27 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5df7219c-aeae-3010-96af-d363152538ef | -21.109301 | -47.222301 | 2024-10-09 00:37:27 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bb0fa2cc-1779-395a-9dde-7ca73d35f87a | -21.1112 | -47.2318 | 2024-10-09 00:37:27 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 123c14c8-dba7-3604-89d3-8d4d404be469 | -21.113001 | -47.241299 | 2024-10-09 00:37:27 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6c0f0e46-5f31-3776-85d8-b7ede57597db | -21.099501 | -47.224499 | 2024-10-09 00:37:27 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e118aeb1-9004-3aca-af53-aa7f96822c71 | -21.1014 | -47.233898 | 2024-10-09 00:37:27 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b4d421cb-261d-3999-a884-856d5f0b1b8c | -19.993601 | -42.179401 | 2024-10-09 00:37:28 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c6c888a-c848-3a89-bf89-1dc358e796e8 | -19.9953 | -42.186901 | 2024-10-09 00:37:28 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38199bec-cc58-3d56-8351-7ec7a2b6d871 | -20.399099 | -43.899601 | 2024-10-09 00:37:28 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c6ffe16-5cd5-396b-9a6e-8934e8179fce | -20.4007 | -43.907001 | 2024-10-09 00:37:28 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf513772-3459-3356-a2fe-cdb9b2c50b65 | -21.086 | -47.207699 | 2024-10-09 00:37:28 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 442b305c-e72a-3341-9180-825f77e4dda5 | -21.087799 | -47.217098 | 2024-10-09 00:37:28 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 82585cec-1865-38ad-88b1-0881d318f29a | -21.0762 | -47.2099 | 2024-10-09 00:37:28 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 62292a2e-0b53-3316-9118-1fc56d9ecd06 | -21.0781 | -47.219299 | 2024-10-09 00:37:28 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c2c2f78b-cbe8-34c5-8257-05bc4976902d | -20.0091 | -42.4282 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b916076f-0c20-374d-918b-1a06c8c9cb1b | -20.010799 | -42.4356 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 43ad26ec-b1b2-37f4-8ef8-3ac8635beb0e | -20.012501 | -42.4431 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8215c5f-6b84-333d-95ee-955797e6d988 | -19.9977 | -42.423199 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04ca1503-2959-36a8-baab-dd0779a5a58f | -19.9993 | -42.430698 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 91db6296-f235-3aaa-bad5-4c17ee73907c | -20.000999 | -42.438099 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cba7d2c1-ea05-39d5-873b-4561c81823a3 | -20.002701 | -42.445499 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3d8482ff-0567-3477-bbe8-fffff8721b9a | -19.988001 | -42.425701 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 17e5eeb2-f91d-3cc2-95a6-bb63140b7915 | -19.989599 | -42.433201 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc7967e3-d928-320a-8b1b-cec594b0c39d | -19.9765 | -42.4207 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bed9c8b8-9cb5-3227-8fa7-6cbfc65f8779 | -19.978201 | -42.428101 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 015656fa-4a73-3be8-a540-b0df105e2c7f | -19.979799 | -42.4356 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e9bfb74-f639-3e00-b672-a7495a6fb4a0 | -19.981501 | -42.443001 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09bf7252-f212-3ec8-b53d-aee3028f8c17 | -19.968399 | -42.430599 | 2024-10-09 00:37:29 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5bcb50f8-b11c-31ac-ae36-c9a353a24ab7 | -21.073799 | -47.561401 | 2024-10-09 00:37:29 | METOP-C | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4120ebfa-f37c-3323-8569-357fd410b066 | -21.075701 | -47.571201 | 2024-10-09 00:37:29 | METOP-C | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 093d4201-7aac-387c-a686-cb574220a672 | -20.9832 | -47.152 | 2024-10-09 00:37:29 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 932177a6-9ba3-3a06-aa0a-5aa3e556b484 | -20.9851 | -47.161301 | 2024-10-09 00:37:29 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f5124cda-8dc3-304b-bc16-5cacd87d3438 | -20.2866 | -43.949902 | 2024-10-09 00:37:30 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03ccdb2d-e992-32da-a323-2ac783de84aa | -20.275299 | -43.945 | 2024-10-09 00:37:30 | METOP-C | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7beda56f-5d46-3ec5-8eeb-a569f00758f0 | -20.276899 | -43.952301 | 2024-10-09 00:37:30 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad8e2cc1-ba67-370f-87b1-97b4ae0a8028 | -20.2785 | -43.959599 | 2024-10-09 00:37:30 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f51a2d0a-051d-326a-9f9f-f18c021315a9 | -19.7533 | -41.675999 | 2024-10-09 00:37:30 | METOP-C | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| edc09f1f-bf6b-3da8-a6e7-d9c8996abe0a | -21.023001 | -47.562099 | 2024-10-09 00:37:30 | METOP-C | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
