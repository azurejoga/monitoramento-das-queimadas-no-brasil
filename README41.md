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
| f4bf3ab9-6bb4-331b-bf54-70d7e5d536b7 | -20.83883 | -46.361 | 2025-09-27 04:25:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ee63e4b-cdc9-3fcc-986f-11b16ea8c3ef | -15.01825 | -46.96782 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53d57228-67b7-3650-9749-1640c2384e67 | -15.2827 | -46.4311 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7612f365-c366-326c-8a38-60ae422a5bf9 | -15.04051 | -46.95683 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 294608e0-028d-30e9-a793-789847e7da73 | -14.06599 | -48.8268 | 2025-09-27 04:25:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b218e718-b266-380a-8696-17fac3c896d1 | -17.10976 | -46.86889 | 2025-09-27 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7028716-47c4-3442-89f3-f95c52e3baf5 | -13.60072 | -47.30644 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6db39ec2-3399-3abf-8b07-d3bb2326adec | -15.53663 | -44.33908 | 2025-09-27 04:25:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 315bb0c1-504b-3b79-ba7d-b7f605719c1a | -20.79062 | -49.39009 | 2025-09-27 04:25:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8298405-e3be-3ba5-979e-9c378a0af51b | -15.93543 | -57.49724 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 92abf35d-63cc-35a2-9a31-9f5bd0a4cd71 | -15.60051 | -46.45385 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9af0ddf-635a-3345-9b93-8b78eb9c0fbd | -15.2766 | -46.4264 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 602e0591-1063-3272-8a02-77c96a3a5e4a | -17.18775 | -44.79761 | 2025-09-27 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9a955b5-27df-334f-ae99-5c91b5bced73 | -15.14742 | -46.43114 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42a360b2-3916-33a7-92e5-06a6059fadae | -13.63241 | -48.07461 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16378e3f-c307-39dc-b3a2-659e0c09adff | -13.50909 | -47.41788 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c28f6512-b2d9-3a05-8088-82a2a3ff2ed8 | -20.65844 | -48.78517 | 2025-09-27 04:25:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b28ce96-b5b5-3b36-9eb1-8290dd190f44 | -13.67851 | -50.6386 | 2025-09-27 04:25:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f6d5ece-04dc-3f44-9744-e6c5bc666d46 | -16.81653 | -48.81441 | 2025-09-27 04:25:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15d98319-57fe-332e-a0d6-01ead34f3753 | -14.51664 | -48.01252 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1545793e-13a6-33da-9245-87174a49b09c | -15.93124 | -59.48865 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42c9f639-7033-3bc8-8479-d39817ab1252 | -13.50296 | -47.41313 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4dd0b6b-579c-3f9e-a781-d66b021ef222 | -15.01437 | -49.53722 | 2025-09-27 04:25:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1ef6668-22cb-32c9-a00d-322d7e2509f6 | -16.81717 | -48.81059 | 2025-09-27 04:25:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa241d6c-cd5e-3c17-a88f-0d8441f2737b | -14.5999 | -48.24947 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d4daa3a-5d5d-3e21-ae37-220cd42fe4c0 | -13.78661 | -46.93198 | 2025-09-27 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5e06e20-c587-3b03-94db-889e1c0e838f | -19.40588 | -44.30815 | 2025-09-27 04:25:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96729277-318b-3a40-83d2-cc421da0f40c | -15.2788 | -46.43414 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ed81562-d2ec-3962-9638-a0774ab9646e | -15.9111 | -59.33154 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 583cd33e-d52b-37f5-9b61-8b94e48a7bcb | -20.31925 | -47.13198 | 2025-09-27 04:25:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b64abe8-0b9d-3d16-8240-bfebcb2dba98 | -15.97205 | -50.87578 | 2025-09-27 04:25:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 444bb2ff-fd69-31fd-a8b9-34cd7130c8a5 | -15.45283 | -47.54629 | 2025-09-27 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b8fa951-dcb3-3db4-8b24-0e249314dd32 | -18.29227 | -57.09454 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cc6a7bd7-7f14-37d2-8fc4-65811faf8eec | -13.63584 | -48.0751 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 81ed6d08-969a-3a3e-aad6-a889c3b73aba | -15.41698 | -48.21086 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60d7d817-10d2-3db7-93c2-b81eafd017f6 | -15.02215 | -46.96479 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1b7c58b-6329-3be7-a629-79a2e4f3675b | -13.36955 | -47.82684 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea9518c3-be90-3f74-bb6a-73d7d898af36 | -14.02049 | -56.10379 | 2025-09-27 04:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17381557-d2b2-3846-b8c0-1b3199f5743f | -14.84356 | -45.62363 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59ae4d62-3b35-3de1-b41e-e35eaecddc14 | -20.43269 | -43.36866 | 2025-09-27 04:25:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| df1f16f5-261f-3008-834f-8e39ad622e7e | -18.25067 | -47.00698 | 2025-09-27 04:25:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a945688e-59d4-3bab-8f56-6cff970a2da8 | -15.04971 | -47.13517 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5e3f857-bad0-3f3b-b8e9-fce42fa3e488 | -15.55703 | -47.9119 | 2025-09-27 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4c8fb78-6977-3664-90b0-18cd2f71f5ca | -14.83908 | -45.60793 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4585136b-8958-3d8b-bb8d-b33a3c1b0f2f | -15.53019 | -44.33398 | 2025-09-27 04:25:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 24aee0af-baaa-32fa-a2b9-67d0436a5ad8 | -15.03776 | -46.95267 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 42d20c0e-cdc2-302d-a1d4-7c81a93ad808 | -15.27431 | -46.46281 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33126b97-19f8-35cb-b752-6fa262db7cec | -13.633 | -48.07495 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 814e4feb-f23d-317a-bbe5-3c35b84693ad | -15.01249 | -49.23203 | 2025-09-27 04:25:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad4878bb-52f3-386c-9357-e0bf51b68998 | -15.9683 | -50.87316 | 2025-09-27 04:25:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caac3aac-0ca5-3cf8-80a3-7ead69b7b44d | -14.83236 | -45.6293 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 26ce509a-c3fa-3640-8558-953d8673d4ab | -16.02053 | -44.39824 | 2025-09-27 04:25:00 | NPP-375D | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 897ff978-a6e0-33e7-adbd-ba9c19ccc937 | -15.26987 | -51.4684 | 2025-09-27 04:25:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5528aa66-ffb8-3fdc-9c50-c83cda3fa27e | -15.27323 | -46.44793 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 823296a6-88a4-3342-aa36-7eca59b82747 | -17.17865 | -56.38122 | 2025-09-27 04:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2ffc5483-e4de-317d-816e-dedb7d70d37d | -13.63179 | -48.07833 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4089ca36-e92f-32be-850d-404b83ed77be | -19.04921 | -48.1364 | 2025-09-27 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf1bb1ae-4220-3812-a296-338d9023900b | -18.22165 | -45.05326 | 2025-09-27 04:25:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 017291e6-3a98-385a-b5d3-817de0385976 | -15.90697 | -59.32743 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88cac63a-941d-3df9-a80c-a552a542172f | -15.41637 | -48.21458 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe5b5a22-9c42-3d50-9c69-49e18c99ae19 | -19.63633 | -45.5773 | 2025-09-27 04:25:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d27a2f24-5317-3219-a13a-7f59538b23b0 | -15.90481 | -59.32991 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abd2afa5-860c-3ec6-8700-0502dc1b1fef | -15.9015 | -57.48895 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb668cca-42e5-3efe-8a9d-6fb3ed1f57c0 | -14.43012 | -44.88124 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac41d996-6dd6-320d-9d4c-d9484605a293 | -15.45809 | -47.09646 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26a260e6-8e56-314a-92d1-efb29b4180fe | -13.60349 | -47.31061 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 038e4d7e-e613-342a-9409-345a4d7d76fb | -15.89257 | -46.19775 | 2025-09-27 04:25:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f4e05b5-89d9-3d90-8ce7-7a623c98e762 | -15.88923 | -46.19715 | 2025-09-27 04:25:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3dc266c3-38ce-365a-ace9-f631b67ec46c | -15.9683 | -50.87505 | 2025-09-27 04:25:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c68eb22-2fec-381c-a887-6ae020193053 | -20.31004 | -47.78056 | 2025-09-27 04:25:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0740113b-9652-331a-9f98-d53092fd580b | -15.42932 | -48.22051 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5928371-8084-325a-bf91-0f0749a35fee | -18.32497 | -57.12405 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 067a04bc-4106-3649-85b5-599703258e48 | -15.26595 | -51.46766 | 2025-09-27 04:25:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 533dbd6b-fca8-3091-acbe-44b65fe33bbb | -14.82788 | -45.63606 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f28c4ef2-2730-32d2-b295-737482e9784f | -13.61471 | -47.30511 | 2025-09-27 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a627af2-6e21-39c8-9d5f-97b99de6217e | -20.01993 | -47.62513 | 2025-09-27 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5399a0b2-708b-3353-9cd9-f002396dfd82 | -13.51755 | -47.40833 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00974f9b-3e99-3127-ba10-1a09345f3891 | -13.757 | -47.87004 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cf2c412-9aaa-3e06-8b7e-fac8a5558a95 | -15.20066 | -48.46281 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46c4fe16-f4eb-352f-9ae3-daf158e349a4 | -13.75982 | -47.87409 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e68f1675-0c1c-387c-9c95-5522b1d61af4 | -18.29154 | -57.09801 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 14321e59-2f7b-3731-b6d2-2cb9e788fc20 | -13.63113 | -48.08646 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4efba212-d50b-313e-8d91-c8c5109d553a | -19.92773 | -43.61716 | 2025-09-27 04:25:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 599eb99d-c3fc-3104-84f7-b8bd25bfa245 | -13.83007 | -47.95895 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19fe54c6-a2ce-3ab2-bcda-bee16884fce3 | -20.30268 | -46.66692 | 2025-09-27 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| affef0fa-ce50-3d9a-97d7-00d788bed831 | -19.93156 | -43.61773 | 2025-09-27 04:25:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 18cbf1a7-14a6-35c7-b19f-fceb93946f2e | -16.91303 | -45.95209 | 2025-09-27 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e719597-6175-3ba9-8693-2763958c1d0c | -15.89744 | -59.33317 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfdb444c-144c-3c4a-a0db-dfbf2eecaee3 | -15.96745 | -50.87792 | 2025-09-27 04:25:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba1dc838-cf42-3bca-a786-8c0392a47438 | -14.59308 | -48.24834 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5b8ad4f-180e-312f-b09d-f416fe2e20aa | -15.28485 | -49.48108 | 2025-09-27 04:25:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a85a09c-d479-3760-b594-ea54aee4a19e | -15.20154 | -56.02306 | 2025-09-27 04:25:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee7ba2d4-a4c7-3065-9523-7210fac86be1 | -19.71742 | -45.86926 | 2025-09-27 04:25:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72154693-11b9-3f48-8c09-b46059009849 | -17.73074 | -46.70737 | 2025-09-27 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a2b16b5-0f17-329f-b93e-924798306c25 | -14.06665 | -48.82289 | 2025-09-27 04:25:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 948164b5-831b-32e3-8ae8-818c73c8fc49 | -14.95059 | -47.49562 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 612e2082-9035-3207-99f5-780e574b59ca | -15.02996 | -46.95871 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35627a67-4c12-30d4-8f43-cb52c28b3e78 | -15.27379 | -46.44434 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b328751f-4667-38d3-bd06-3cddad84a465 | -15.03443 | -46.9521 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 62110e70-d710-3587-b55d-b8a257cba220 | -14.63396 | -48.29791 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README42.md)
