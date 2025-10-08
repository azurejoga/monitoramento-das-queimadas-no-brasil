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
| 9a009a68-9f81-3e81-957f-736e69243c33 | -4.57863 | -41.29729 | 2025-10-08 04:17:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bdddbe99-1597-303e-9143-615c9fdc7b5f | -13.36783 | -47.22866 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cb64627-8b06-3bdd-98f8-bc84ac4656b1 | -11.78128 | -45.10167 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ba3b39b-bd15-3e89-93c9-086c26505f46 | -10.42638 | -45.38069 | 2025-10-08 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f343092-c905-3641-86f1-411b86a58823 | -7.44585 | -43.13363 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e6f11404-6643-311b-879d-315369080128 | -10.48065 | -49.37236 | 2025-10-08 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 538532da-ce6f-312f-8b03-0f06e0003364 | -3.34832 | -42.32874 | 2025-10-08 04:17:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f5f3a14-2e0d-3ff1-9406-bee99e23ce61 | -11.73171 | -50.93727 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 18edc0f9-b4e6-317f-8e26-1b8d4fc33222 | -12.71492 | -44.37446 | 2025-10-08 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 571e3395-e482-3cc9-8f87-12d2bc29c4a1 | -5.32066 | -45.25695 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e811aea-0e60-3b05-bed8-42d42375e38e | -7.47796 | -43.10299 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 85d48140-39e7-3011-9d7a-cbbdea8e1a68 | -12.02597 | -45.20385 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 929b5f9e-6359-3895-8d23-a8bab23fed8e | -11.17408 | -54.90335 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5de751ce-d7e8-3d24-b152-f43ff2edee74 | -11.14931 | -54.88279 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c79edf0-d4d3-31a5-ab67-d38869c7fe93 | -6.05116 | -44.30914 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4923e91-ba12-3eff-bc4c-50c1c5344798 | -13.25827 | -48.04939 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbec1a6e-6b0c-391b-a4d4-adbb73dec0dd | -10.90923 | -47.13563 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ebfd8ac-2fd5-304d-8e43-1a67fa334ade | -13.02113 | -47.90568 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed18af1f-aab7-3a4e-9a7c-b01394f9696c | -7.68628 | -42.401 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e40761cb-16a2-3692-bed1-ce50ef5e9b8d | -6.75654 | -43.76675 | 2025-10-08 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d94e6d75-0d0f-3e96-90ae-cc0d60ff4be5 | -10.91162 | -45.70377 | 2025-10-08 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e58ec8a-d3f2-3995-b20d-b8c8bf342262 | -11.17578 | -54.89478 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ac190442-607f-3301-9ae4-5fafc4642dbc | -13.36934 | -47.26263 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d86923c2-f63a-31ab-8b00-3f4c655f3ffd | -3.38781 | -50.14304 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e86275ca-6d5c-366c-ac05-9c5b3104f024 | -11.16332 | -54.89668 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb3a7a67-2cef-325b-8565-2a53e9d1b8d0 | -13.35654 | -47.55522 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b8ac52c-f749-3eba-bc61-e8a94f22c5d7 | -13.27045 | -47.5662 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51dca46d-f5a5-3bbb-92f5-e997b0ab5bc7 | -4.85383 | -45.66365 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37badbcb-1e99-3577-a4ca-174311ee8413 | -11.1742 | -54.87241 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8f3f95b-a392-34f8-ae20-efd0df35315b | -5.03918 | -43.60896 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 44097cf3-2191-3dae-aa2d-e392018a22af | -11.9917 | -46.77523 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2bba4f64-df0f-3afd-b415-6e55a08b35be | -11.14316 | -47.74518 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48074c71-1b9c-30ac-b306-a3be742c644a | -13.06637 | -43.59151 | 2025-10-08 04:17:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 275e1f71-a455-307b-a58e-780d483aa403 | -5.17496 | -45.12917 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 318e1e1e-af91-3edf-bafc-4aef789ae33a | -13.37563 | -47.24668 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e9295af9-b646-38e4-bd95-bf519add9cb1 | 0.92502 | -51.12509 | 2025-10-08 04:17:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bf56cef-faf2-387e-8248-19170552270b | -3.55652 | -49.97963 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b94d7e3-b10c-3320-bd46-8300aa378d3f | -5.39058 | -45.20129 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae230f5c-6e0d-3b8e-8436-2863a9d70965 | -10.64666 | -47.80309 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aac713d0-7eea-3a64-98e9-4c45b1451a35 | -11.79373 | -45.04543 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f40e3e3-3d21-3cce-8fdb-296d0794dacc | -7.2531 | -44.11149 | 2025-10-08 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de3a58f1-8180-31fc-bf69-aa0da9a7d1ca | -11.11688 | -54.04941 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfd4d3a9-c122-3319-a413-9813bbeed40f | -1.40909 | -46.70481 | 2025-10-08 04:17:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3f66d0a-ec72-3d10-a111-33d3da7b3468 | -10.37983 | -50.23635 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1945fa3-94e4-3873-a4f9-66a03e922feb | -5.90759 | -44.19888 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28252216-5f29-3d19-939c-a3d8b796e5a8 | -11.78535 | -45.05492 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ccf877f-50ff-3e4a-8a81-a943cf07cace | -5.82908 | -44.97058 | 2025-10-08 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7127f7a-d033-303c-8508-abe100f38f58 | -4.22163 | -46.83681 | 2025-10-08 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c703ed29-399b-3495-b878-0e36c7424d28 | -4.30998 | -48.08144 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 15d04978-e7e7-3ae7-b314-74e2113bec7f | -4.05659 | -42.51086 | 2025-10-08 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f462055d-846c-3a2f-b669-2c97871d7215 | -11.13527 | -54.89295 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c057e80-85cf-31c3-9910-a96d522cba81 | -11.81735 | -45.13345 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01706c8a-499e-3857-a525-ce0ea64d3155 | -7.69466 | -42.39141 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a1d6a955-5db6-3f0c-9ca7-badb70e4754d | -10.38481 | -48.13324 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e833790-8f01-3723-acd0-d43c124e22a3 | -13.37485 | -47.22984 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 693f3b73-e9d9-33a7-bd9c-95409d10ec41 | -7.45415 | -43.12424 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0805a471-162a-3ab0-a494-b68037166ea9 | -11.70328 | -50.99178 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb0cec5b-5b8b-3171-8b00-dd210ca8a1dc | -10.38057 | -50.23217 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2367a70f-7bc5-3d49-aec5-31bc7db11303 | -6.57086 | -44.15438 | 2025-10-08 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08c4997d-1afd-3e54-9e05-f4a191710d76 | -11.87169 | -44.93394 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c884970-6a1d-356f-a650-9ec71eef4782 | -10.22709 | -52.70073 | 2025-10-08 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0b3a09b-a809-3fac-86a3-10591b5042c4 | -3.69945 | -49.41587 | 2025-10-08 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e97c28b1-86ff-335b-bdf1-e936ae9e5b1d | -10.33944 | -51.56164 | 2025-10-08 04:17:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82bd948e-2593-3944-adb4-e74ed78183cb | -10.66812 | -44.14923 | 2025-10-08 04:17:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1da1e4a2-c2e8-3d02-ac1f-c5a479c0ac60 | -4.9476 | -45.59595 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9d02e11-9198-3c21-af69-92a3dc7b5a0d | -12.25064 | -47.86245 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ee6933a3-9e4f-3002-849c-23a89dafeffb | -13.37914 | -47.24726 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 843189a9-94ec-3de4-b986-430c50ef8483 | -7.79337 | -42.61756 | 2025-10-08 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 83533668-5bbc-31cb-a606-5889e735c6da | -7.24074 | -43.9837 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c95886b-59a4-358f-9157-96d0bdd33c16 | -13.0694 | -47.88528 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3fabd99-7789-3c88-a39b-ebe75136d900 | -9.77685 | -48.28307 | 2025-10-08 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81dc0070-f402-352e-b664-c0f2e7125789 | -7.34341 | -43.86714 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f513b5f6-d41c-32dd-91bf-f04b4bf63d86 | -3.85852 | -38.55893 | 2025-10-08 04:17:00 | NPP-375D | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ac56a9b-7647-313e-94bc-cedeacb48f40 | -11.79764 | -45.04243 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a73a9385-96d7-3fbd-ac26-c1a9ce87e093 | -7.35508 | -43.85823 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 91960d73-5130-31d0-bbc2-53efb9f06e3e | -2.89674 | -50.73743 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea0f8588-bd23-3e17-97ba-11defac24927 | -4.49525 | -42.86344 | 2025-10-08 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d2ed56d-aa7a-3a0a-bae6-8b83f154ae94 | -7.47466 | -43.12391 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 774ccac3-edcc-3992-beeb-f71f7586ca18 | -5.88918 | -45.55656 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f25b20c9-bb75-3e73-9da3-d587a87e9cfa | -7.70977 | -42.38284 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5925bc30-e3ca-39cb-9d47-91deb4b0aea0 | -5.26066 | -44.13743 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 015c3b1e-7e1b-3e40-8f73-4893ee111e5e | -6.99673 | -42.86636 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a72c720f-7e4c-3755-9d1c-473a5659ac11 | -7.44972 | -43.13068 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4fd8976-c074-3d2b-87be-ac16fbc3715a | -11.80488 | -45.04 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d4de3fd-c5e0-3d04-bc16-21ec6b565ba7 | -11.29117 | -54.88776 | 2025-10-08 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e21d97bf-a8dd-3427-91b8-9f15587f8c64 | -11.71302 | -50.989 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2fec315c-9600-3ac6-af53-dd0f3141131d | -3.08588 | -50.57667 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4d25ce3-94b9-39a7-9141-f2c8da986b8d | -11.17504 | -54.9059 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 600dbdc3-2933-3047-b6ec-e35cbcbbefc9 | -3.97756 | -42.88121 | 2025-10-08 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8d517e30-c831-34ff-a06f-866af4d29f41 | -5.99716 | -39.31264 | 2025-10-08 04:17:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e99acf77-e092-338a-87ac-7f94d55f6189 | -10.37636 | -48.13685 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6787aea9-9141-315b-b045-e050f139ac9f | -6.66551 | -41.38165 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d02e41f1-5ae6-377a-b15e-a88fd882f8e8 | -11.34197 | -44.88399 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d36668ad-e2f2-3262-991e-fcca153ea351 | -5.74574 | -44.51221 | 2025-10-08 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdb59e03-2fea-3eb5-959a-d38c443b1267 | -3.898 | -44.90525 | 2025-10-08 04:17:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd0fc522-4e3d-392c-b54e-c4552c44dff9 | -7.4724 | -43.09497 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 541581e6-5715-3f71-b61b-5fd9fc25edfc | -5.45484 | -45.87097 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d887a124-e73b-3886-95fe-ef512771abfb | -11.15432 | -54.8881 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b073227-2c45-34e5-a617-283969fd98ec | -11.94035 | -51.46994 | 2025-10-08 04:17:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b771212c-a647-3cf5-90e0-a2af2ddf5138 | -11.38177 | -54.35395 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README41.md)
