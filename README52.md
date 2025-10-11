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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47ad438d-515f-3624-8927-d756c4b25705 | -8.4838 | -46.1789 | 2025-10-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a76a0b7d-0996-30c6-bfdd-c051222851aa | -12.7299 | -45.8422 | 2025-10-11 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f748e6aa-b33d-3ce0-849e-d6d28517ce25 | -11.6278 | -47.5338 | 2025-10-11 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| d612ec43-fdda-327f-b6b9-dd44203fa294 | -11.7027 | -44.2879 | 2025-10-11 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 114afc2f-b39d-3515-abdd-b4d443607c7e | -9.3947 | -45.7882 | 2025-10-11 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 42bfd4c3-7fbd-3b4f-bad1-8bd4df0d7256 | -8.5024 | -46.1995 | 2025-10-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 9276a7cb-7d1d-3336-8b5a-955a3828be97 | -13.0783 | -47.801 | 2025-10-11 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 0a51af0c-f3a4-3a4e-9ee5-607f79232195 | -15.6538 | -44.4838 | 2025-10-11 13:40:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 148.9 |
| d2def362-7d04-32cc-a794-c87a554a189b | -10.0545 | -67.5484 | 2025-10-11 13:40:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 264139b5-b984-3936-b762-9267083595ed | -11.8635 | -44.938 | 2025-10-11 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d4327399-1f68-3f28-afca-44c199caa460 | -8.5029 | -46.1545 | 2025-10-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 15dc86d7-b7ec-3b9c-a2ed-a8e7d0c44c5d | -15.0021 | -45.5725 | 2025-10-11 13:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 939fb610-e27f-32d5-9d57-f6832d2a1099 | -9.3951 | -45.7655 | 2025-10-11 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 11871160-ed25-3b3c-93e6-20fc64664b3c | -13.8501 | -45.7992 | 2025-10-11 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| c241c690-ebf8-3ca8-a425-a36dba2f8bb2 | -9.4137 | -45.7861 | 2025-10-11 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| df52430b-3f10-3975-a52b-d72fe94fd974 | -8.5021 | -46.222 | 2025-10-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 195.7 |
| c67bcf0f-13c6-3588-9d1b-e9881ac27f89 | -13.2833 | -47.1203 | 2025-10-11 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 435a48fe-5a99-367c-a5e4-74d12a3154be | 1.2241 | -50.8724 | 2025-10-11 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 5cbb9b7e-e194-327c-90d7-0ef5cee1a885 | -13.3026 | -47.1174 | 2025-10-11 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 129.7 |
| a0b8067a-c183-33e2-b4d7-1d6e54e60790 | -8.4833 | -46.2239 | 2025-10-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 65707621-05e4-3d66-a1fe-a9aa42d15106 | -11.7809 | -46.3687 | 2025-10-11 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a5c21135-92c5-3cc9-a145-20ee391596e4 | -11.7507 | -47.0261 | 2025-10-11 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 0394ef4c-0305-3c17-8861-fa40d7ce05e1 | -13.8496 | -45.8223 | 2025-10-11 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| a01330a6-26b5-32cb-8b12-44b1340ee3b8 | -8.5027 | -46.177 | 2025-10-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 5d12faad-1cf2-3454-b9bb-00b345da6b5f | -11.6282 | -47.5115 | 2025-10-11 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 5054b718-92ee-3e5a-84fc-994832953e00 | -10.9231 | -47.5564 | 2025-10-11 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9db772c4-10cb-33e1-ad37-3e3e2f199416 | -13.322 | -47.1144 | 2025-10-11 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 498ff023-9ff3-3a5a-ac65-d9b17bfbaf15 | -13.0787 | -47.7787 | 2025-10-11 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 1f8481ce-68fc-30b1-aabd-91630260490c | -9.0022 | -45.4693 | 2025-10-11 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 294f8a74-4e6c-3167-ae69-85ad3a8a8d03 | -11.7219 | -44.285 | 2025-10-11 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 31ed2b39-a2e7-3f5e-8063-d15020be4061 | -12.3592 | -47.2335 | 2025-10-11 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| df9d3c1b-cb89-31d2-a430-ad4145b843cd | -11.7422 | -46.3967 | 2025-10-11 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 072ef8b0-a0a6-3237-98ae-1e5516cb15b0 | -13.7999 | -45.415 | 2025-10-11 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| d294dd27-bc13-3d67-9453-f897d32bee96 | -10.6703 | -46.6954 | 2025-10-11 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| be34acca-71e8-3a68-8e3a-66c8a381d91e | -8.4835 | -46.2014 | 2025-10-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 33b7b375-9a1a-35f1-9213-21dafb213c30 | -10.9041 | -47.5588 | 2025-10-11 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2b2aa972-3956-3d8f-ae5d-ff51e25f00a0 | -13.3874 | -47.7331 | 2025-10-11 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 382be0bb-070e-3aa7-ab68-a95c0cfc2c88 | -11.7219 | -44.285 | 2025-10-11 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 738f8383-5bc1-3271-9370-e83c5c04f0d0 | -14.983 | -45.5528 | 2025-10-11 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 149.2 |
| d1448043-6c21-3ca2-89e1-5859d6649669 | -9.414 | -45.7634 | 2025-10-11 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 976d597e-3452-396d-816f-f463bacc07da | -10.0731 | -67.5478 | 2025-10-11 13:50:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 66d370be-3879-34dd-831f-79549658bda8 | -11.8827 | -44.9351 | 2025-10-11 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 744e6074-fa36-364b-82ef-0d86662fda12 | -10.1714 | -44.5496 | 2025-10-11 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 272066a9-2986-3da5-bf16-043327b7f502 | -13.2833 | -47.1203 | 2025-10-11 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| fb953d08-c7e1-38c3-a5c3-3e14965f0319 | -13.3026 | -47.1174 | 2025-10-11 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 7eb9cf10-0df7-31c9-9253-a85b3605c18e | -13.8004 | -45.3917 | 2025-10-11 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 3c4e4352-8120-391d-8976-a91c8b437a4a | -15.0021 | -45.5725 | 2025-10-11 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 4f6eac63-9bff-3ea1-9b2f-0180a71bdf0a | -9.3947 | -45.7882 | 2025-10-11 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6719d890-8986-3941-88b3-5ca054cffc90 | -10.6703 | -46.6954 | 2025-10-11 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 0ffa4970-6cdb-35a8-9b7b-206378148980 | -11.7809 | -46.3687 | 2025-10-11 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| a87bc63f-5b15-379f-bec9-542f36126f43 | -10.2088 | -44.591 | 2025-10-11 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| b35b74b0-29a1-3c54-9ed6-c700eef1cefc | -9.4677 | -45.9834 | 2025-10-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 1a218227-0d4d-31b1-b601-3ae9c4c6dac8 | -11.6278 | -47.5338 | 2025-10-11 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9b6aa725-91cc-3b2a-b186-4d2793373e47 | -13.3874 | -47.7331 | 2025-10-11 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 444db72c-e69a-3fed-808d-cfaa025ea988 | -12.3592 | -47.2335 | 2025-10-11 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| c1335af8-1510-3fd2-ba9f-d54d9b416fb3 | -12.0118 | -45.2161 | 2025-10-11 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 04a380f4-3c52-37a7-8444-1b1478d9d55e | -18.0799 | -57.5347 | 2025-10-11 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.0 |
| c3482c90-a35e-360c-9199-ab10745e9207 | -10.9293 | -47.1553 | 2025-10-11 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 69bfbe4e-a577-33e2-b97f-dda44e677868 | -9.4674 | -46.006 | 2025-10-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| cab6daf3-b735-3639-892f-46f0b5a8efe1 | -14.2749 | -45.8879 | 2025-10-11 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| dde69d66-0861-3d0a-9819-17fc5dac3544 | -13.7804 | -45.4183 | 2025-10-11 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f748100b-a7a1-3d5d-8211-4357a1534378 | -12.7299 | -45.8422 | 2025-10-11 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| aacb93b6-ab7e-347d-b94b-062c19156702 | -10.0545 | -67.5484 | 2025-10-11 13:50:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 109.6 |
| eea1c2f8-1658-34db-ae82-de8ff4251ccc | -13.7999 | -45.415 | 2025-10-11 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 8d07d011-5457-37bb-8479-b65683be1f7e | -15.0026 | -45.5491 | 2025-10-11 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 3fa8b208-aa92-39e5-8e19-711462dc51e7 | -8.1618 | -43.323 | 2025-10-11 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| a2f58226-8229-390d-9e5c-951362488036 | -10.2085 | -44.6141 | 2025-10-11 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| e3b56aeb-a8a7-36cd-a53b-86242467ed73 | -10.9364 | -47.9309 | 2025-10-11 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 813cd981-9551-3fd1-a0a4-af7a647acdca | -8.5029 | -46.1545 | 2025-10-11 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 2f90d5c5-a139-3554-909b-0821b44b758b | -10.0751 | -45.8894 | 2025-10-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 6d353574-f34f-3605-95c7-ffee06fce77c | -9.0022 | -45.4693 | 2025-10-11 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 211.7 |
| 6437e9eb-30ac-3abe-a2e6-a4bc6363f510 | -12.9229 | -46.8364 | 2025-10-11 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| f2aa2c0c-ab6b-3e04-8e87-f6912d0dc0c0 | -9.4137 | -45.7861 | 2025-10-11 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| fa0b2ad4-66db-3e1a-ae3d-9bc981f2a5d8 | -9.0022 | -45.4693 | 2025-10-11 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 678e8e7d-a91f-320d-813a-b1c8f910c94a | -9.3947 | -45.7882 | 2025-10-11 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| bfe8bd02-c7b6-3f88-9cea-36b5e26347df | -8.9833 | -45.4714 | 2025-10-11 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 3da618d1-5bcd-310f-bac9-d2fb0f79e0ce | -18.0601 | -57.5371 | 2025-10-11 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 38bbb8ed-3971-3e62-8dad-80990c074fb6 | -18.0799 | -57.5347 | 2025-10-11 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| b235bccf-0f59-3054-bf7b-6fec56a3db6c | -9.4677 | -45.9834 | 2025-10-11 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 7e5a0392-5ef2-37fc-a2c7-b9caafd1f051 | -10.9293 | -47.1553 | 2025-10-11 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 188.1 |
| e62d6af7-0efa-3e0e-921c-423cfc242b9b | -8.1804 | -43.3445 | 2025-10-11 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 10b7747e-5f81-37d8-9720-d33268cfa2f7 | -10.0999 | -45.5001 | 2025-10-11 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 4d0a2cff-6c9e-37b6-8303-3beb567e5fe9 | -13.7999 | -45.415 | 2025-10-11 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 6149d141-39e4-3a0a-a6f2-59a61612b7c7 | -13.2829 | -47.1429 | 2025-10-11 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| bb1e2679-a134-3471-bca7-1effa89799f4 | -10.2088 | -44.591 | 2025-10-11 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c18a1908-eac1-3641-9ed7-71f58a92b890 | -12.5097 | -47.3913 | 2025-10-11 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9c88af34-acba-32e7-80c6-8fc7dc34a280 | -12.9229 | -46.8364 | 2025-10-11 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| fdd894b3-e104-31a8-bf39-aa94aa2468b1 | -12.7299 | -45.8422 | 2025-10-11 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3821acfe-6dae-351f-a2d7-e3db887d9d2d | -10.0545 | -67.5484 | 2025-10-11 14:00:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 133.1 |
| fc0df471-f10c-318f-b147-d77f0baa3687 | -10.8538 | -47.1201 | 2025-10-11 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 1491ba07-506d-3b8e-9a53-64a72609bef8 | -8.1996 | -43.3189 | 2025-10-11 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 259.0 |
| 96c84e19-5ce7-389b-8e2b-09093fc7fa83 | -8.1618 | -43.323 | 2025-10-11 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| fd9e77fd-5147-34b1-82e4-a1cb31c17498 | -9.6974 | -45.7986 | 2025-10-11 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 45f5c0f9-e925-3377-b1e5-e0abb1f41125 | -9.3951 | -45.7655 | 2025-10-11 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 11c0fcba-3b4e-3ff1-86dd-84b046b6e026 | -13.0787 | -47.7787 | 2025-10-11 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 06c7cadc-43b2-3ad9-a75c-ef9bb168da76 | -8.0154 | -44.4539 | 2025-10-11 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| a99a3a1e-cff8-3150-9eb7-e08ea469fcd3 | -13.8004 | -45.3917 | 2025-10-11 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 223.2 |
| bee8d922-75e8-3f98-98b2-1964d5bef8e9 | -10.2085 | -44.6141 | 2025-10-11 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 64226186-aacc-334f-8903-a0982165c892 | -10.0995 | -45.5229 | 2025-10-11 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a05c2405-6cbf-3452-8de7-8140783aa7f0 | -10.8535 | -47.1424 | 2025-10-11 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 238.0 |


[Clique aqui para ver as próximas entradas](README53.md)
