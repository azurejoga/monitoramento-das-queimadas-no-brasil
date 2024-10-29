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
| a6182328-ba7e-3309-a210-314e51aad0a2 | -4.93117 | -45.43429 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc0b9367-32ee-3d8f-9a07-ff9b5f93a499 | -4.92814 | -45.42929 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8bab1605-7936-3258-99a6-c26211196e5e | -4.90777 | -45.7607 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59dc5ca7-b427-340a-ad67-4adba97883b8 | -4.85865 | -45.76652 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1255701-c417-3a6a-a648-7025c4a23a22 | -4.70067 | -45.88629 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3d119ab-d1a4-317e-ba66-10b601984d20 | -4.68265 | -45.81187 | 2024-10-29 04:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e61c5897-204b-310d-a6a4-e3b39b772ce9 | -4.83643 | -44.90666 | 2024-10-29 04:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c58c204-06fe-318f-90a1-54757350b30c | -4.71729 | -45.88684 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3981cb6b-6edb-386c-820c-cebcc25a05ca | -4.69707 | -45.88579 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40ed586f-cd0f-3021-900d-c8154efe6cce | -6.39821 | -46.28683 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea8f99a5-a287-31bd-95b2-f0b956f40452 | -5.30634 | -46.30354 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cf758f1-a078-3593-a553-b7996cdf9a8f | -5.30574 | -46.30753 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9721b83b-c9d9-37dd-a05d-abe136326009 | -5.2915 | -46.32998 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7976d312-9872-3169-aee6-1a28051baa87 | -5.29091 | -46.33391 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5b410ce-8367-3295-a132-a1922f5ef3a0 | -5.28976 | -46.31734 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f1f28a1-a46f-3d70-a599-f5892349b60a | -5.28622 | -46.31679 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5365da6b-45e1-3e94-be53-b24afcc1afcf | -5.28608 | -46.31816 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d496ec34-ada0-38a2-a38d-b1fec25139a8 | -5.26693 | -46.2539 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 549b596e-f7c3-35ef-aafb-58a873f6e1ed | -5.25103 | -46.2389 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bb51450-fce5-3b70-9b85-3112e355d2d1 | -5.21678 | -46.06369 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebb900cc-0f10-3dfd-b5ed-56154e4db956 | -5.21318 | -46.06322 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4631494-b7fd-36c0-bf82-73104f3dfdeb | -5.16862 | -46.11491 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3577588-b6e1-3eb8-9a40-f079bb401229 | -5.16305 | -46.05522 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1e6be80-5afa-32e0-b809-01786b109454 | -5.10374 | -46.11485 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 915df878-828f-3787-81ff-80861906e120 | -6.38574 | -46.44398 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f57c69f-65ed-3fab-a574-f809adf88138 | -5.44163 | -45.89497 | 2024-10-29 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e818a8a-8d91-38a8-90ae-8eac60adee03 | -5.2921 | -46.32597 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7c6f660-48df-3cec-ad48-761bc9e8ce79 | -5.29086 | -46.31074 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d93028f8-f784-3f60-a7a4-7e7da4d963e5 | -5.29036 | -46.31334 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ffd34ef-4152-3b34-a832-6ba843e74652 | -5.29025 | -46.31472 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83e1be25-99e1-3c7c-961a-94f58376877f | -5.26755 | -46.24985 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d891bc3-e2d1-314e-a87d-c4e44a8080e4 | -5.21546 | -46.06271 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d214a57f-7fe2-34d7-aa34-4aa55b2ce0d0 | -5.21383 | -46.05904 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81eab66a-e249-342b-9384-c14eb403d72d | -5.21213 | -45.85359 | 2024-10-29 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da9eba83-46f9-3d05-a012-38038b3e6f60 | -5.18287 | -46.21234 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7635f356-83d9-38fd-95e1-41976d31bbd7 | -5.1697 | -46.13177 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfcc1f03-ea38-39d6-a6fe-f312344759d6 | -5.10309 | -46.11314 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84389906-ea8b-33ec-adae-abf0135ccb54 | -5.10207 | -45.95912 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7552868-22a9-34ea-a6ef-0ebb6f0ebc8e | -5.07058 | -45.82585 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0f556ed-15d9-3a90-96f1-a1327720e4e5 | -5.99148 | -45.95225 | 2024-10-29 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b100ccd-3372-372a-b189-b8c4c9e53655 | -5.69589 | -45.34972 | 2024-10-29 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4060640a-b8ff-3cdc-94a2-e4300594bc71 | -5.69215 | -45.34915 | 2024-10-29 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 217eadb4-c38f-3f9d-b63d-3274e2aeb59e | -5.62604 | -45.27097 | 2024-10-29 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84856f51-dcb8-3ac3-a91e-f50f916fed70 | -5.44826 | -45.90012 | 2024-10-29 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5bf37549-b29d-32bc-a675-33cba4ed8894 | -5.41813 | -45.65551 | 2024-10-29 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 170660ed-914b-3b8f-8510-4a30451c2cb4 | -5.36601 | -45.65431 | 2024-10-29 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b259e4b-3268-375f-8ec1-c65ecf4e10cd | -5.36235 | -45.65372 | 2024-10-29 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11970e53-c0d4-3899-92bb-36ababfc36ea | -5.36188 | -45.88274 | 2024-10-29 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a65090e-3fb4-3a77-9afa-cb5bb370c99d | -5.31022 | -45.89816 | 2024-10-29 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c889c5e-99d4-3ada-aea6-87413ea8e82a | -5.30659 | -45.89769 | 2024-10-29 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a1bc1c8-1ac3-3b4e-8391-5b7238d139f2 | -5.29523 | -45.20464 | 2024-10-29 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4addff8d-62dd-30bd-9e1d-639c4906510e | -5.17162 | -45.30441 | 2024-10-29 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52dc81ea-8029-3d89-95dc-0a20a6119207 | -5.10503 | -45.96383 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82bd20bf-1eae-364e-8edf-0860a4dd9569 | -5.10143 | -45.96326 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0e30b1e-bff4-3bb3-bd19-f6dff71eeace | -7.91817 | -45.43457 | 2024-10-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14717c9b-ec21-350b-b221-33b2ea9e3920 | -7.91685 | -45.43205 | 2024-10-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0684c13-24a0-3a62-a84a-cec1bdbc7ccb | -7.8927 | -45.42098 | 2024-10-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4df8c98-eb01-3d8c-880d-4dfad30fd036 | -7.80208 | -45.58673 | 2024-10-29 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 737dd6b9-b341-3282-8877-7aa6d1385535 | -7.606 | -46.87614 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3987320e-59a1-37e5-99b0-bac2c150fba5 | -7.60186 | -46.87963 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39429d00-354c-3461-956c-b629da56c823 | -7.59168 | -46.85078 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbbdb7d4-8f73-3d6a-8efa-f1b8e37c452d | -7.39207 | -45.69027 | 2024-10-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26015e8b-5b8d-389a-93f3-bff9dd471672 | -7.32345 | -46.1778 | 2024-10-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b911c65f-ea00-309d-bf99-52dfcbc54140 | -7.25678 | -46.07279 | 2024-10-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5df1f80-d590-3119-95dd-0b5575ea3c0f | -7.25614 | -46.07708 | 2024-10-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 430e8e90-1f53-340d-911a-168a5c4d3bb6 | -7.21862 | -45.52757 | 2024-10-29 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92713986-b6ca-39b6-bfac-d3ecacd2bd2d | -7.17755 | -46.32822 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84b527a8-0d71-3991-852f-e16cd2381e3d | -7.17395 | -46.32754 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bdb09c6-59f5-3026-8645-f57784cce534 | -7.12636 | -45.39241 | 2024-10-29 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ca1878b-a5e4-300c-a48c-bee95063a706 | -7.04957 | -45.51907 | 2024-10-29 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3da1ba24-f2d9-31ae-ab6c-e577af2449fd | -6.95195 | -46.1103 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0857d69-50c8-32ac-b0f2-eeac5095b1a7 | -6.94891 | -46.10558 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a2d59a2-6c08-3752-8658-9737013fd9f4 | -6.94805 | -46.31279 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e73f0b7-7060-39f7-9175-6a6c4a92002b | -7.72512 | -45.71525 | 2024-10-29 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b9bc09a-7364-3361-adbc-07ba019e090e | -7.57209 | -46.44512 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8942fd8a-8062-361d-8c3f-e4b3c39742c0 | -7.57147 | -46.44933 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f59c77fb-751b-355d-b0fa-9ed688f6cb81 | -7.39515 | -45.69542 | 2024-10-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c2a4ff7-957d-394f-b028-cc7d5a0c5c63 | -7.39275 | -45.68567 | 2024-10-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb79847e-e09e-371a-896b-a9062d6fa636 | -6.95205 | -46.10785 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 047a7726-7b24-380e-aa44-23e9b161d9a9 | -6.94905 | -46.10309 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af3163f5-7e4a-32df-a543-93bb0bcf57e0 | -6.94839 | -46.10736 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a60a8026-490f-36a7-8eb9-6f8328cca769 | -6.94829 | -46.10984 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14de3f87-0e5d-34e0-b78a-254714c76c57 | -6.94775 | -46.11161 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc7d51a7-0375-31f1-8d35-776b7e48a441 | -6.87341 | -45.91092 | 2024-10-29 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5bdc118-5610-3382-a7fc-1faf5ff60c49 | -6.87295 | -45.90929 | 2024-10-29 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c73a7f8-aad1-35b9-b4ef-49dd3906e432 | -6.81903 | -46.14536 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6df4bd01-31b9-3783-88c7-4cd0daddad73 | -6.78906 | -46.0221 | 2024-10-29 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b442860-70db-3cee-b662-be4b05c0f546 | -6.66322 | -46.38375 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40557c34-ea08-3939-9d8b-644ad3269e19 | -7.61014 | -46.87266 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66cdf540-2190-3f50-8bec-f2bda6ff7dbd | -7.6066 | -46.87212 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cbd73c3-632b-38d5-9a2d-7d480befa355 | -8.23329 | -45.84068 | 2024-10-29 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bd31db0-0731-38d4-8632-8b5f9e8de8af | -8.2326 | -45.84543 | 2024-10-29 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b260ef1f-6b95-378b-a78f-b461a9ae35d6 | -9.74201 | -46.27465 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5aa4058-ba5b-3b1c-8b21-14e81fa39388 | -9.74049 | -46.27693 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb2d5193-d217-304c-ae68-8f194602202a | -9.70574 | -46.25293 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8de8696b-5eed-3545-8cf5-5fa75e82b175 | -9.70508 | -46.2575 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfb0494f-d575-30f3-a0f2-fa4883acc6aa | -9.70401 | -46.23858 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0f7b1a1-15b1-320d-ba28-2c5bc5064fbe | -9.70333 | -46.24321 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 58713b14-8d78-3bf6-a421-a1660f542d11 | -9.702 | -46.25236 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4dc5be78-d12f-368a-8ec3-a6f984fab2ba | -9.69959 | -46.2426 | 2024-10-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README59.md)
