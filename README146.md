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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 394c4420-9c13-37ed-a798-053fe1b8e945 | -12.5866 | -54.7474 | 2025-10-04 12:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| deb8e6f2-b577-393b-975c-82499fb24d4d | -11.9335 | -46.3926 | 2025-10-04 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f2d3c7d3-7fd3-338b-836f-a479dfef3695 | -11.5069 | -46.7671 | 2025-10-04 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 281.0 |
| 103e85eb-fddd-36b9-856b-622961687806 | -12.0314 | -45.1901 | 2025-10-04 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| e74c4e23-303c-3d0b-8728-66e9b228f233 | -7.7494 | -46.272 | 2025-10-04 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f78b8573-293a-3c9f-aee8-ad9ce66a7daf | -13.1333 | -47.949 | 2025-10-04 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 78c54766-7ded-356a-9310-1a0e398c5388 | -9.3196 | -45.7515 | 2025-10-04 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b0df2f69-c8b4-3c1b-9b95-11f5d4a9ae1f | -13.114 | -47.9518 | 2025-10-04 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| bed0cc80-363e-301d-a5e6-ac3ea999fba7 | -7.7679 | -46.2927 | 2025-10-04 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 190152b6-9728-31b2-b2cd-c7e488e89bb4 | -8.2316 | -46.8066 | 2025-10-04 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8448d78d-c6f0-3969-b82a-129529ee98cd | -7.813 | -42.5349 | 2025-10-04 12:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 402f819f-d105-3d6b-b11d-f41a24259cb6 | -11.7962 | -48.9231 | 2025-10-04 12:50:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2b419ae4-7f92-37cf-b54e-e414279e8d3f | -13.0959 | -47.8876 | 2025-10-04 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 1a56de01-7cf5-32d9-af1a-53049c9f8035 | -8.9948 | -47.4845 | 2025-10-04 12:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| cbb47c51-6edf-33fc-83b1-ada7e93d1a63 | -11.5069 | -46.7671 | 2025-10-04 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 351.3 |
| 197c63e1-050c-3a12-8a4d-6ff39143ac5f | -9.1114 | -44.4029 | 2025-10-04 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4e288238-e21d-3d3b-b8b0-5d6db2e9c667 | -13.9383 | -48.1852 | 2025-10-04 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d5b3628b-5856-308c-bdbe-5ad10ecaf45c | -12.7194 | -48.5611 | 2025-10-04 12:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 0f1f5664-ba02-331c-8cd9-aea9a50ea713 | -8.834 | -46.7917 | 2025-10-04 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 058e3a2e-9397-3729-bfdb-2a41a4df1d44 | -13.3619 | -48.0713 | 2025-10-04 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 116.7 |
| e9c0c739-9db6-3c00-bc54-f017c49b75c3 | -8.8534 | -46.7451 | 2025-10-04 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6c5a160f-5252-3a50-87c7-15ba35c48109 | -15.958 | -43.318 | 2025-10-04 12:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 115.5 |
| c22af848-6215-3613-aeec-8b9a643baf17 | -8.8529 | -46.7897 | 2025-10-04 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 36931dd5-c4a2-322f-94e0-c4fead26be60 | -9.3379 | -45.7947 | 2025-10-04 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 3e57be5e-31a1-301d-8345-025b429b92a0 | -12.6512 | -46.9894 | 2025-10-04 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| ac9237d3-59a9-3589-92d8-aa1607656c23 | -12.0314 | -45.1901 | 2025-10-04 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| fbc8a6ed-ae2e-3dc2-8030-4eb84a60a544 | -12.0891 | -45.1814 | 2025-10-04 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| de918985-30ba-3297-b7e3-02a5a8998082 | -11.4877 | -46.7696 | 2025-10-04 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 227.5 |
| 2c742eca-731a-3dfa-afef-737af68aaa16 | -14.2131 | -46.0596 | 2025-10-04 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 437.7 |
| 21e2d33c-cf15-3cb7-99f1-8f0f846aaa87 | -13.2938 | -47.5905 | 2025-10-04 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 46ef054f-7697-36fd-9764-000824fdfd45 | -12.8761 | -47.2937 | 2025-10-04 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 215.6 |
| e2957343-52fc-36fe-b3e4-d90fe236af62 | -13.3127 | -47.61 | 2025-10-04 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 4fe83cea-3a50-3cfa-85f5-af5bd9f36391 | -7.7491 | -46.2944 | 2025-10-04 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| f37a2fd2-135a-32a5-b6fc-548725aa5245 | -14.2126 | -46.0827 | 2025-10-04 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 240.4 |
| 82c759ea-0469-3aeb-8ec3-f641a7f1f4c7 | -8.2314 | -46.8289 | 2025-10-04 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 7746e494-fc34-3736-bbfc-15df69b32638 | -9.3382 | -45.772 | 2025-10-04 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| f1aa5a78-25b2-304b-af41-1fdc60509d8d | -7.7303 | -46.2961 | 2025-10-04 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 793bb85c-b3b7-3179-bb7b-f764d636e548 | -8.8526 | -46.812 | 2025-10-04 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 260.2 |
| 3aaf1198-5844-3b24-8a4e-a7a472128202 | -12.031 | -45.2132 | 2025-10-04 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 135a1e59-4625-33b9-a519-236ca82d244b | -11.5072 | -46.7446 | 2025-10-04 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| cc0f9d0a-d9af-37c4-b209-ea3ebb96f95e | -7.5504 | -42.3965 | 2025-10-04 12:50:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 132.5 |
| d75ad5d6-0f13-3e81-85d1-34006ee9fcc2 | -13.3426 | -48.0742 | 2025-10-04 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 3dfab370-f7eb-3faf-ab70-18507b1b3dfe | -14.251 | -46.0991 | 2025-10-04 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 72a82c43-7513-3efc-a325-a6bd3a54d03c | -11.5683 | -47.6749 | 2025-10-04 12:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 6c9c3824-7b86-3e42-a129-bd996f7d5c10 | -11.8352 | -50.0891 | 2025-10-04 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 6b15cd87-de40-36c9-a4bb-f970c3aa0f6d | -9.9396 | -50.2304 | 2025-10-04 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 931b8d11-d6d5-30c9-9c62-88a86ffc4d5d | -7.878 | -48.2021 | 2025-10-04 12:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a8e02e7d-9381-3759-81c2-535337b7a637 | -12.5866 | -54.7474 | 2025-10-04 12:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 25ef1dc5-7716-37fe-90d9-1624285e56bf | -12.9471 | -50.9838 | 2025-10-04 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| f2254111-c1da-386e-9b24-ebd8e4b408d9 | -11.0126 | -46.6971 | 2025-10-04 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c0184cc0-07a1-3535-a04e-ab93fb9710b3 | -13.8283 | -43.1702 | 2025-10-04 12:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 124.6 |
| 28442ef2-fcc6-3a46-b66d-ade6ef9c89cc | -15.5408 | -46.8344 | 2025-10-04 12:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 71f9fb4e-1d04-3cfd-a3db-e25e8f637a1a | -7.7938 | -42.5607 | 2025-10-04 12:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 129.6 |
| 5591eef0-3f4b-3e44-857e-d5d92ca66d70 | -7.8593 | -48.2037 | 2025-10-04 12:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 63869ae5-4e10-3af1-9cf4-2f7c6faac449 | -12.3853 | -50.2595 | 2025-10-04 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6c170049-f7f8-34a2-9492-96a655675126 | -14.3904 | -45.9369 | 2025-10-04 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6a6994bb-e177-360b-a982-ae8b25dd3ced | -8.2128 | -46.8084 | 2025-10-04 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f59a7b68-39c1-3a55-af33-16c5e35afe82 | -13.332 | -47.6071 | 2025-10-04 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| dc50ba11-5c92-37a3-8e3e-6448bc8a73b7 | -14.5941 | -52.4976 | 2025-10-04 12:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| fd54756d-f06f-3e9a-8c43-1cf7630f4509 | -10.9314 | -47.021 | 2025-10-04 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 07290e09-0c6a-343b-af5e-2c83822f6347 | -15.3797 | -47.952 | 2025-10-04 12:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 6562f155-5437-305c-a138-0ea2b055fcc9 | -14.6716 | -48.3157 | 2025-10-04 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 57dfb8d0-fe6d-3ddc-8ebe-d46ee4e34f85 | -12.535 | -45.9864 | 2025-10-04 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| aa751a80-9218-34ca-9380-433b52db8e30 | -14.672 | -48.2933 | 2025-10-04 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| dd6df3ce-142a-3eda-95cc-81b0a5dd320b | -7.7489 | -46.3168 | 2025-10-04 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 37e6be7b-d56f-3e4b-ad6e-9204fd504b3b | -11.5492 | -47.6773 | 2025-10-04 12:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 5e44ce5c-6263-32b1-839b-fd58ddf5f206 | -14.3899 | -45.9601 | 2025-10-04 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 9f3f5b8e-2fb1-32c0-b343-75dd344d4ab5 | -8.1891 | -44.1357 | 2025-10-04 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 69235513-879e-396e-a97c-0be387ed5f96 | -7.7941 | -42.5369 | 2025-10-04 12:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 136.5 |
| 250d9543-e0c3-3e49-853e-536bf8d600b3 | -7.7301 | -46.3185 | 2025-10-04 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 38917603-7847-3cf3-9e10-288e629ae015 | -7.7933 | -44.1304 | 2025-10-04 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| c1c1d27e-e3b0-3d3c-ad81-9992d33db05b | -7.813 | -42.5349 | 2025-10-04 13:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 153.4 |
| a8f0bb66-05b2-32e9-b789-a6a019c61156 | -9.9393 | -50.2518 | 2025-10-04 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| b594aa6a-edae-3ac4-9f6b-ebac78a5fb6d | -8.8529 | -46.7897 | 2025-10-04 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 09ae212b-1707-3aa1-bc6c-cbb40045ab70 | -8.8526 | -46.812 | 2025-10-04 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 5c15d1a8-1573-320e-8441-0a1c4a810fbc | -9.9584 | -50.2286 | 2025-10-04 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| ed93d07b-7790-3011-8f53-baa23953c11b | -13.1144 | -47.9295 | 2025-10-04 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a8e00d81-4256-3054-87ac-226bb3db8299 | -14.6716 | -48.3157 | 2025-10-04 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 272.8 |
| c8ea2db0-15e9-33e1-9dd5-e65533346216 | -13.7473 | -51.3097 | 2025-10-04 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| aa4a8c66-4745-342a-a840-f1fb24bbcd74 | -7.8593 | -48.2037 | 2025-10-04 13:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 4b6e154b-10eb-349e-989b-7fa6e8560a8e | -7.5316 | -42.3985 | 2025-10-04 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| 49dc5d23-bc47-3ad5-b11e-9e2ea7f82a66 | -12.0895 | -45.1583 | 2025-10-04 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 779b477c-3e94-3312-98ec-6b6225697bc0 | -12.0314 | -45.1901 | 2025-10-04 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| cfc27f5a-c1e1-3a97-8cd0-ce67a63ddc84 | -13.3426 | -48.0742 | 2025-10-04 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 0f91a333-558e-32ec-b299-442e3a10604f | -7.878 | -48.2021 | 2025-10-04 13:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 86faf2ac-d573-3bf2-a158-d51c6ea0713d | -10.5838 | -48.696 | 2025-10-04 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 13c0de26-4de1-3865-957c-6f89d262874c | -8.2316 | -46.8066 | 2025-10-04 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5cdae112-eadc-3a9c-a8a5-6467288af811 | -13.3127 | -47.61 | 2025-10-04 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 3d660b71-64b6-3dcc-9f33-6a70f19cfb88 | -7.7566 | -42.5172 | 2025-10-04 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 020d108a-e05b-37f9-b948-6480a02e0e2a | -13.114 | -47.9518 | 2025-10-04 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 538ca2bc-b00e-35f7-83c7-5bbf38d67a66 | -7.7489 | -46.3168 | 2025-10-04 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 16e14c49-88e2-3988-b4c2-27ed3c84aa98 | -11.7924 | -46.8184 | 2025-10-04 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 3f87c9b9-71e2-35be-b23b-72e3edf4d486 | -12.3158 | -45.3776 | 2025-10-04 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| b465524f-b55e-32ad-8c6a-95dcaf4d7693 | -14.2131 | -46.0596 | 2025-10-04 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 401.0 |
| 82f49f9f-e21c-313e-9495-bcd8e7aad10f | -13.3619 | -48.0713 | 2025-10-04 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 21c199cd-f4a4-38bf-a63e-1e190f05ac06 | -13.1333 | -47.949 | 2025-10-04 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6d1dc45f-f312-39e0-8439-3bedd7bfe20f | -14.5941 | -52.4976 | 2025-10-04 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| fed7deec-a326-3c48-be1d-159be507d5b9 | -15.5408 | -46.8344 | 2025-10-04 13:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 119.2 |
| b035cfeb-65a1-3741-9a37-00a784aacabb | -12.535 | -45.9864 | 2025-10-04 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 8ba2f957-e506-3561-97c1-0f715404a762 | -11.1458 | -47.9054 | 2025-10-04 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |


[Clique aqui para ver as próximas entradas](README147.md)
