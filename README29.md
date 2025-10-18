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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d21af466-26eb-3229-9447-3febad787ef8 | -10.23104 | -46.70838 | 2025-10-18 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b054004-c63f-37ce-9978-94021571ddec | -7.66343 | -44.64287 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4cac977-3da9-30fa-8669-67edd3d6b3e6 | -12.43051 | -47.79038 | 2025-10-18 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc0157cb-d987-3f7e-9ae5-b8899c86f5b4 | -7.07114 | -44.73428 | 2025-10-18 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55bb1cab-2fb8-3854-ad34-3dad3f89c1a7 | -11.60541 | -44.0866 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e04c64e9-4ceb-3b13-a7df-54982384eab4 | -8.7906 | -47.93834 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cbdf041-c949-32e2-8124-b5d32a27908a | -8.16518 | -47.03478 | 2025-10-18 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7015fd69-9a1e-39c5-90ee-2235c3b811bf | -13.23804 | -47.09866 | 2025-10-18 04:02:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b353fab-969e-3784-9b2e-fe2eedbd13b9 | -8.2367 | -44.00885 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9aa62bf-df13-33b4-b469-ecf84183ea13 | -8.09107 | -45.44576 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 724ebd11-744e-33e4-9053-fb3b54c3235b | -11.36176 | -44.28383 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef5d43df-ca8c-3b9f-b0fd-a5b595fa1204 | -12.46093 | -45.46697 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0154a81-089b-37f3-bde6-ee9bc6a106bb | -10.49189 | -47.74104 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d649720-cd8d-313a-86ac-ac6c7bf0ed8d | -13.73922 | -48.32804 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dd66445-a6b5-39cc-9da8-6cb2636c832d | -12.65327 | -43.45244 | 2025-10-18 04:02:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c01f3922-6d70-3e60-b151-a4526634cca1 | -8.29485 | -43.39173 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 68b8cfbd-283b-30bb-aa57-b6704a9496d0 | -10.7051 | -44.54845 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cd26d39-94d2-305a-8357-d55d8074a1c3 | -9.75469 | -43.96323 | 2025-10-18 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1b4c00c3-f2dd-3d44-a726-b0563bbd576d | -6.4318 | -47.29729 | 2025-10-18 04:02:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc492313-48be-327d-8ce4-807d85824b50 | -13.24224 | -47.09909 | 2025-10-18 04:02:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f63d717-c9c5-33f9-9836-728e4704c1cc | -6.88819 | -45.4571 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b75abc3b-7a5b-34ea-ba3b-e59d861056a7 | -10.48825 | -47.73515 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0f1c965-3611-33b0-904d-3fff0fe98d95 | -13.7779 | -48.23737 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aab3f895-fb5e-347c-9fe5-b23994ff08b1 | -11.64274 | -47.86122 | 2025-10-18 04:02:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b66cf6d-a801-368f-bc11-bc5f39f39b17 | -8.10793 | -45.44446 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 055b5705-ec57-31d2-9077-96af90a89965 | -10.5339 | -43.36293 | 2025-10-18 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75f1d4be-c9c4-396f-880f-25d645dc0020 | -7.16652 | -46.52783 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5b26eae-2944-3cea-8f0a-348f22031f05 | -10.50066 | -43.45548 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1976b8f-5179-3a94-948b-2b5605248acc | -6.93389 | -43.69325 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5d8328d-d5ea-3a46-8cf0-47c3e9569665 | -10.50197 | -43.44754 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6325ca6-6e1e-3bde-aa4c-8d1939690605 | -11.6061 | -44.08248 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f4522d26-ea43-3eff-9035-944f17c0af96 | -12.61089 | -42.40244 | 2025-10-18 04:02:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df374028-ecc6-3686-b03e-4f0216fd6044 | -14.4873 | -44.6081 | 2025-10-18 04:02:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 125d440e-4c5a-3d3d-ba82-80fb8bafe67d | -10.1052 | -44.56026 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b589b4b3-79a3-3a2f-ab1c-1c69340d80be | -10.48295 | -43.43213 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 15180863-9d98-37e9-bb60-71f4087ef470 | -13.0833 | -43.06078 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 66094ddf-6f28-3d1a-949b-2b093b7a39cd | -10.75516 | -47.8833 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1cb68e98-e4e6-351e-b467-df9b3fd4ba9e | -11.00305 | -47.89561 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 692c44f5-867c-39f2-9994-00d66704d049 | -11.94366 | -44.23942 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84bedaf5-7c70-39fc-9335-a9b1b1f29d3d | -9.23611 | -43.41364 | 2025-10-18 04:02:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bccbf984-edfc-34a9-811a-aee8fbfe89a2 | -9.87855 | -47.65961 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fabec7f-6a2f-386e-8d43-dc6644e4af18 | -8.20626 | -46.93044 | 2025-10-18 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bb3d8c4-fcfa-3ebb-a82a-0a14253eac06 | -10.4183 | -44.91607 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c6a66af-c011-3a72-aeb9-73cc8f2f2cc0 | -8.23966 | -44.01389 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 046482c0-081a-3fa5-a8a8-677afb0abcf0 | -10.14466 | -44.53004 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 396c0100-8604-361e-937e-f6fb7a909e8b | -9.91328 | -40.6517 | 2025-10-18 04:02:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5f0ed42f-f0e5-39d6-a159-c75a5e4d7405 | -10.50263 | -43.44357 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84f01545-e7db-3c04-9788-4277c101bb5c | -11.40352 | -44.27793 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62fd2e1d-3ef3-3876-9060-d864f1dd7655 | -7.99353 | -44.16125 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a89f3d5-25ac-3b4a-bf5e-d7a108a54518 | -8.54486 | -50.07949 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e411dbcd-99f5-30d9-a02a-665e15b37021 | -7.58837 | -44.99377 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7e0a617-2a74-36bb-80e5-94b7db7d6c2b | -11.20496 | -47.8255 | 2025-10-18 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e0abb452-5045-33c2-bf5e-f06c20b59b65 | -7.07507 | -44.73489 | 2025-10-18 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b39e65b-aeb0-3ede-b21c-dfd8743c4ffb | -13.44189 | -48.11703 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9be6445d-94da-36b1-9649-3b64382536cf | -12.15745 | -45.08512 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1706a3c6-ba17-30aa-8a99-96a354efdab8 | -11.60175 | -44.06476 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 87f0d662-fa26-3c6c-8531-364d7e52b1c9 | -13.04119 | -48.19496 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4625b0a6-40bd-3d76-a334-6f7369e92749 | -10.71478 | -44.55294 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5b2e42c-aacc-3806-aa2b-a88a947bcd2e | -10.49715 | -43.45491 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed8f3f1f-b65d-3086-b953-d55bf871d29c | -7.39897 | -44.7492 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fb57e53-2321-3a03-802a-556150cb3a00 | -8.40656 | -46.26768 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6a868efe-6130-33cc-b3eb-62d700b992c5 | -7.21534 | -43.80714 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b51d7d9-4bb7-3434-91f5-541cb9d5382e | -11.58891 | -44.05411 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3a8910e-f937-3b82-8df5-673bcc76c26b | -14.12774 | -44.71355 | 2025-10-18 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbc15808-7839-3fab-a5cb-75cb09822a87 | -10.64303 | -45.31088 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31967943-7c67-3824-8242-88f1e3a2f5f3 | -8.23078 | -43.99877 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60ad7859-024e-3f50-9202-66babbd03300 | -10.9226 | -47.97789 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ada8e8e-a649-39c5-a56b-e8818ea5b18e | -11.14653 | -47.72491 | 2025-10-18 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd633880-0b59-3818-96a3-ecfe2dc2ee44 | -7.33967 | -43.8657 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| afc18c1a-392f-370e-9046-1289d9ab269b | -8.36437 | -46.21059 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c55b68ab-0937-3896-8298-cf6e879e2390 | -10.69774 | -44.54715 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 975b151e-64cd-35b6-bc12-36b2cb5baf0f | -8.19321 | -43.30982 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 588d2ebb-aaa0-35c3-8177-5938d9b7580f | -10.49299 | -43.45831 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d17351de-c823-3653-8c21-b8ae18399aca | -13.76796 | -48.22016 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34351fd2-a2fb-3de0-b978-01445e6d1bef | -10.81181 | -54.614 | 2025-10-18 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 104b87ac-ee13-3f07-afd0-b7353915e2c9 | -7.93634 | -40.97507 | 2025-10-18 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| adf45c52-7bc6-32eb-a903-948f152f52df | -8.33699 | -49.97116 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8427711-de87-37de-b818-53f05de94c91 | -6.75604 | -45.41998 | 2025-10-18 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0707cfe-2e3e-3386-b75b-c5815018e91e | -10.24476 | -44.06179 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38c9a099-e8c0-32fe-8085-1e160e625e59 | -13.18384 | -46.43848 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85b098e3-9164-359f-a567-851d3e469063 | -10.49345 | -43.43388 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fcc027a3-ffeb-37a0-b92f-c0cff6378585 | -10.6273 | -48.01796 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0a21838-6fc5-355d-8520-9b3da66bcfe0 | -8.20035 | -43.31096 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| da3a857a-bbff-307f-82f7-5a2b2a8e7e4b | -13.50946 | -47.99619 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15c6dbdd-926b-3f73-a5f5-d24794762900 | -14.14793 | -44.24424 | 2025-10-18 04:02:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0866c12d-df62-3215-b916-123ba12b9fa5 | -9.25403 | -44.34776 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b783927d-cd91-370c-8141-f25adcc7f522 | -13.52096 | -48.00731 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c1940bc-6bed-359f-b01c-e1508b75dffc | -12.17683 | -45.08391 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a91674ec-cb95-31dd-81f6-c579fff3ca4d | -10.25752 | -44.02924 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e14bc044-ebbc-3783-9505-d5a29ae0523f | -7.14134 | -46.41184 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 845538b5-e9a6-394e-93f7-0f9ad7847a87 | -11.60461 | -44.0695 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| adaaa0c4-b5f6-387e-81fa-d8590d8983a3 | -8.36997 | -46.20316 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7f5c472-4b15-3eef-aa47-8e04a1f4e54e | -12.15854 | -45.06815 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 659d8379-6bbe-311f-aa08-8d95679e8446 | -8.5558 | -50.08153 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93de35b0-ef18-3adb-8400-00468ab591ef | -11.15175 | -47.72144 | 2025-10-18 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e413765e-8b0b-3d06-b748-06ffde2160f2 | -12.42974 | -47.7947 | 2025-10-18 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80775453-33d6-30f7-b523-fc14cf0b49d1 | -10.50027 | -47.53485 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a66bb4b-9998-3e1e-93fa-5c1aed1e3c3a | -10.57966 | -47.39081 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4195fb1f-0d7a-31d8-b3f2-55624009d853 | -10.98341 | -44.32346 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9ab1b97-0998-3fa9-b2cd-d821e368580e | -9.24463 | -41.13945 | 2025-10-18 04:02:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
