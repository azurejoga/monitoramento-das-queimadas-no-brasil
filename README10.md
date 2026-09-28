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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b127633-eb99-39ba-9f82-4413b983876c | -11.4361 | -44.9291 | 2026-09-28 00:55:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fdd619cf-6a9d-3fb9-8f8c-8358d7e035aa | -11.0992 | -50.6833 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca8d4f3-52f6-357f-a672-b28deeff6bbb | -3.1538 | -54.0854 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0c7e6fb-0dc6-330f-8545-2df3a991b016 | -12.1041 | -50.297298 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e995c731-93ab-327a-b29d-bbb29b8866a9 | -15.1769 | -46.142502 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2b7ff72d-2572-381c-b1eb-ea0164f3527b | -15.1616 | -43.627201 | 2026-09-28 00:55:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1db4c1dc-67bf-3e23-89af-59c1186d9136 | -4.0389 | -54.213501 | 2026-09-28 00:55:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 856c3160-3fcf-3145-8f67-92238ea744ff | -3.6953 | -51.3787 | 2026-09-28 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a7e6d0-c37a-3c50-9737-2959582f5ed7 | -8.2375 | -45.4771 | 2026-09-28 00:55:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0cb5b670-f485-3b88-a922-77a2cc3a3503 | -15.1022 | -53.8862 | 2026-09-28 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7aa4748f-c01a-3f8f-859c-5a3e2cf095e1 | -12.7223 | -47.279499 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7e7eb67-c3be-333a-8007-ed4f0ce5dd9c | -13.0824 | -47.441799 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 501396c6-2f27-3cc0-91a1-680951b7ed5d | -11.4555 | -44.924099 | 2026-09-28 00:55:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0473bc4-11a2-3912-887d-d4c5460f3c75 | -11.094 | -51.334499 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef37573e-56e7-37af-8fea-02a65dd6f11f | -3.4232 | -50.431198 | 2026-09-28 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22c4cf23-c8cf-3e9c-893b-ce7df11b0af2 | -13.8866 | -53.666599 | 2026-09-28 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c761a417-6367-3400-88e9-ad8037eafa82 | -10.0153 | -50.239201 | 2026-09-28 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be3baf88-67dc-3f6c-8620-90ea5d029494 | -12.6777 | -45.0116 | 2026-09-28 00:55:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3045a33c-debb-333d-947c-100ac681375f | -17.890301 | -45.046799 | 2026-09-28 00:55:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b31e5e8b-82d7-35e7-84e6-e2119e49ad95 | -11.3653 | -43.398701 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71092c21-a8fa-303e-99e7-a8bc457b1069 | -11.1385 | -50.052101 | 2026-09-28 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8a2d0e0-f157-3d3b-8855-fc97c23f14b4 | -14.5196 | -48.301998 | 2026-09-28 00:55:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 037d05c9-f841-35ae-8158-c53b14cdb8c6 | -9.5018 | -46.373501 | 2026-09-28 00:55:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 694ed0a3-3584-3e5c-bfcd-ece1037f8a1a | -11.1305 | -50.061798 | 2026-09-28 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7bbfb04-5566-3cd1-8075-3e30b73d4a4a | -8.2278 | -45.4795 | 2026-09-28 00:55:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37953582-7a97-35a1-a884-c6331d30ec55 | 1.6788 | -55.944801 | 2026-09-28 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaace516-f978-3230-a2c2-b26c5795699f | -3.4177 | -48.3451 | 2026-09-28 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 957bbad9-a5d5-32cd-abbd-bb4bf0848aba | 1.6722 | -55.928501 | 2026-09-28 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20e97909-2bba-38cf-ba02-54eefdf4afdb | -7.6738 | -54.848999 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29e19c34-671b-3409-8375-c2ee7bfdf2d0 | -21.136 | -48.580299 | 2026-09-28 00:55:00 | METOP-C | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9749c716-1999-32de-8512-59f30f892d7c | -3.4152 | -48.334499 | 2026-09-28 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b758ca5-8ede-3f44-813f-ff73d5fcae1b | -23.764299 | -51.928902 | 2026-09-28 00:55:00 | METOP-C | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d02534fb-2835-36e5-a185-af27ad231e74 | -9.1541 | -45.6357 | 2026-09-28 00:55:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8008c147-2647-33de-acb3-d613560d16a3 | -14.4833 | -53.626801 | 2026-09-28 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e188ac07-07f1-3e0a-9554-4808ca92c0a2 | -3.4213 | -50.4231 | 2026-09-28 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a752a3c1-da7e-3c0b-9122-e334f96c8e23 | -10.8129 | -57.2202 | 2026-09-28 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| deddc0b9-e55e-3fca-b221-344bdd20e996 | -15.1672 | -46.145 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63f60df0-fbda-3dea-b7c9-392933fafa5f | -2.9169 | -54.1311 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 682a1d19-b85f-3b59-9490-9634702aa156 | -11.2131 | -44.782799 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| afee7490-557b-32c7-a413-1a490b856956 | -12.6277 | -47.273602 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d08686bd-b0a3-370f-b979-62297bcc8ea5 | -11.6891 | -44.539902 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed6244b3-9158-320f-8ad1-f82151a8ce85 | -13.472 | -48.593399 | 2026-09-28 00:55:00 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e4c322fc-e4dd-3a6e-ab60-ba7127abec80 | -13.7126 | -48.824001 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a8804a2-4b00-3e5c-8773-93a846840116 | -3.1456 | -54.094398 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d5e6f6-d478-3a08-888c-65ca82c65799 | -12.1827 | -50.369301 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db9cbcb8-2d17-3203-b93c-cebc551a93af | -6.6987 | -45.631699 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66b7a60b-278d-3344-bf7b-5ab033e7a1e7 | -11.2228 | -44.7803 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a354e356-fe2d-34fe-a7ad-1eaeca5dd721 | -10.9049 | -50.691299 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce576700-113f-3dec-aa94-6113d4451037 | -11.1875 | -44.804199 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0519ea11-f548-340b-80c9-53aa7ac5fe48 | -2.863 | -54.121498 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa8a6d6-6265-3ef8-8b0c-9508c7c1a0d3 | -11.3891 | -43.410599 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98c71793-4047-3089-8be3-15a9f5e545c9 | -3.2682 | -54.269299 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec28a9c3-41e9-3b71-8e3b-1d1fa54cad75 | -11.7146 | -44.518101 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00bd3aeb-78d0-3ab8-8e51-89d568ed5455 | -17.836201 | -44.381802 | 2026-09-28 00:55:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b7d2057e-7b0f-365d-a77f-5b1c4ea19a89 | -11.0131 | -54.1451 | 2026-09-28 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8731ca03-1b58-3116-846e-98255098719c | -12.1924 | -50.367001 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 397abe8c-1935-38ec-980a-0c31ae4d6aec | -15.2964 | -42.756401 | 2026-09-28 00:55:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7d474b1-fc7e-3b9b-a364-34bb19b24a05 | -12.7125 | -47.282001 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83ec63ea-fd2a-3103-bfdb-d80919a22995 | -20.1777 | -48.5877 | 2026-09-28 00:55:00 | METOP-C | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8193885c-7203-3f0a-b63b-e83ab69ea28c | -11.1773 | -49.8643 | 2026-09-28 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3390f482-6505-3ccc-be38-1c8c298a9a5f | -8.241 | -45.491001 | 2026-09-28 00:55:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd3ef665-ce40-369b-8d46-b62828198f51 | -12.3123 | -46.408199 | 2026-09-28 00:55:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a118a082-1aa3-339e-82cb-61c4579aeded | -2.4494 | -49.2206 | 2026-09-28 00:55:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa1c74f-008d-3488-8777-20524cafe296 | -12.8779 | -44.780399 | 2026-09-28 00:55:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccb1709e-ca28-32e1-af01-f5f7fe064e9f | -11.0417 | -54.041599 | 2026-09-28 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d63d3e7-c6ed-3db1-9d54-939ad8837b93 | -11.0643 | -49.470299 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4115a1e9-d17a-3a58-bfd9-be931196a995 | -11.7836 | -51.057201 | 2026-09-28 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74b0113c-233e-3908-abf6-177d5d33dd3a | -11.0956 | -51.3414 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d26d52d-3220-3c0e-8442-d19b650689b7 | -7.8892 | -45.4445 | 2026-09-28 00:55:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d7d41a32-7d32-3d26-8cdf-0b2d9245b5d4 | -2.9974 | -54.753101 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 543c92b0-c721-3db0-ab78-c356b640d521 | -12.1565 | -50.345299 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 645535d9-da87-3591-b81a-42d9a9d48c92 | -8.9001 | -46.194801 | 2026-09-28 00:55:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26bdfabd-04ce-3a3e-8da1-c0bffac1044e | -3.2171 | -54.316898 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 921942d3-1c3d-34ea-8cda-410a8983a742 | -20.187401 | -48.585201 | 2026-09-28 00:55:00 | METOP-C | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5a3b23-c2b7-35b3-985f-3a822545db20 | -2.2658 | -57.010502 | 2026-09-28 00:55:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 691e42fe-cc90-3acc-9a9f-ccf074e81dc4 | -12.7357 | -47.334999 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98fab1a8-8b08-3743-940d-be1a673b58cc | -10.4194 | -53.830101 | 2026-09-28 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c733e3b7-34c0-3ba4-a732-80c75d70e50d | -12.1941 | -50.3741 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25eed0ef-1355-3855-8cde-a8f6e8a4ac72 | -8.6608 | -43.9174 | 2026-09-28 00:55:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a73bb71b-19dd-3111-836c-ba4889b761ae | -14.5234 | -48.318001 | 2026-09-28 00:55:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8cef6358-9e66-3e6d-baad-62249aaccb2a | -9.9832 | -50.145901 | 2026-09-28 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40e10eb9-a2a2-3751-8019-8e316d0fd511 | -13.3795 | -51.319199 | 2026-09-28 00:55:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d06e0e4e-b89e-311a-965f-94a493b60867 | -10.8779 | -43.671299 | 2026-09-28 00:55:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 572d85da-1498-3af7-954c-34dcd874b112 | -13.701 | -48.818699 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7709cc93-d52b-3df1-a062-7db8db1fe43f | -3.0729 | -54.4072 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65ba438c-a204-39b6-85a8-44e7c8c00d26 | -3.9395 | -42.563999 | 2026-09-28 00:55:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d626b63e-e0e3-3c6d-a63d-67ef80708369 | -13.0626 | -48.916698 | 2026-09-28 00:55:00 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4079bc8a-2fd9-32c4-888b-ef88cdf8d972 | -12.6923 | -47.326302 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efc6b791-febf-3ca8-9bff-515eb12ffd13 | -12.6898 | -46.976398 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5ddd774-bf11-3fcd-8302-2b9a20fb4335 | -12.1467 | -50.347599 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ddacf26-9f2b-3d08-80c8-ce366d0f697e | -3.157 | -54.099098 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b152139f-e69f-3f0e-a7a6-713c2d8b5438 | -12.2055 | -50.378899 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e83a97f8-5d00-3f88-8635-7bda02d58cd5 | -2.9596 | -54.0928 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58a470c7-6152-3a59-b168-d34219ce60ba | -17.829399 | -44.396099 | 2026-09-28 00:55:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 20be112f-e4d3-30dc-a23d-dd8057874b18 | 1.6461 | -55.907799 | 2026-09-28 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cabd76f8-7d5b-3ac5-9617-27b635c935d4 | -8.6564 | -43.899899 | 2026-09-28 00:55:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| edfd749f-289b-3616-a5b1-bcd7d99b1a5e | -15.104 | -53.8946 | 2026-09-28 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e144990-c6b0-390c-a943-fbf1523fcafe | -12.6585 | -47.315102 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93d3e1cd-1bd8-3de4-962d-86d01ab37491 | -10.8152 | -57.2314 | 2026-09-28 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46cfad67-24db-353f-9aca-1fb130222eed | -10.4046 | -53.810001 | 2026-09-28 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
