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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc697e29-3952-3c47-81b7-d975ff5885b3 | -12.0694 | -48.5377 | 2026-09-30 14:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c1e9ce28-ab07-36a4-8a3b-2be9e14651ba | -9.9959 | -50.2462 | 2026-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| bff94d8e-7155-3649-addc-9f50f5f193d7 | -9.997 | -50.1607 | 2026-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 51df7225-ae26-38b3-a56e-ab398b100591 | -11.5199 | -48.3218 | 2026-09-30 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 4cc88ef6-f94b-3563-b355-7c6eada6fd48 | -9.2237 | -45.8527 | 2026-09-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 1c49420e-85b9-3b8a-bdd4-e5e33be168ef | -12.4355 | -44.1262 | 2026-09-30 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 385.7 |
| fe79c928-5e2b-3554-8292-3f0824c673e8 | -14.3348 | -44.9017 | 2026-09-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| f7d0d8b9-d0ca-342d-94a2-bec24035447e | -6.8762 | -43.7083 | 2026-09-30 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 8050d706-01c1-3116-84a6-204f8e2eae0b | -9.9956 | -50.2675 | 2026-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 237d8e56-3b1f-3ec0-9f8a-69b14482a819 | -11.6588 | -43.5425 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 7709ef4f-00c9-31a3-89f7-3fe495bb21f5 | -12.0694 | -48.5377 | 2026-09-30 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a834a09b-600a-3013-a6f9-f76ef2ca76d6 | -11.7182 | -43.4386 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 259.0 |
| 6128235c-de36-3507-8d77-953acb9adbe4 | -10.2827 | -49.9606 | 2026-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 21cea570-23d6-3cd5-9efa-9ae6656eb233 | -7.055 | -42.849 | 2026-09-30 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 1e681864-2a2e-3be9-8eb9-fc0ad1048a8a | -11.6592 | -43.5188 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 7e4b3952-1677-39a6-9bf7-84b9f4c126f3 | -14.3348 | -44.9017 | 2026-09-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| b0cbd403-4e89-3ec3-907e-eee7c7967432 | -4.3516 | -48.9713 | 2026-09-30 14:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| a474cde3-71a7-346d-beba-52e3e3d001da | -6.8864 | -52.4821 | 2026-09-30 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 905c63ba-270a-3ab3-844e-9fb1475bf03c | 4.1884 | -60.63 | 2026-09-30 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 73f3b361-ba75-3be6-868d-a9790c53f9db | -11.2095 | -45.1478 | 2026-09-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| de5fd171-a267-3217-b111-3c74b77048b4 | -11.64 | -43.5218 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 331.3 |
| 7f47fd23-46ad-3872-a2c9-f80a1803223d | -7.4918 | -45.8018 | 2026-09-30 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ab27c18e-78e8-303d-acfc-9e8c73bab2ce | -9.0249 | -49.6334 | 2026-09-30 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 4cc231e1-b5cf-3e86-9693-d4ee65217e83 | -13.3641 | -44.0166 | 2026-09-30 14:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 27b7948a-f84f-3651-91be-c7eecdcc5ff6 | -12.4351 | -44.1497 | 2026-09-30 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 277.3 |
| ffea7bcf-8be4-3b24-97ff-a9a1048ae7c4 | -12.6082 | -47.2429 | 2026-09-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 58ce728d-f8c9-3591-9709-f9d08a9901fe | -7.4733 | -45.7809 | 2026-09-30 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4f944fa4-0c3a-384a-9b4e-ec6dba946f4c | -7.0612 | -42.3035 | 2026-09-30 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| d43a9f14-a2ae-3704-bb7b-44e83147b3ea | -13.3835 | -44.0132 | 2026-09-30 14:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 254.2 |
| 4657b696-d5e5-319d-93a8-166d36cb3e3d | -9.6657 | -46.7024 | 2026-09-30 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 1309fe31-9b3e-36d5-b5f7-22ee746af624 | -7.2564 | -43.3462 | 2026-09-30 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 5a452d89-43a5-3d70-a5b5-6ca8f03a6467 | -10.0331 | -50.2851 | 2026-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b4dece29-2fee-3d03-8ea5-af4a098c8962 | -10.0895 | -50.3009 | 2026-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 6169390e-b637-340a-ab32-6eb08dda315a | -11.1767 | -44.8296 | 2026-09-30 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| da00d31d-792f-3cd1-a27b-24fc9239a2f3 | -11.2758 | -43.5303 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| beed5d1a-a3f6-38b3-a24b-24814900b139 | -10.0892 | -50.3222 | 2026-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 8bc23ff3-a9eb-399b-8457-deb615bfcd97 | -11.699 | -43.4416 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| af97f71e-5589-3a7a-951e-d7e07f59e45f | -7.506 | -44.5503 | 2026-09-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d85c9eb8-a78e-3849-90f5-120662598f0d | -11.3743 | -43.3734 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 37c365ef-ef4e-3de8-ba65-57b593c1853c | -13.3646 | -43.9929 | 2026-09-30 14:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 297.1 |
| cb9e8c10-ca96-3f9b-a473-15ae9bbeb861 | -7.3965 | -42.6498 | 2026-09-30 14:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 1e7ca951-c7c6-3841-837c-a3b9d7f94c00 | -10.2843 | -44.6274 | 2026-09-30 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 988ad2ea-d244-3fa9-8048-a891a4601649 | -11.6207 | -43.5248 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 51f91b0d-248a-3077-8dae-39a749ff2b9d | -6.7062 | -45.6216 | 2026-09-30 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ff61e321-0404-3c75-a56b-8495575b30c7 | -6.9419 | -42.8598 | 2026-09-30 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 20e579fe-e7d3-3367-9b1d-e17de68405fe | -11.6212 | -43.5011 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 3f2708ac-83e8-31ff-bfed-5df60565f0d1 | -9.0652 | -45.0062 | 2026-09-30 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| d0d6a40e-4395-39bc-b35e-9f2f7934489b | -4.1482 | -48.8948 | 2026-09-30 14:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| e6f3aebb-d72c-30a7-8f0c-96595721cd65 | -5.7873 | -43.7758 | 2026-09-30 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| d3f6d397-0216-39f9-8b4d-8dce0b4a8306 | -8.0358 | -42.8423 | 2026-09-30 14:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| d6234008-5c28-3c28-a6d7-960f3e15f8a3 | -7.2561 | -43.3697 | 2026-09-30 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| d85b35e3-9cac-3bf8-afb0-4be29b661537 | -15.1309 | -40.988 | 2026-09-30 14:30:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 141.1 |
| 3af19f7c-1a43-3c76-a8b5-78015ff4e638 | -9.4813 | -46.3646 | 2026-09-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 1533c8dd-598e-3e25-b72d-4f915ac92dc0 | -9.0437 | -49.6317 | 2026-09-30 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 882fbbab-9d70-3b8e-a007-521f18a496d2 | -8.0169 | -42.8444 | 2026-09-30 14:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 177.8 |
| b64bfb77-1b9b-3434-8cd2-cb111195e946 | -9.6654 | -46.7248 | 2026-09-30 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 0139c880-c172-3c41-9a1b-17a1192b3006 | -6.7254 | -45.5749 | 2026-09-30 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a49297e0-77f9-3e37-b72d-fd706d4c3100 | -10.0145 | -50.2657 | 2026-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 208d1b96-e475-37e3-b41a-c64aa483f455 | 1.7115 | -55.9221 | 2026-09-30 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 863be66e-2654-3983-bf43-b50eab888a29 | -11.3555 | -43.3526 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| efdf2d5e-b438-3cc8-a34a-96bb9f6a5fd3 | -11.2566 | -43.5331 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 53d3999c-8af3-3154-a080-a05cd2a57286 | -9.8617 | -44.9347 | 2026-09-30 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 168.7 |
| b237d06b-f071-3a26-b908-ddf2bde99552 | -16.9203 | -42.1171 | 2026-09-30 14:30:00 | GOES-19 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.2 |
| cd45279e-96b6-32d3-8d49-8fe298531878 | -8.3397 | -44.1658 | 2026-09-30 14:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 2cfc0755-ef3a-331c-ae3d-f8fabb6ab184 | -7.0547 | -42.8726 | 2026-09-30 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 38a5d726-09a3-3ea9-a98d-8fae9b71f85d | -6.1402 | -53.0574 | 2026-09-30 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| fb05867e-608f-3944-8ab1-65a3cf364685 | -10.0703 | -50.3241 | 2026-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 01a619a1-ed80-3ee1-b49f-fd007954be41 | -7.1391 | -43.7305 | 2026-09-30 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| b3ce9f79-502e-3fac-b629-75412f08155a | -11.6395 | -43.5455 | 2026-09-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.0 |
| 5f9a9f8d-7d12-3d8b-999b-e6d067759f26 | -10.6035 | -49.9913 | 2026-09-30 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| bf2e3c1a-44b0-3bf0-8570-14636c390230 | -13.5344 | -49.1731 | 2026-09-30 14:30:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2e379c16-1c0a-30f7-a025-4e861e5bb284 | -7.1091 | -43.0557 | 2026-09-30 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 0de8889d-3ee4-3fe1-991f-cad170c70ed3 | -8.9147 | -44.9544 | 2026-09-30 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| e1f4feab-619e-3460-8ddd-736f4105b1a7 | -7.2755 | -43.321 | 2026-09-30 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 2ff0711f-54f5-3a91-83e3-94aa134e33bc | -8.3208 | -44.1679 | 2026-09-30 14:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| ac02e3a0-d3ad-3c63-81ed-d3328be9c373 | -17.5338 | -43.7135 | 2026-09-30 14:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 139.2 |
| cb1e4f79-9841-321d-b705-a4c38dd1c4ac | -7.5057 | -44.5733 | 2026-09-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 307c4931-46b3-375a-8dc2-9f7fba8e083b | -8.3805 | -45.3994 | 2026-09-30 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| f6975950-0a99-33d9-b7e9-c707afbb764e | -5.9889 | -53.5335 | 2026-09-30 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 82548162-0643-31e0-959a-6ebeeeb08013 | -9.2229 | -47.3285 | 2026-09-30 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 7dfbd065-a46e-3615-a363-1b9dd5664fae | -11.7178 | -43.4623 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 8d8980b1-9b16-3fbc-81c7-28d5564599da | -12.5329 | -43.091 | 2026-09-30 14:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 179.1 |
| 21451690-2dea-31ff-a154-e1b8c86c7dec | -12.7618 | -47.2431 | 2026-09-30 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 2e767250-c541-3334-b99a-fe1760df860b | -11.3743 | -43.3734 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 801bfa7f-38f2-33f5-aa93-4ad9b3f8915a | -11.64 | -43.5218 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 6b144c4b-a3db-31a0-a6fa-fb38dccdae54 | -8.0355 | -42.866 | 2026-09-30 14:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| 9931fc61-32bc-3b72-965f-28875d023e7b | -4.1482 | -48.8948 | 2026-09-30 14:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7c8e9744-c34a-36df-acb5-231083142da6 | -11.699 | -43.4416 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.0 |
| ec3918c6-7efb-32ff-b921-ca406d4a73d4 | -3.785 | -47.5065 | 2026-09-30 14:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ecc4eac9-a429-3b91-9dc0-66963873c49c | -11.6207 | -43.5248 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 106eb931-8213-32e6-baf4-33d34735a366 | -11.4106 | -43.4862 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 354.7 |
| 8a7c8099-992d-3b9d-9b09-4d4323029a50 | -4.3516 | -48.9713 | 2026-09-30 14:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 501bb444-5a39-36ae-8806-205b76509ec8 | -8.0358 | -42.8423 | 2026-09-30 14:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| d862bdb9-f647-38ec-bc7e-0c54101ea24c | -0.8399 | -48.725 | 2026-09-30 14:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| fc2e2422-4692-35bc-9648-18451b02ca07 | -12.5334 | -43.067 | 2026-09-30 14:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 159.4 |
| bb2b6af3-3923-3c2d-9172-88e4272593fe | -5.9887 | -53.5538 | 2026-09-30 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 4b1f7caf-5f79-308b-9702-56887dbdb556 | -10.2843 | -44.6274 | 2026-09-30 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| a920b636-ee3f-3c6d-9a90-b4e72ddb8bc9 | -8.3802 | -45.4221 | 2026-09-30 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 62ce2bf5-57eb-3d60-86e1-422e5b7d69b9 | -7.1091 | -43.0557 | 2026-09-30 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 99626dc2-ee61-3039-8081-7d4695297bc8 | -7.2755 | -43.321 | 2026-09-30 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |


[Clique aqui para ver as próximas entradas](README72.md)
