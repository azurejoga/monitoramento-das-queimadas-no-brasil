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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aecfe8d6-b0c8-3bb8-b8a5-6074dde52a17 | -12.81403 | -48.09463 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 47bcbb5b-7c29-3aab-acd8-be57eccea8b1 | -13.53419 | -46.95423 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 53512710-dfbf-3aab-9a36-a7454a56bc1d | -13.34666 | -46.8644 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4fb0c51d-cb52-3d25-be07-a76bced7b649 | -12.09448 | -44.72454 | 2025-08-31 00:28:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| c3fcce45-a351-3dab-80d1-62a67a96b585 | -12.31104 | -45.71364 | 2025-08-31 00:28:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| b23853f4-758b-3eb5-8911-dce2c9b72b17 | -14.84143 | -46.74547 | 2025-08-31 00:28:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e6c8e2a-6718-3323-aa38-7156140d40f4 | -13.30497 | -46.88913 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 25027f29-ba56-3bf2-b64f-49f9d43a566e | -12.10524 | -44.73314 | 2025-08-31 00:28:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a3741a0e-e352-39bb-99c2-1a66e5151c30 | -14.81279 | -46.74597 | 2025-08-31 00:28:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 13f14ad0-617a-3c09-a9b4-f94da4ab19f6 | -14.47737 | -52.02799 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1e6913f7-8e5d-3ff8-b0f2-6da2d3764573 | -11.84066 | -46.42501 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 59787bfb-ebeb-3f64-9e51-55180e192477 | -12.80497 | -48.09601 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 695c7370-08dd-3a2a-98a3-6dd7584a09b6 | -12.30972 | -45.7044 | 2025-08-31 00:28:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5db8daa8-474e-3631-9f6a-eefcb367483f | -11.35872 | -43.63002 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 4adc7aca-e060-3b62-af91-ffd3c5058c5f | -11.88207 | -46.7213 | 2025-08-31 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c84dbf43-b6ee-3223-a18e-3751f20890a0 | -13.34021 | -46.94868 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 476e6031-a74b-361a-bd48-0002626d7474 | -13.51802 | -46.83643 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a9609c5e-c0be-3f53-ad2f-2e63a5a9d5bd | -11.82571 | -46.52486 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 808a1980-c293-303e-9715-dc5dba99c31a | -13.329 | -46.86709 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bae8c5af-b18a-30d2-947e-3b5c6e7a16ee | -14.27289 | -51.89594 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ab974d3f-c18a-3fce-95c8-5d129c1c5a8c | -15.5006 | -41.9235 | 2025-08-31 00:28:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| e4e1d2d3-9d78-3253-b9b5-8972f0ca5f17 | -12.39995 | -46.47084 | 2025-08-31 00:28:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1048926f-0d53-399e-9358-c947facb61f3 | -14.81407 | -46.75525 | 2025-08-31 00:28:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e704486c-26d6-376c-86ba-9d41587524b5 | -16.08061 | -43.61356 | 2025-08-31 00:28:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2736e78d-a89b-33ef-b717-4fbbef7302b1 | -11.91363 | -46.68919 | 2025-08-31 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 57a65ec4-944e-3518-ab5b-4ac03c9866ec | -18.43785 | -47.23335 | 2025-08-31 00:28:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8879215e-37e4-34af-ab40-5aa8c6a72bae | -12.10941 | -45.78468 | 2025-08-31 00:28:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f3014201-6652-349e-93f1-a42861a950f3 | -13.68033 | -46.8742 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb4f7992-797f-3d67-ac0f-d727ae97d75e | -13.48866 | -46.9514 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 534d9222-d432-3786-8e59-eaaa2bbeabac | -13.67895 | -46.93013 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 45dc40fd-6486-3466-833b-e679afb64c24 | -16.41173 | -45.65369 | 2025-08-31 00:28:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 60019072-ec49-34bf-a520-8b749cacef28 | -14.27915 | -51.88875 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4c0f5748-de48-3bbf-85c9-b1d78da5c335 | -12.85033 | -48.0896 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6cd55f17-62c1-35da-bb24-57127edb8c30 | -11.89748 | -46.37972 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 35aedd84-0bf5-3839-9631-984a11f27e14 | -16.21288 | -52.66727 | 2025-08-31 00:28:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c4dcc4ac-7418-3670-be22-f0e7450b0c65 | -11.84191 | -46.43397 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fea99830-f43d-378b-a299-59052ccd1873 | -11.3387 | -43.63307 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| c4363209-6af6-3979-a361-3b68e2de8eea | -12.75834 | -44.41676 | 2025-08-31 00:28:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ef6f84a8-e8ac-39f6-b511-299898a4ed0f | -13.3503 | -46.95645 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c16ff11a-6515-3f3b-b98d-10957fc97cc9 | -14.13823 | -47.05639 | 2025-08-31 00:28:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7482f3f4-abd0-3032-897e-017cfd6c720c | -11.34692 | -43.61982 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 6c45e9d8-1c4f-322c-8b20-0e0205842eba | -18.60857 | -50.20809 | 2025-08-31 00:28:00 | TERRA_M-M | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 38.0 |
| 2ac3a7be-539f-33ac-b9ee-3b2d21a55846 | -11.92127 | -46.40664 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6b90bc8b-4484-3ef2-b8bf-5e1e8d89573b | -12.85941 | -48.08841 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d3b419cf-234a-3496-866f-de0efd227803 | -14.6232 | -48.06876 | 2025-08-31 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2f0fe225-ea8e-38ae-ac60-2717a88f2dfe | -11.90885 | -46.39642 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ba63a286-9948-3875-a7eb-989bf97fb141 | -13.57564 | -46.91465 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f24bf4ed-f024-3630-a640-0da0a28701ed | -17.96618 | -42.97984 | 2025-08-31 00:28:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| eb4c6359-54e4-35a8-a23f-5165d17277a9 | -16.22814 | -52.68639 | 2025-08-31 00:28:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 801205c4-6552-3f13-b806-53b29ab88e34 | -18.66061 | -49.09313 | 2025-08-31 00:28:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 7f529b9c-d8cd-3521-bff0-8b9235fa0dc5 | -18.51194 | -49.03537 | 2025-08-31 00:28:00 | TERRA_M-M | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a962dff3-6ed6-3d2c-96f0-af1de70f0813 | -11.9073 | -46.70841 | 2025-08-31 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dbf7369e-ad83-31f9-a36d-923079c649cd | -13.34906 | -46.94738 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 53062c4e-192d-31b8-98b1-b2d08b4e46f3 | -12.84908 | -48.08023 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b503c99-dfee-3227-8bbc-05ce86d066f7 | -18.05592 | -45.9507 | 2025-08-31 00:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 71856a7f-7736-369d-a746-b46ea9d686a7 | -11.90605 | -46.69945 | 2025-08-31 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a2c99323-bba8-3c59-9064-1f4541e810e0 | -12.80372 | -48.08656 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5b48b2a9-ef6f-3521-b63a-f5a64679c8ee | -14.03607 | -44.56646 | 2025-08-31 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3a1a1240-e982-344b-afcb-2cbebd396ca5 | -13.33287 | -43.20065 | 2025-08-31 00:28:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| bfa3ba90-e5ca-3a63-98d4-1791865d6faf | -13.02785 | -56.90889 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 226ab986-d145-3be4-a3b1-73447ccc0f1b | -12.63741 | -48.2202 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d6518f46-7412-31ad-8d70-72fa5d9bde3d | -11.36339 | -43.59315 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 3fb476b9-923d-3f5a-a199-83947a2a1c66 | -18.51038 | -49.02276 | 2025-08-31 00:28:00 | TERRA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| 8a9b1f50-4b56-3be0-8dc9-ff62204e7794 | -17.15228 | -46.07351 | 2025-08-31 00:28:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 365fe4b0-4ffe-3836-86b3-49e9798f952f | -11.88486 | -46.35411 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0674c7a4-907a-325d-8ae3-b2551ed6a872 | -14.47935 | -52.04559 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8d69e96c-f6e6-3038-bf3d-6f2eb810cf43 | -17.1624 | -46.08142 | 2025-08-31 00:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68738b53-d75d-3dc4-890a-e846643f9823 | -11.8318 | -46.42627 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| bb87c233-9850-3df4-9360-a309cbe66807 | -13.34394 | -46.97588 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 233d9c4e-f5f2-3d38-8772-b0ec8a228148 | -15.67239 | -43.22237 | 2025-08-31 00:28:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8341e027-32b9-3bff-a60a-68caf44e1230 | -12.75682 | -44.40654 | 2025-08-31 00:28:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2c8077e8-6c88-3712-9c22-67ac6080c08f | -11.89494 | -46.426 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fd057785-7a59-3374-a3b8-4ac8451c9784 | -13.53543 | -46.96329 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 88f84719-bd23-3ce2-acc3-ec292e5503ec | -13.69412 | -46.90908 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b071f321-b62f-3235-8318-fd86cebaf383 | -11.82074 | -46.42465 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2b1adfd0-522f-38f7-aefc-8725dbc4107a | -11.90378 | -46.42468 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1bd69bcb-7f94-393e-94c2-dd6990bad290 | -12.10044 | -45.79189 | 2025-08-31 00:28:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 487d9afa-78c2-3695-a371-2257cfa25f4f | -14.55271 | -51.99527 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0381fe7d-ba28-3a6d-9727-77e9f1b3ea39 | -14.55749 | -51.98248 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8ef1bf46-c4e4-3806-8160-b9a1c3f35ea5 | -14.63114 | -48.07168 | 2025-08-31 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 97bc6be4-5bc3-336b-979e-c5166d9bc600 | -14.03465 | -44.55662 | 2025-08-31 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f483f2a3-e391-3468-a36b-ba93f1965657 | -13.36797 | -46.95374 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d1c44745-fcbf-3ac8-8ddd-e53515789ceb | -12.40878 | -46.46954 | 2025-08-31 00:28:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d4049268-c9e9-3a34-881e-e939690cd1c6 | -11.82696 | -46.53384 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2de23c27-5f00-3812-befe-cac0d2272388 | -14.33851 | -51.88127 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 31ca3d57-7218-3474-a279-a1f5e7886328 | -14.83257 | -46.74675 | 2025-08-31 00:28:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 323be3a6-0b4d-3c70-8a87-ec86db45b252 | -11.89875 | -46.38875 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7a043b09-1ced-362b-abf6-33a8d4bf6dcb | -11.81567 | -46.45295 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c2f5e7e6-425d-3086-a700-6cba32c0e26a | -11.89622 | -46.3707 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e413347e-6e42-3021-923a-838d3fc99053 | -14.54548 | -51.98399 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 2da71237-f121-31db-8cdf-d2d605cde689 | -14.62984 | -48.06158 | 2025-08-31 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fd9409f2-7b67-34c3-8bdf-635a467e4a72 | -12.9892 | -44.85754 | 2025-08-31 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2edbe577-2ef1-3119-93bb-aeeca0b21abd | -11.33049 | -43.64632 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 134ce90b-9039-3787-96ad-3631ca89df75 | -13.48106 | -46.96185 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7557274b-187a-3b59-bb93-6883c87f38e5 | -11.91011 | -46.40538 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| d8ff539c-ccfa-33fe-8800-889d2d015177 | -18.1455 | -50.2508 | 2025-08-31 00:28:00 | TERRA_M-M | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1e2f4f4c-0c80-349f-9183-6876180d90e7 | -16.97832 | -49.31603 | 2025-08-31 00:28:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f18f379f-2d4d-3379-9836-e022c1399979 | -13.50917 | -46.8377 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 688d027e-9d68-3af2-bb10-d3aa07864fc2 | -16.22588 | -52.66555 | 2025-08-31 00:28:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| a3b5987b-bb72-3435-aa06-0093d273d05e | -12.82183 | -48.08374 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README4.md)
