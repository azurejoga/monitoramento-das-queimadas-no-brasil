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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06cc48ce-d8d9-3e08-af66-85076cdfb784 | -3.91764 | -42.41271 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 70e123b2-9b43-3d06-8d12-b746ae626814 | -3.91708 | -42.41631 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96f1066a-2b86-3904-b18b-6e9c8d219268 | -3.91484 | -42.40858 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d7a4ea66-8c0d-31c4-96c1-05739e478e08 | -3.51977 | -43.06079 | 2024-10-12 04:04:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f65936eb-d359-31cc-8415-6f58cc5de287 | -3.42532 | -43.34943 | 2024-10-12 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72fae21d-7d05-3dd9-9ef9-3e8e880af0e8 | -3.42181 | -43.34888 | 2024-10-12 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9815e479-ee7a-35b1-b657-d16eb37a55a3 | -3.41831 | -43.34832 | 2024-10-12 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afe95bbe-0317-3cf8-8bc9-316b2c8b6236 | -3.41769 | -43.35223 | 2024-10-12 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 455773ca-675f-399e-81bd-db22e395c6ef | -3.41543 | -43.34387 | 2024-10-12 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 099f64ba-f866-3eb5-b079-dcff1eb546ba | -3.41481 | -43.34776 | 2024-10-12 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 686780e1-927f-33ad-8ae5-1167e07ae33e | -3.41193 | -43.34331 | 2024-10-12 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e10a430-1acc-3567-9369-edd6080d77ca | -3.41169 | -43.36727 | 2024-10-12 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9966ab59-11ee-3b72-80b2-a9af73ae98e7 | -3.35071 | -44.26282 | 2024-10-12 04:04:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c50b448-e49b-3228-b440-7dcd3ce51aeb | -4.52765 | -43.297 | 2024-10-12 04:04:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40d7c9f5-c33c-3c1c-8776-a6d65bb0c7cd | -4.45897 | -44.57058 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b310362d-857f-382a-8a11-65d84b210369 | -4.45827 | -44.57494 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3e8267df-b625-32f7-869c-2b71a6a14a7d | -4.45758 | -44.5793 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a876c2ba-6f1d-3b60-8782-388f1f60168f | -4.45529 | -44.56996 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f3d8e08-f1af-3af4-bd70-fc2048b14934 | -4.4546 | -44.57433 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d63bcce1-d0dc-3683-8c76-fc488fb1fe7e | -4.4539 | -44.57869 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb4ea0bb-5b89-3831-906f-b5d00c0eb387 | -4.45321 | -44.58304 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c6d25a2-2757-3c3b-b73a-52c665bb9ba0 | -4.45161 | -44.56937 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f36066b-84b8-39c6-a12e-bbdad6580459 | -4.45092 | -44.57373 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| f500f511-bef3-3cec-ae24-217c832cbbae | -4.45022 | -44.5781 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| fcfbdc80-29e8-3de2-b985-1e0cdea25ddb | -4.44953 | -44.58244 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1587e8a0-1919-3480-ba9d-c440744984ae | -4.44794 | -44.56877 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6abe5e4-f7d3-3383-820f-8c4091483bd9 | -4.44724 | -44.57313 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 593bd6de-0317-3216-848e-f47e59158cb2 | -4.44654 | -44.57751 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 12cb7eb7-0ebd-3d1c-ac04-3f425a7e8191 | -4.44357 | -44.5725 | 2024-10-12 04:04:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 129e6d74-b0ec-35fa-abb8-4f5639b0c39d | -4.37996 | -45.79572 | 2024-10-12 04:04:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08c33a8d-ea8b-3af0-9989-afa6d54a5750 | -4.19618 | -45.75916 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7e3cdd0-be33-3f85-be1a-f64cba19c3d7 | -4.19534 | -45.76425 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a044a9cd-9ac0-30d6-959e-3529b0fdc09c | -4.1945 | -45.76932 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f9ea336-c9ea-340f-8183-6a90ce8c5fc4 | -4.04337 | -45.81626 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bff22312-842a-3cc5-91c0-87668b762479 | -4.03994 | -45.81214 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6a3921a5-f344-3ce3-8865-eab69d737a5b | -4.03939 | -45.81556 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5da2fd4d-6d7c-32be-8fc9-0b90d5677d40 | -4.03885 | -45.819 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2e9b19fa-44c9-38a5-92c9-8899f37443d7 | -4.03596 | -45.81147 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dec1ebf-16b7-35ce-9039-60d7ff0c01fc | -4.03541 | -45.8149 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f111dbc-75d6-3a07-b24f-3f7e652b325a | -4.03486 | -45.81834 | 2024-10-12 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63dd8695-f342-3f9a-83bc-50350e07bbe8 | -3.63689 | -45.96114 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4684612f-c2e0-3c73-af87-2276b4e70d5b | -3.63631 | -45.96468 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3c67fad-8acd-3a19-b51e-ef5f40434148 | -2.1012 | -46.3161 | 2024-10-12 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f94a1e19-e167-3cc5-a85f-49f5fe0a2dd2 | -1.63392 | -46.25749 | 2024-10-12 04:04:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 646d11e9-7b15-3728-a859-5c13e808e372 | -2.74011 | -46.78193 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4696d733-b92d-31b0-b0e2-0a82127c5a73 | -2.66062 | -47.07932 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c8c40fc-8f4f-344e-945a-f17eb9a0706e | -2.61123 | -47.34393 | 2024-10-12 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7a64001-c23b-3aaf-8642-3f62675a6980 | -2.60941 | -47.3453 | 2024-10-12 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| edc6c694-1a90-359a-8a12-e7185039f337 | -2.60671 | -47.34319 | 2024-10-12 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30d31489-ea63-3718-a145-d2b2b67511e0 | -2.60594 | -47.34779 | 2024-10-12 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13bf9bf2-a1a1-39c2-a895-029a713f6241 | -3.31182 | -47.01176 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1374955f-6008-3898-9fba-1a564ec55f6a | -3.31141 | -47.00955 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a9564ee-64bc-328e-987f-c57762d6fdf5 | -3.31112 | -47.01596 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7f18252-cbf5-30b4-8454-c406d690c341 | -3.31074 | -47.01377 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9e362d7-6eb9-3e6c-a765-31593f395555 | -3.31007 | -47.01796 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2ba1f1f-4754-3c1d-aa3c-c4769637e229 | -3.21737 | -46.7827 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a130718-45e4-3341-9c00-7d1eb219f899 | -3.21306 | -46.78202 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d3451eae-3cd5-3641-8ac5-75e4fe6b19dc | -3.2124 | -46.7861 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cb4817b7-c9c8-3d44-9f3e-51ddfcb9317d | -3.94563 | -46.43787 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68414a89-b56c-36ef-b0de-51c6ce3bcd7d | -3.9444 | -46.43544 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a1fa7318-637a-37c1-b53a-8e81f0ebcdeb | -3.94436 | -46.4454 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 406b7ed1-844d-3bce-9b03-ab3b4cb96b4d | -3.94379 | -46.43921 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3ed69cc0-3bab-3ec2-a19b-6737bbd15f75 | -3.94085 | -46.43097 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18604bf9-e96d-3691-b999-e6d8d4a5bcbd | -3.93963 | -46.43853 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a2796d25-459b-3fb7-998c-4841f2278937 | -3.93669 | -46.43028 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ce658c55-4888-3da2-8824-37e343396c41 | -3.93608 | -46.43407 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50ff40b0-3916-3380-9543-33ff48df5adf | -3.93548 | -46.43785 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a57af00-a6e2-31ee-a40e-674ead01f2ea | -3.93131 | -46.4372 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4aaad23-6ae8-344a-9776-edadb4ba644a | -3.926 | -46.41728 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9ced919-1d09-3077-8ec6-5dc2f70fea1d | -4.10515 | -46.80561 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb6a9036-d388-33d5-9440-51f2b8360fc2 | -4.10156 | -46.80621 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59830432-629f-3493-85ee-babea1637998 | -4.10091 | -46.80484 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58c7b1ef-67ab-3f89-88f0-f6524182716c | -3.94499 | -46.44163 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 632b6ec3-0152-3599-8582-e7739b5eb385 | -3.94319 | -46.44299 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60ad5bff-fc78-327e-891b-bafab0a736d7 | -3.94024 | -46.43475 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8d4719dd-c3ee-37ff-b4c7-a7a3c971f249 | -3.93903 | -46.4423 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58274f94-069a-3408-9fc3-08fa5111c603 | -3.93842 | -46.44608 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eef07d7c-1d1d-33ac-bd01-cae473f43946 | -3.93487 | -46.44162 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eb945490-0acf-3266-872c-f63f7eed8b11 | -3.93426 | -46.44539 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8edd897c-c66b-3b80-b1a2-282a65d85491 | -3.93071 | -46.44095 | 2024-10-12 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad8b6396-62b1-3a40-adc8-53ed84b6baf1 | -3.56184 | -47.35881 | 2024-10-12 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ffdfdf6-2b59-380b-a3db-d6c927e96233 | -1.99948 | -47.25797 | 2024-10-12 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4f0ff483-636c-302d-9930-8e10de727d2d | -1.61937 | -48.02407 | 2024-10-12 04:04:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 718e1e36-1130-32ea-8edf-86effd684b53 | -1.61853 | -48.02937 | 2024-10-12 04:04:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cde4d22-dda5-3db2-ab59-bcdd0c13e6a1 | -1.06763 | -48.24428 | 2024-10-12 04:04:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d364fe13-091d-3b7d-a984-9dbaf6f7555c | -1.0655 | -48.24842 | 2024-10-12 04:04:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3d95909-8703-3f4e-81b4-8a115de51ab6 | -0.87108 | -47.43317 | 2024-10-12 04:04:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0217d11-cefc-350b-8660-08526c222499 | -2.83212 | -49.53408 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22ae2aa4-64e3-3f1f-b121-074d9a4ab36f | -2.82 | -48.45415 | 2024-10-12 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a091f946-d780-3a72-8f8b-030132bc82a7 | -2.81913 | -48.45951 | 2024-10-12 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3082957f-3b9a-35b3-9275-ccfb766f03b7 | -2.81514 | -48.45332 | 2024-10-12 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8aed685-f102-3c21-b040-e36d1e1f986e | -2.81426 | -48.45871 | 2024-10-12 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 066d0ce4-e1cf-3a07-ae38-119484b7e265 | -2.78479 | -48.09749 | 2024-10-12 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6aff76fb-a1bc-3185-b6f7-d944ddfe72b4 | -2.63005 | -48.48033 | 2024-10-12 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bce65a3-0fa5-34f0-9d29-8fc6c94023ee | -2.62917 | -48.48581 | 2024-10-12 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f20fcd3-742f-3dbd-bd10-594fc3e8e8ea | -2.62832 | -48.47669 | 2024-10-12 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a125b19f-2a67-3f8c-b23e-3e163e23dd38 | -2.62741 | -48.48213 | 2024-10-12 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acf21ef7-9c09-3a74-ba24-b12f1b42a40b | -2.62691 | -47.98574 | 2024-10-12 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f3cfd98-e8a1-332a-8c04-714ce83923b5 | -2.62649 | -48.48758 | 2024-10-12 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f70fef7a-df35-38e8-bfe1-7d2037bcb37b | -2.62577 | -47.98503 | 2024-10-12 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README41.md)
