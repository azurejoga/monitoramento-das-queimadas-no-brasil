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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20f79e73-d1f1-3552-a6d8-f903a110c40b | -15.229 | -52.7101 | 2025-09-04 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 08ae8245-812a-3ca4-a76c-3a17c2754305 | -5.6777 | -45.6089 | 2025-09-04 13:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 311.5 |
| 875ef1af-7e46-3dce-9ce1-7740b1642f47 | -5.6965 | -45.5851 | 2025-09-04 13:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f5ee5a1d-e6a4-327b-90ce-3e8e0d04fc80 | -6.3502 | -45.6498 | 2025-09-04 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 29593448-1cf0-39d9-9604-3aae574ae296 | -5.908 | -57.7311 | 2025-09-04 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 6aeab171-b0d5-382a-98af-3456c188e5cf | -11.6525 | -52.212 | 2025-09-04 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8a4a1de0-9d1b-3639-b1b6-a4c615c9bb7b | -7.6851 | -48.7386 | 2025-09-04 13:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 3809044e-99df-38c7-8277-7ff23d7dcc2d | -22.6567 | -43.6825 | 2025-09-04 13:20:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 126.8 |
| c212f47a-5662-3bc1-83ff-a692fbf90e80 | -6.0784 | -44.6961 | 2025-09-04 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ce5bf8e3-5370-3d9e-b5e7-3bb9a9e186f6 | -11.5782 | -52.094 | 2025-09-04 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| be02b3c2-6b52-3e37-977f-f4f047b8298b | -5.8525 | -57.7722 | 2025-09-04 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 0f5e88fa-e983-3afa-a514-f3cc37bbc8f0 | -5.7002 | -45.156 | 2025-09-04 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 9c5d3c0d-773e-3fcd-9ef3-b34503556f27 | -11.5779 | -52.115 | 2025-09-04 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 348b6f91-200f-3e7a-925f-458c52df9590 | -6.2205 | -43.5558 | 2025-09-04 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2cec5481-e529-308f-9d5c-869c40f3fd42 | -6.213 | -42.4294 | 2025-09-04 13:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 832d3e99-dff6-3941-b97c-d10c3b9c66f4 | -13.8651 | -47.9734 | 2025-09-04 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 8eff4b3f-c1ee-3f97-b519-92145500ef85 | -11.5972 | -52.092 | 2025-09-04 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| eda3d31a-7c5a-36c1-acd0-bc2858d35760 | -6.3689 | -45.6483 | 2025-09-04 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 311.6 |
| ce6279ed-26fd-358f-ae01-ee6d8194a912 | -6.7992 | -45.6815 | 2025-09-04 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e79bc533-3168-31d9-a1a0-4ee163cef663 | -6.2127 | -42.4532 | 2025-09-04 13:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 0de16d0d-55ae-3c00-b65c-bbe8d90430ef | -16.5497 | -55.0991 | 2025-09-04 13:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 2184d9f0-f71e-3fa5-b137-2c2b063b7bdd | -10.5031 | -50.4295 | 2025-09-04 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d0f27f08-cbaa-34a9-9f38-ce2d5fac6480 | -12.4593 | -48.0885 | 2025-09-04 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 634e56e2-8bcf-332b-9c16-1375e82ceb09 | -10.7497 | -45.2795 | 2025-09-04 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8f26fe29-1029-35b9-8095-131eb25a5c24 | -21.7038 | -45.4179 | 2025-09-04 13:20:00 | GOES-19 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.8 |
| 911a8d8a-1c08-3b38-8575-be232508a0f9 | -8.3644 | -48.3116 | 2025-09-04 13:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 661cc691-7dff-34a4-ba99-775d12c85e11 | -11.6601 | -54.5093 | 2025-09-04 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 5583f984-be41-37aa-83dc-888cdb464614 | -11.7385 | -47.7637 | 2025-09-04 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| a296aca1-5efc-3036-983c-7e1b53e78731 | -8.8842 | -45.822 | 2025-09-04 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9063a0eb-9313-38ad-99ec-3efe0783f55b | -11.7389 | -47.7415 | 2025-09-04 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4e986794-c94c-3e2f-a931-e473ffbd3471 | -11.6599 | -54.5297 | 2025-09-04 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 7973b636-0889-3db5-9d37-c6f735986b9a | -8.3641 | -48.3334 | 2025-09-04 13:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 36c63600-2a49-30c7-b2ee-df3844f032bb | -4.9951 | -56.256 | 2025-09-04 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 2505ab2c-7640-3a52-85d3-1e625bb31fe4 | -13.8457 | -47.9764 | 2025-09-04 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 07310b3b-f23a-3bc8-8fa7-3f2930532445 | -15.408 | -55.9416 | 2025-09-04 13:20:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8f6cd656-2e15-3353-8b4c-97e53ee4e3aa | -11.5969 | -52.113 | 2025-09-04 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 9481385f-6cd1-3a78-a61b-b17b86d76b91 | -9.7108 | -48.9636 | 2025-09-04 13:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 19be03a0-e14c-39c9-a804-3ae9a5c7e240 | -12.5173 | -48.0584 | 2025-09-04 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| cb7b479e-6a79-31d6-bd20-b0ba3cd6cfe0 | -17.0652 | -46.449 | 2025-09-04 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 149.8 |
| c5dab3f0-106a-3e1b-82dc-ab5ae0df0a14 | -8.9028 | -45.8426 | 2025-09-04 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| e0156802-0fd6-32cc-a4f3-873f5f9503c0 | -6.2961 | -43.503 | 2025-09-04 13:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 8dea171e-584b-3ed5-b77d-1e1984e7fb90 | -5.908 | -57.7311 | 2025-09-04 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 058e38af-0c5f-3b27-8de5-8f3c47bf3f98 | -9.6851 | -51.0186 | 2025-09-04 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e3107f9a-1666-3327-8159-d5bcb715f215 | -7.6851 | -48.7386 | 2025-09-04 13:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 208.8 |
| cc4b5031-5168-3ac0-a260-7b99fc37bdda | -7.6854 | -48.717 | 2025-09-04 13:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 80.6 |
| e22828d3-bd67-37ba-9e80-7c4ca6367b52 | -9.7108 | -48.9636 | 2025-09-04 13:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 1bc2da2f-6d21-3c40-94c1-c59603b9374b | -6.3692 | -45.6258 | 2025-09-04 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 54b9b9f1-a15c-3b0a-ad67-497d314f86ff | -11.0062 | -45.9072 | 2025-09-04 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d3ab05b1-e38b-358a-ae43-f090a927ec67 | -11.7385 | -47.7637 | 2025-09-04 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 9a40e44b-5296-30ff-9aeb-f38ef1e83fba | -11.6231 | -46.6614 | 2025-09-04 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 81d99cd6-4d10-348e-9544-8102d1f91945 | -7.7252 | -50.3174 | 2025-09-04 13:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fd620ccc-6385-391c-83df-319778571747 | -7.7409 | -48.7772 | 2025-09-04 13:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b43330bc-3fbc-3168-bc4a-952d6b852828 | -5.8525 | -57.7722 | 2025-09-04 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 88adbd00-83ae-3d13-bc6f-e009a24a7200 | -8.3829 | -48.3317 | 2025-09-04 13:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| c36178ef-42b1-34ef-a19a-16161cfc7120 | -6.2062 | -45.0506 | 2025-09-04 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 63feb8e5-4a5d-3636-bba5-7b9827bb4690 | -5.9442 | -51.9589 | 2025-09-04 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 8ba2ceed-c017-3168-986e-fb1cf3f8b43b | -10.1457 | -46.2424 | 2025-09-04 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 824a2983-78de-3ae5-9b4a-ac80dbb03b7f | -6.2315 | -42.4515 | 2025-09-04 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 167.3 |
| da6c42ee-99c6-3995-8a22-6f468437d715 | -8.3832 | -48.3099 | 2025-09-04 13:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d494b5f7-c02e-3338-be78-c7a95ab955b0 | -11.5972 | -52.092 | 2025-09-04 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d4a63e81-3db9-312b-8631-ba0ba7e09b7c | -12.4981 | -48.061 | 2025-09-04 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c72cf64b-4500-3017-862d-04ec71636426 | -7.7039 | -48.7371 | 2025-09-04 13:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 9b83e438-f878-34b1-8eb3-9cb9b4303b20 | -8.9031 | -45.82 | 2025-09-04 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 159.4 |
| dde88b9e-0386-399c-85d5-c2ae0538c584 | -8.3641 | -48.3334 | 2025-09-04 13:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c088afb8-54fe-319f-9d09-b32d3e516ebe | -12.4593 | -48.0885 | 2025-09-04 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 18fe7aaa-3af3-38c4-9e8c-1604538d4cfa | -14.5855 | -53.0056 | 2025-09-04 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e2a41d0d-8d9a-3720-a5ee-2341c68eac65 | -6.2038 | -43.3475 | 2025-09-04 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 45af9693-9df3-312e-93de-db52b495b8ac | -15.408 | -55.9416 | 2025-09-04 13:30:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f1dd4a43-e86d-34b9-922d-81eb8ed55b31 | -10.1644 | -46.2627 | 2025-09-04 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 4c1ff1a2-bde7-32bd-b04a-30222bfa2424 | -18.7517 | -44.5835 | 2025-09-04 13:30:00 | GOES-19 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 93.2 |
| b7fb4cc1-76dc-38e4-a3ec-070d61fced0e | -6.0421 | -46.6549 | 2025-09-04 13:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| d4782c70-7040-35cb-a365-57091d8df0e2 | -6.2205 | -43.5558 | 2025-09-04 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 45d07ef3-2a36-32d3-a863-054b19064b6b | -11.6599 | -54.5297 | 2025-09-04 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| c9a05d42-176f-395f-baef-753151a2cb3e | -6.2249 | -45.0491 | 2025-09-04 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 28b36a57-62e5-3af1-a925-0905d1deabca | -11.5779 | -52.115 | 2025-09-04 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 183.5 |
| e2b35c14-5abc-3d72-9ff9-ae7a1d55a0ec | -6.7992 | -45.6815 | 2025-09-04 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 10202e07-2754-39a2-a2e5-ff3f29d8dfaf | -7.7036 | -48.7587 | 2025-09-04 13:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 104.0 |
| a7957d73-73f8-3a9f-9200-d4043c12fabe | -6.2318 | -42.4278 | 2025-09-04 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| f8e34c96-310d-3c5e-964d-9bbf926dfa07 | -10.9867 | -45.9325 | 2025-09-04 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 02d47bd0-38bb-3819-87fc-a1d59d62b205 | -13.8651 | -47.9734 | 2025-09-04 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 133.9 |
| f48af6ad-6a77-3c54-b8d9-aa1840d87dd2 | -5.7002 | -45.156 | 2025-09-04 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b3ab2aa4-ad38-31b1-9fe7-2d624e5804d3 | -5.6813 | -45.18 | 2025-09-04 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 45ab608b-0a5a-3f05-bb6a-92a2b87c2fc9 | -7.6849 | -48.7602 | 2025-09-04 13:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1ed4cdaf-b98b-3c75-b07f-b2fcd9872dc9 | -5.6777 | -45.6089 | 2025-09-04 13:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 3bece59c-c19b-3dc7-bdda-e16ab6104148 | -4.9049 | -41.7696 | 2025-09-04 13:30:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| c061b07d-0b84-3ec1-b696-c1eb01e84a52 | -11.6525 | -52.212 | 2025-09-04 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 1ed01402-83be-3aff-9ab0-f831d4cc2585 | -6.2127 | -42.4532 | 2025-09-04 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| ab2d94b0-9811-3ada-aaf9-fa9f2d91fc78 | -5.7 | -45.1786 | 2025-09-04 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 0233a2a4-e59b-318c-8c63-a366340e9ce1 | -8.3644 | -48.3116 | 2025-09-04 13:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ee838d45-261c-349b-959f-f4b91ee4c93f | -10.4658 | -50.3907 | 2025-09-04 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| ce8ab391-a90d-381d-8355-d5afc0c818b6 | -6.0232 | -46.6784 | 2025-09-04 13:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| fe4d4624-892c-3ff2-80a1-3272156021c4 | -21.7038 | -45.4179 | 2025-09-04 13:30:00 | GOES-19 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.1 |
| ddceed29-d037-33ea-b41d-b7e34d6facb5 | -11.5281 | -54.4806 | 2025-09-04 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 59704679-a83c-32f8-8546-edb0e4385bf3 | -8.0799 | -45.339 | 2025-09-04 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 131.5 |
| d051d189-4019-3020-8c76-b38e289ce131 | -5.9257 | -51.9599 | 2025-09-04 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d2e2cffb-29cc-3b30-9a95-9f9325df03f7 | -14.5852 | -53.0268 | 2025-09-04 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 89a452a8-a2c7-3542-94e5-2408db4322d6 | -5.0135 | -56.2553 | 2025-09-04 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ef8608fe-bfa3-3132-8e44-907333998e03 | -5.6963 | -45.6076 | 2025-09-04 13:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 8b08eb30-dcbc-3cd9-8eb3-c65e67f2f7c9 | -8.0417 | -45.3882 | 2025-09-04 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b314477a-60d6-3cab-a7b0-13411517fe29 | -10.1454 | -46.265 | 2025-09-04 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |


[Clique aqui para ver as próximas entradas](README106.md)
