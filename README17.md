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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec8b64f9-3d18-34bd-9f49-04a6226263b3 | -9.6349 | -46.60186 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af2dd51b-ed35-388e-b5ac-eb4ccd1b86f0 | -11.0192 | -47.05047 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a66b025d-4d55-3d76-8e65-229f5206e464 | -10.60273 | -44.33055 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 0b77e42a-fea3-3047-88ee-99e1144b2490 | -11.04254 | -45.14035 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| a111ea25-4f96-3c3e-8c91-3ddf5d10b114 | -7.46214 | -44.82523 | 2025-09-01 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 520026e9-9263-3d6e-85c8-f1a7552d1a78 | -12.62502 | -45.54888 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4c10a17-52d9-31f2-8637-a0a127831c34 | -8.47018 | -45.16985 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3cd723e-ef12-3b72-b947-0b203c95865f | -12.80736 | -48.07933 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8ce9582c-102e-373d-9913-b87d7797e544 | -11.65303 | -44.86274 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66327d51-2e71-3642-bdfe-29b38c9794a1 | -12.57646 | -48.20935 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d3f2b68f-05c1-3fd2-a1c5-a81ed16c04fb | -11.45311 | -46.81893 | 2025-09-01 03:45:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9601314-b99f-31b1-a0fb-3adecd14be40 | -8.19609 | -46.76778 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a06676db-e173-3bf8-a443-a0bea4c68e37 | -12.39025 | -46.47187 | 2025-09-01 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f693824f-11b8-3cf1-b7aa-022a82279f37 | -10.05144 | -48.10419 | 2025-09-01 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 769d2cd4-7265-3a41-8a21-1a9a48ec48f1 | -8.84356 | -47.50952 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 50a4a3d2-943e-3496-be83-2c81c6303601 | -13.47499 | -46.93808 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7e3a5e25-ad28-39fd-810f-1bcc637174bb | -11.87232 | -46.73615 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aba80608-8325-3f8f-92c9-5cee8a34ff8a | -9.15218 | -45.22088 | 2025-09-01 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2bf8a22-7d08-337b-9b69-0a5386aa48df | -12.81432 | -48.07576 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 903cd3d7-f9bf-3b72-ae5a-7e6457e82579 | -11.95856 | -45.79911 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 173bd0dd-bd11-3965-a35f-07fcfee0ce61 | -9.27379 | -47.11192 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37c3aadf-5412-360d-962c-a893dec43c0b | -13.48827 | -46.98567 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b1c48fb-d3e3-322b-864b-eb48d75f2e75 | -9.53093 | -45.84119 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd1af11c-309c-3a30-8cb2-1cbf942efd31 | -11.03744 | -45.13934 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 1f70167a-7e83-3a6b-99a6-2137d881497f | -12.85198 | -48.07393 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 83468114-26d3-331c-bb02-daff0dd6c1f8 | -12.576 | -48.20641 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e939e17e-f015-33b6-9e8e-bbc0adcf959b | -13.99719 | -46.3166 | 2025-09-01 03:45:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 03fa0031-5144-341d-b214-fccb99265911 | -7.63217 | -44.03254 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bb967d3-9205-3ad2-9c85-aa33a5ff3c5d | -8.3361 | -47.44329 | 2025-09-01 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25ffaa3e-aaea-3128-a811-982a4d05357c | -7.88302 | -46.9918 | 2025-09-01 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 813ad082-bae8-30a2-95e1-f92e675e7883 | -13.69274 | -46.8759 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99d40e7e-6c95-35d0-9748-daf37cf39c3d | -13.66454 | -46.93261 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d022e22b-4fd4-30c6-8a14-38ffcf7213e5 | -14.22734 | -48.06074 | 2025-09-01 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92461b44-af1b-384c-ab0a-d7d1d3db086c | -12.58206 | -48.20757 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b0aea2d-b98e-310d-a5a5-8af2e052dd95 | -8.84508 | -47.79879 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df14a9d6-6484-36ee-9a56-c4f3d62e5301 | -11.08865 | -44.62148 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16b806bd-f835-35dc-acb6-ca6fc9da2de8 | -13.18293 | -45.28006 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92f98243-358e-3aad-b024-a73340e00a0a | -11.02608 | -46.95364 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27f306c9-2113-345c-8667-f8a3519e92b6 | -8.20208 | -46.76872 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 1dcda617-c24b-3e26-9126-4f85f56cb7dc | -9.63454 | -46.60075 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0083617-b122-313c-a4cd-2d5ba637010d | -13.69081 | -46.9172 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68a347e7-0cc2-332b-8614-95100cc78bb8 | -12.31193 | -45.67987 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| dcf00e21-9f25-3710-b914-295db57cfe1b | -11.32292 | -43.47409 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0d5b722-550a-37d4-a70a-06f568108a0b | -8.19557 | -42.30104 | 2025-09-01 03:45:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4da03d53-eb6f-3235-9c7e-9d38ef2f4c4c | -14.00236 | -46.31796 | 2025-09-01 03:45:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7302cdc8-a530-365c-bbdc-4bb3c9f988a8 | -13.3419 | -46.97697 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b9e5a6f-c734-3a3c-9a6e-90117c8b8e79 | -11.877 | -46.74198 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ebeaae72-0c3e-3ddd-9237-4293fb2b599a | -13.47848 | -46.97989 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fce3f230-a798-3e16-b999-eaeb2961c451 | -12.8244 | -48.07472 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7696463-835f-34a7-9342-8373ef1f1e07 | -13.47064 | -42.47569 | 2025-09-01 03:45:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 79b1e797-06e8-35e2-859b-28011aa8e6c2 | -10.57983 | -44.85456 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27351755-ef14-3849-b386-0faa13c1431d | -13.57883 | -46.93273 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dde146b-9ef3-3217-b0e6-2285440aa615 | -13.17132 | -45.28688 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| fdbad349-6aef-3768-b20f-96a583279d01 | -7.67574 | -42.65638 | 2025-09-01 03:45:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ce36eb3c-d033-3dee-b9db-1ad75af55a73 | -11.08645 | -44.63305 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 572a1ce7-1fb3-3c70-9c12-9e47e609bb3f | -12.59187 | -48.18979 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7227d57-b053-3b34-8686-5d2d386639c3 | -11.03051 | -47.02306 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49ff9a2e-870b-3256-abec-5babe26d1693 | -8.1944 | -46.77699 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69ea4d46-787e-3dd2-bfe9-dd01c1cf56d6 | -14.22811 | -48.05693 | 2025-09-01 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e14c3912-2fa2-3f3b-82cc-b6fe84546502 | -13.48154 | -46.93475 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d317c55-d4e4-3eb4-a87c-4892407098cb | -13.66979 | -46.9349 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9fb831e-1773-301b-97ed-d08c7bc4b616 | -12.8251 | -48.07122 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b52e3c8b-6b42-32be-a7fa-db0f47616b51 | -11.04886 | -46.89762 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 668bff16-cb7c-3815-b0ce-183b679e909c | -7.10839 | -45.34389 | 2025-09-01 03:45:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b54f5028-8fc0-3da8-a812-49574ba710e0 | -9.67954 | -45.89845 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc74a97b-0888-3d53-ad86-92077481186a | -12.79105 | -48.08615 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66af9ccf-3a89-3121-aa99-7e3b808d81e8 | -8.91051 | -40.43947 | 2025-09-01 03:45:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 19e76c76-8a01-3007-9f8f-2b4a1679cee0 | -11.65356 | -44.85988 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34a06c66-3cfd-3f27-a208-f6a7d596d7cb | -11.04606 | -46.97366 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd9d89be-43a0-3f7b-8349-e9310aeded43 | -8.88198 | -47.20694 | 2025-09-01 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b3f7e50f-bd09-3523-9a84-fda250c50dce | -12.31369 | -45.67743 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 98d2cd36-d9e3-31d9-85be-65ddbc564382 | -11.01753 | -47.05905 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 60f5d44c-82c3-3363-a6cc-e94e3a530a85 | -11.20616 | -45.0428 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e56fb028-c050-3ed3-8b97-2bc148aa8017 | -11.37456 | -43.60561 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3eff0c74-52bc-3f70-b0f9-1d945058b495 | -11.02688 | -46.94951 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c41a2d07-5420-3f8e-9381-b59acc598a16 | -11.02826 | -47.06566 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7c10229-a43a-3e05-a09a-8ab7e809a777 | -13.16634 | -45.28596 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e8d0e99e-9b84-3e7b-b6eb-4e7779ee18ef | -8.8269 | -47.49089 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 993c2f25-2570-3301-a545-2aaeb91e0ace | -11.35376 | -43.28117 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e83a5826-b34e-38f5-a0e8-6d4efa75008e | -7.69485 | -44.99725 | 2025-09-01 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65981754-76c5-381e-8a8b-858c89868b64 | -13.17244 | -45.28105 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 14b3a43a-b5e4-37bf-9c85-b855f668dc06 | -7.4634 | -44.81808 | 2025-09-01 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a72d089-2594-316c-9421-62e6fab8c8b5 | -14.16291 | -43.67326 | 2025-09-01 03:45:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e4f4885f-e90c-386d-8af4-8f830991b7a9 | -11.03684 | -45.14256 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 7c3e65c9-e531-3138-aac0-2050e0d79f1a | -13.51013 | -46.99103 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04d15474-41fb-3836-81f2-0e5b1cfdf33d | -11.80042 | -46.42834 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c4cfe8b-576e-377d-b060-943ce48edd92 | -11.02768 | -46.94541 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fc00f41-59f6-377a-a752-beba80987598 | -11.04314 | -45.13718 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 7bd70a01-e945-34cd-b5d8-f1f26b811bd9 | -7.94852 | -46.45494 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b56527ff-7464-3924-9a39-b7aaf657bbbc | -11.37339 | -43.58574 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 38b02f0d-f60c-3bab-9368-d31768a832d4 | -9.64726 | -46.62863 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca7f99ac-6163-3d60-909e-e62d9b831438 | -9.6338 | -46.60475 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c8c621d-27d0-3463-9923-697c1b449d0b | -14.03302 | -44.47426 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1b0b7ad6-e186-3304-8ecc-2b0b3d84759b | -7.94141 | -46.45222 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae23ea96-69b3-32c1-bc01-39cac825eefd | -8.01048 | -44.05296 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65257a12-8dba-3376-9d8a-5f3c5cc304bb | -14.04213 | -44.5937 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a39622b-220e-3568-afc8-f0794b445af2 | -13.48107 | -46.99294 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 112c3ef5-4781-3934-b524-2a4699d21d05 | -9.15969 | -45.21806 | 2025-09-01 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3efca65-4922-3e28-9c8a-71ea1c84b4c1 | -13.17301 | -45.27814 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 91105a4c-fb75-381a-9089-b530ee202434 | -7.62712 | -44.03629 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README18.md)
