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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b73e1fd-2c9b-3567-a2ae-7a929ce2bef4 | -11.39347 | -54.04495 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c9013df-2dc2-3f2f-919f-cd367252f553 | -13.18985 | -48.53823 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa32b95f-7acc-3fef-9658-f6a2dd4c8244 | -12.0174 | -50.98703 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c7a82c6-bb17-31e7-8120-eb89c5243f7a | -9.96522 | -50.13404 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b944978-f973-3a67-9310-718221c36ecf | -12.06314 | -46.49902 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e7d3bc09-ce6e-3294-ad85-59203ec92543 | -11.98833 | -50.93888 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b9d1b580-aec7-3005-a1cd-9b7d64990214 | -7.47215 | -45.80713 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea6efcfa-6e5d-3876-816f-77d4e182048a | -12.15436 | -50.40376 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dac403fd-529c-3937-b610-9249c83768f1 | -9.79264 | -48.20194 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa7aed02-df2f-39d0-b604-e184cb15dc8d | -9.14071 | -49.97697 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f82ab4f-3d4b-35ca-b1fc-2f4d6f1fb9e2 | -10.81467 | -48.74306 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1008babf-f172-3c18-8af9-ead48a7ba9f3 | -11.40681 | -43.42113 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49c3f568-84aa-3f82-9167-8fb2fc30ce27 | -13.32901 | -46.8143 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88d825af-f9ce-39a6-b893-487e73a36092 | -6.31621 | -52.63108 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9eaac17-6984-35b6-ae6a-4818a8b4eef0 | -13.11035 | -47.40441 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3521f4a5-f4ad-3c44-bc32-d45e6008265c | -12.04235 | -46.4932 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05f1903d-88e6-312c-ade7-60b3aad4e3f3 | -12.04195 | -50.94033 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 809d02c9-715f-3359-88fb-8410795b966d | -6.72257 | -45.61735 | 2026-09-29 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fea3896-1c4e-393f-8f28-72ab03b75d4e | -12.06339 | -46.4696 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33a6d0c0-b105-3f7d-b317-1f790228115a | -11.98387 | -50.94534 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ae61d10-f372-3270-8104-7354816abdc4 | -13.17764 | -48.54799 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88246501-acc3-3f4d-bf0b-db080f76c3c8 | -11.43677 | -43.44519 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d6ecb94-f53b-337f-9984-54413bca3252 | -11.39585 | -47.4427 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 754a63c9-5cbe-3d90-9516-9ad97815230d | -11.65539 | -47.59434 | 2026-09-29 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c691299-015e-3b97-b171-0a17cec2237c | -12.76312 | -47.29647 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 65a9fc60-486f-33ea-8f33-60efa6ee4e23 | -7.46839 | -45.80653 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1484b40-10e3-3e68-8be0-a2177551945d | -5.72106 | -53.46432 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c3cdd41-b217-360e-9e4c-ea10eb433b58 | -12.91086 | -52.07122 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcae06a9-e7de-3b27-b579-209f506dca97 | -11.38096 | -54.05178 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c2bbf06-3963-324a-bd72-ab06061dc351 | -12.71871 | -46.99573 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e2c7eb9-37e7-311e-bfbf-b15c2e014f88 | -12.78983 | -54.02195 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79a86e81-8b46-36f5-8e13-7b55989e27df | -6.67364 | -55.11629 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ffe2072e-3fc0-3e4b-8f64-e23a2f148c35 | -7.39871 | -40.22108 | 2026-09-29 04:51:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| fb6088e8-7902-360b-97cb-e72ad238ed7f | -6.31762 | -52.62265 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 25fe541d-43e1-31aa-8e26-c9806667bdac | -12.02361 | -50.94813 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95e95b95-dcd6-3b7e-9d3b-2365a80f7479 | -7.69235 | -48.86277 | 2026-09-29 04:51:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 288eb069-ce7e-34bc-9e1d-bd71513b70a9 | -11.38904 | -54.03812 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7268dfd9-adcc-33b9-8d32-27132b81bbf7 | -10.40724 | -53.82046 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 924bbbe3-8ce7-32cd-aca6-d29954c28732 | -13.33666 | -46.81553 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d67ab7f-48af-3890-b4c9-e0c801c08b71 | -9.20279 | -45.84694 | 2026-09-29 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f56957f8-9e59-33d3-89c2-26d8015af1f9 | -11.39557 | -43.43459 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e7908b2-e517-3567-b5dc-d6f18de91b3c | -13.14148 | -48.55017 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 919445f2-c073-3549-a9c6-cfbd9984f3e7 | -12.77337 | -44.15224 | 2026-09-29 04:51:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00d8514f-e319-3f3a-a50b-5fcf324eac1a | -10.8158 | -48.71302 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a0be7ec-3d2c-3862-9868-c2891db8c61b | -10.80613 | -48.73042 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9efbdd4d-97ad-3c58-8db5-7a2a24614c00 | -11.18837 | -44.82347 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1996efcd-0fad-3820-820e-229c24cbf3a0 | -8.68722 | -38.1965 | 2026-09-29 04:51:00 | NPP-375D | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1c70a51-6f09-3587-9efa-3c5639457345 | -10.42715 | -53.83735 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb6f87ee-dd62-379d-b3a7-e70c2a5e006c | -11.38673 | -43.3933 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d99edfb-5365-3c46-8379-9b4ae74100bc | -12.01197 | -50.93539 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9600bbbe-972d-3967-b68e-0e10b3083a10 | -7.40417 | -40.22184 | 2026-09-29 04:51:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e4b957f7-7c71-3204-8fb1-909021ccf936 | -11.34705 | -54.05046 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d69e49c0-c49d-352e-88d0-835f2ad3528e | -11.36218 | -47.44543 | 2026-09-29 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61b5a9a6-a6c0-30b9-b29e-1851a1e69520 | -12.77515 | -47.11005 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e56601f5-c367-31b4-a02e-8a3cc932f911 | -12.02519 | -50.98105 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5771ba07-342e-3577-87df-780fcb18d717 | -11.40422 | -43.44078 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ab300b4-e1b3-32cb-950d-f0c5ca37bf44 | -8.00022 | -43.25635 | 2026-09-29 04:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7ed6eca4-4366-3b32-a1e2-5a541b12c6c9 | -10.51551 | -45.36629 | 2026-09-29 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b3911c3-9555-369e-8e5d-ae2d3837d2c1 | -11.41352 | -43.44202 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53ba56c9-21a2-3361-af84-332c7e2d7797 | -11.15857 | -50.0516 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05abb6b2-bb63-3ca0-b9b6-1e334f20a6a0 | -7.39823 | -40.22459 | 2026-09-29 04:51:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 1f12163d-6f01-3c9b-a8bf-82123d9942c2 | -11.99161 | -50.96113 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1452af10-0a28-3d85-b1b9-8a29263bf209 | -7.24351 | -43.36164 | 2026-09-29 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f342f82a-fbcf-37d0-bb8c-c4a078bcaa57 | -8.21562 | -45.45462 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 77d5a5e7-6645-3e8d-b677-9d3a607b0e6b | -12.14172 | -45.00021 | 2026-09-29 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02a76c4c-ef07-32f7-b560-e627975f35a7 | -8.24675 | -45.45881 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45c5b7a2-5f7e-3b9d-a02f-2ea0cfdc550e | -11.18363 | -45.13813 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 545fd641-fb22-3e23-a156-2e42305e52f3 | -10.81299 | -48.73129 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4d85d0f-4e73-3d4f-aa73-26cfb7476715 | -11.18782 | -44.82735 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8286af41-d7c5-37fc-a0e3-60550a63f6c7 | -6.68668 | -46.9903 | 2026-09-29 04:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1da69d3-185a-3eb6-857c-e4f32f04b1b9 | -9.96078 | -50.16209 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0862b56a-8229-3e6a-8ce0-3da5ab0ab38b | -11.36771 | -54.04042 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a014aad-b8ff-3421-875a-8d5310cc817a | -10.71689 | -44.42879 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e18d5051-8b32-36a8-b823-0471d6a697e7 | -10.81525 | -48.73932 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78f4bc78-063c-37ac-9f1f-cf9b6ebc33c7 | -11.97998 | -50.94833 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c422405-e7b5-38df-965e-33ad01cf7810 | -11.868 | -50.4625 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a83dfc54-0a65-36ec-b522-d373ba315f46 | -12.94165 | -46.65003 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a4e7765-9a01-390d-96e8-803f842b6aad | -8.23301 | -45.47131 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 688bd586-7e75-34a3-b8e0-3a36ab68d6af | -7.52143 | -46.6124 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d34f9d5-affe-3e56-87e7-ecac29b10154 | -11.54925 | -54.49625 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc89775a-f64b-3058-ac93-900cad1cf78c | -11.35518 | -54.04728 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02b03751-fbf0-32a3-a5c3-23db32498132 | -10.97084 | -49.67242 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23298fba-57b6-311b-acee-8858412fce94 | -12.06792 | -46.46529 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7804264-6aab-399e-885a-bc245ed0c507 | -11.62143 | -44.151 | 2026-09-29 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4994667-553e-3f73-926a-58cda5490fac | -8.63787 | -45.35176 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d181e075-3e81-3c08-a872-e6342ba8e9ab | -11.09845 | -47.11464 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b416e374-f877-3ac6-87a1-2cbf66079bf0 | -12.73539 | -47.27903 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40a4287a-6bc3-30c9-9d2e-43588bb890aa | -10.27029 | -44.63456 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c98593e-62e1-3a67-8b69-58d390b6b98c | -12.94235 | -46.6451 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04e9329d-3c5e-3552-8b70-b9f2448fb52b | -10.82497 | -48.72168 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e629fa0d-fad9-378f-876f-e19a967fdae0 | -11.12856 | -50.0685 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbc3afc9-ec49-3d58-8ce3-95d139a1e05c | -6.16328 | -52.90886 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5658682c-27ef-37e6-abf2-8cd1846b13ad | -12.02806 | -50.94167 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e27b54f1-7a2e-368e-b14e-5d9e8102669e | -13.45609 | -48.58473 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5ef878a-6eaf-398d-9143-d6fd484e0961 | -11.03456 | -54.13369 | 2026-09-29 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48a4da43-4699-3af1-830d-9fc057834075 | -12.95003 | -46.64635 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ae2db3d9-6415-365b-9eed-0abf79b2e501 | -6.67786 | -55.117 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ef9d89a2-e97b-3f83-a47f-38b0a65c4514 | -10.82098 | -48.72483 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80a5a29a-5f0e-3044-b894-72dde6387119 | -7.69138 | -44.92606 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5247c76-e06f-3b37-b6ca-e91df33ff1fe | -7.24729 | -43.36655 | 2026-09-29 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README42.md)
