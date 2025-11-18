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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e36ccdb8-6f0e-323a-ae7d-bfff02e6672b | -10.37832 | -49.89368 | 2025-11-18 04:50:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99366d12-78bb-3a52-9b4a-a769b80b7058 | -12.88141 | -46.06055 | 2025-11-18 04:50:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57d02437-c0cd-3c42-8be8-c79a72c91548 | -7.10652 | -48.7154 | 2025-11-18 04:50:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18d86fdc-5dff-3b2f-9937-9b47acf74b95 | -7.43504 | -48.94217 | 2025-11-18 04:50:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4ca5e3b-e70c-3598-a39f-cea1202e81e9 | -10.36083 | -48.92202 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 470885f2-580f-365d-9482-7416a251d698 | -12.98707 | -44.11861 | 2025-11-18 04:50:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a64ccca7-1580-366e-9fcf-aeeba8bf32d1 | -9.0559 | -45.42508 | 2025-11-18 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1e8dea1-70f4-3f89-9295-6a816722ebeb | -10.84825 | -44.87766 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20ebec38-b01d-3843-b295-396e1c266533 | -8.29526 | -44.22484 | 2025-11-18 04:50:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f70b363b-e1e5-3d64-a76b-cdc538351e7a | -11.09921 | -45.43633 | 2025-11-18 04:50:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c0062b6-c78a-332e-87ce-91ceab4015e3 | -8.54372 | -46.04803 | 2025-11-18 04:50:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4ddbed6-2108-3be8-bf0b-41bd31ce36ac | -8.08782 | -46.05305 | 2025-11-18 04:50:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4acd177-562d-3468-b80a-4822c9353d58 | -12.70429 | -46.79597 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45f0b286-6ec8-3926-926a-42a7d691e1f2 | -11.66845 | -44.72989 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e090d153-31c1-3f3f-bf32-0d6d380c6e2a | -12.86405 | -41.48608 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 98a87f4d-bb6b-32be-800a-773913bad633 | -9.4935 | -63.51065 | 2025-11-18 04:50:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17d5ddeb-e1b3-30f8-9fbd-a41f3d0dd880 | -7.62057 | -42.58275 | 2025-11-18 04:50:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eb51cf32-3957-380d-841c-377ec4dcf17f | -12.85971 | -41.48436 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| fe85e3e2-d3ef-3b50-8f94-45ca13d7192a | -11.20588 | -49.41601 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 14a23b6c-70ca-33f7-84da-aae03f375df7 | -12.70361 | -46.79727 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac8afff2-6029-38e6-8b56-5da60a354ff2 | -12.86104 | -41.47266 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1aa70541-05e8-387a-9533-50c117a369bc | -10.51096 | -43.96214 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b286606-a098-3b26-a8a7-d3c0f1f2d105 | -11.4259 | -43.3296 | 2025-11-18 04:50:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41026dd9-bfb7-3810-b1d8-c09c2e9c2e91 | -13.68362 | -42.03035 | 2025-11-18 04:50:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d212a92-f78c-3c82-85fb-732596e34f13 | -10.09537 | -47.51406 | 2025-11-18 04:50:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 069d4a74-01aa-35ab-86c4-8cc484e25c3a | -8.57219 | -46.48481 | 2025-11-18 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f647d36-7d31-3b45-901d-334c9da84a35 | -13.89923 | -47.49099 | 2025-11-18 04:50:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d5f5516-0cd8-3c5c-9b88-d226b0d97a30 | -10.51978 | -43.96099 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5574eb04-1111-319d-9a4e-3a9fd7ab675a | -8.30114 | -44.00872 | 2025-11-18 04:50:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 883879de-b730-39b4-8829-1ee925db1857 | -6.86403 | -47.07899 | 2025-11-18 04:50:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ae7095e-24d5-351a-b9ca-6ad83de0ce28 | -9.21201 | -48.88685 | 2025-11-18 04:50:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33b90e63-cfab-3d1f-8646-3b0a86021852 | -11.61625 | -48.56954 | 2025-11-18 04:50:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3ca7e67-f8b5-3a96-b85a-32e34e6e0081 | -12.85783 | -41.48705 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4d3633e7-124c-3679-bd57-835e24776829 | -8.56405 | -45.10481 | 2025-11-18 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89631472-779a-30ae-9c2d-62012345c1bb | -11.28947 | -48.51379 | 2025-11-18 04:50:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10b64bdf-49c4-3daf-bf63-c7b53d3b6c36 | -12.86515 | -46.40877 | 2025-11-18 04:50:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d93e7f89-89bf-3797-bc39-26d7bdd06ee9 | -11.84844 | -49.2253 | 2025-11-18 04:50:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be5560f6-9fe2-3c7a-b977-7e8e289254c2 | -10.52085 | -43.96339 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4893296c-3489-35e8-9e21-9bbc26b4583b | -11.66232 | -44.73956 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27a2a28d-6dcf-352c-9169-c64aa70c8f3c | -12.66752 | -46.7481 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4779ff0-a61f-3b90-a805-f0f33d784495 | -8.3814 | -44.06432 | 2025-11-18 04:50:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9503a228-5cb7-3442-88f1-9fcb14ca26ec | -12.00233 | -49.26421 | 2025-11-18 04:50:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 770a9959-051c-3670-b0fa-9416645b969e | -12.43066 | -47.88173 | 2025-11-18 04:50:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b6dbed7-5d09-3160-aaab-11f61d524bb2 | -7.86032 | -46.86518 | 2025-11-18 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81fe4e89-98bd-3c7d-a2d9-5c3ee7666409 | -10.36144 | -48.91784 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5403ee46-0efd-331f-be4d-a8f4bb8facc8 | -11.39497 | -43.32221 | 2025-11-18 04:50:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c61f8ac-7be0-31bd-9cb9-6406ce605784 | -8.935 | -49.8424 | 2025-11-18 04:50:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f609b8c-0de0-392c-b1e4-660ada9aa477 | -6.71388 | -47.79381 | 2025-11-18 04:50:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6a10120f-ac93-3191-9b99-13c20fc64160 | -12.29145 | -46.80381 | 2025-11-18 04:50:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 469141c3-2229-35f0-9bff-8ece513af35a | -8.46815 | -47.9808 | 2025-11-18 04:50:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48ba04c5-a5bb-3176-bfe6-d5a942848dec | -7.80146 | -42.62415 | 2025-11-18 04:50:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 173b386e-c8a4-3c9b-92e8-66f998bfe74d | -11.85204 | -49.22586 | 2025-11-18 04:50:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95ff6232-19ad-31bb-8b02-20bfb698f658 | -12.86664 | -46.4072 | 2025-11-18 04:50:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06103b8c-dae9-3b64-a13b-d828863be643 | -7.43319 | -45.19597 | 2025-11-18 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d97eba8e-e0fc-3f7d-9df6-41b6dc0973a0 | -6.93889 | -49.66791 | 2025-11-18 04:50:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17b93b32-b8b3-3b0e-8087-5cd23b41f976 | -10.29371 | -48.89645 | 2025-11-18 04:50:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ab85b20-718e-390a-8dc1-affae409f917 | -10.7662 | -44.17768 | 2025-11-18 04:50:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b592cd77-e53e-3f43-8fd0-8767e0c45508 | -8.55255 | -46.04566 | 2025-11-18 04:50:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cb05195-e1c0-3eeb-92ef-a807daf33eb1 | -8.93786 | -49.84664 | 2025-11-18 04:50:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0649df5-4426-32c0-bc71-a41bfd3353dc | -12.06635 | -48.19348 | 2025-11-18 04:50:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffe8bf02-6fc4-36be-a24b-dda7a86c602e | -9.50772 | -47.47084 | 2025-11-18 04:50:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcfc20a0-7f4c-3471-b75a-bfc5b4a01f99 | -6.71754 | -47.79434 | 2025-11-18 04:50:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ff27d8af-1f13-3f12-b178-4207029dd572 | -6.85102 | -46.1116 | 2025-11-18 04:50:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2496e641-ac17-3dd2-b90f-bdf4ba216c4c | -7.07187 | -46.04589 | 2025-11-18 04:50:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51c94db1-79f3-31ad-bca7-f4ae47fe3f75 | -12.74186 | -45.43323 | 2025-11-18 04:50:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ff014d1-86e8-3735-aa3d-302f496b2296 | -6.83518 | -46.30092 | 2025-11-18 04:50:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93e719be-d65c-3311-a8d1-3d63ff7d674f | -11.16336 | -49.45878 | 2025-11-18 04:50:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f5b5d2b-f9f8-301c-8753-3287f7dea612 | -10.29658 | -57.14248 | 2025-11-18 04:50:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 374f20f9-e2fa-33a1-a2e7-5b2859a7b7f8 | -8.54426 | -46.04418 | 2025-11-18 04:50:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e2609b1-c591-378e-9553-7ef074724eac | -10.29011 | -48.89594 | 2025-11-18 04:50:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e45dc86-635e-3e6b-9359-8307fd20ab54 | -12.00531 | -49.26895 | 2025-11-18 04:50:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d3e2d5e-e983-31ca-af84-a32340e5be5d | -7.62617 | -42.58057 | 2025-11-18 04:50:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 052b0565-15e2-36d6-894b-a1404bd6a853 | -9.03271 | -45.46416 | 2025-11-18 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0c71956-1c20-35f7-a885-71d2f817113a | -12.00171 | -49.26841 | 2025-11-18 04:50:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 650702d2-bb1c-3ef2-a19d-1ed113f75cb2 | -10.35724 | -48.92145 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60fa70f7-96cf-36ce-aae2-27a349f679c8 | -10.75022 | -48.03515 | 2025-11-18 04:50:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ab89666-b95f-3f7c-8b74-12c5269d6db3 | -11.84238 | -47.59357 | 2025-11-18 04:50:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b5470c1-99a6-34cf-bb9c-7a2eb3642eba | -7.86742 | -46.87131 | 2025-11-18 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4221e9f4-c513-3538-842a-22002994552d | -8.29595 | -44.21984 | 2025-11-18 04:50:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f6f25b7-65d2-3f62-a98a-e1f7554ba7b3 | -7.92667 | -46.03009 | 2025-11-18 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 802ea3fe-686a-32d8-8aba-6f5403eb372e | -11.84165 | -47.59862 | 2025-11-18 04:50:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4737ea00-10ff-3858-a1af-a379149cf954 | -8.79312 | -44.39309 | 2025-11-18 04:50:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e34c042f-f21c-32e4-8acc-6bf748f78786 | -10.91546 | -49.4118 | 2025-11-18 04:50:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3044ad96-c171-38a4-abef-903899f7512c | -11.72438 | -49.84778 | 2025-11-18 04:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9501fe55-6799-3acd-a809-f17cce52c0a2 | -11.84074 | -47.59563 | 2025-11-18 04:50:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a717827-ecc7-37af-a755-5621322690be | -9.3911 | -48.45594 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 980150f2-e58f-3920-8f3a-41ffa2d1fb8e | -11.66776 | -44.73505 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c62cac32-ad6b-3e8f-87ec-f4c5d408a51f | -12.73725 | -45.43264 | 2025-11-18 04:50:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e9a9904-7bb2-3d6d-9896-6e57ff8a8e63 | -11.74511 | -49.3464 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 581a007a-2d4a-3588-80c3-cf6230955120 | -9.40025 | -48.44436 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ae4d1398-a191-387c-85b0-9605cc994ade | -10.3637 | -48.91985 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8437d1b0-96ea-30e8-bf8c-023cca464fe8 | -12.51826 | -54.38256 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff8bf966-0bcc-3c9e-9f6f-778d7b475361 | -9.50454 | -47.46553 | 2025-11-18 04:50:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5e90e28-824e-37e2-ad68-c22cd701ce88 | -12.85487 | -41.47336 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| eb63a406-a4f5-3243-a9ba-e414a5979cad | -6.94228 | -49.66843 | 2025-11-18 04:50:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1276cac2-f711-355a-996d-de0a8ab07d4c | -10.7949 | -47.64141 | 2025-11-18 04:50:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91a3762d-b0c1-30af-aba9-e82983d7a063 | -12.89534 | -54.72495 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| baa63acc-1ee5-3b32-80ad-c659cb5c9601 | -10.8034 | -48.0938 | 2025-11-18 04:50:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 316314d7-3db6-3717-922b-ed19d0804c2f | -8.98224 | -47.7294 | 2025-11-18 04:50:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36b9965c-3350-30fc-a1be-6a628906ff0c | -8.93842 | -49.84293 | 2025-11-18 04:50:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README46.md)
