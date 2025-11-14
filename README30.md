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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da30f50a-da88-3ff2-a188-8ad705dd6228 | -2.24066 | -46.07756 | 2025-11-14 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53af8b44-a24b-3d55-ae6f-51f3d2886629 | -5.16466 | -37.57441 | 2025-11-14 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0fa749a1-d042-320c-829f-f64f18085c18 | -4.58895 | -44.54505 | 2025-11-14 04:23:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efe7f52c-fad7-31fb-b83f-0aa0235c5f45 | -4.3875 | -42.15249 | 2025-11-14 04:23:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1200dc52-20f7-3a90-8a5f-92e717a34ab8 | -2.17157 | -48.37203 | 2025-11-14 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3700d831-1745-3e59-85d6-9a6dbc49ad9e | -7.72143 | -47.18848 | 2025-11-14 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ef35284-927c-3849-a14a-2bc4f6438c07 | -9.23293 | -45.5876 | 2025-11-14 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f66cfbf-359d-3281-be4f-6567fb48f9c5 | -4.89787 | -42.91031 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f5fb955-027b-3cae-97b5-e172ddaccbc5 | -4.24081 | -42.33286 | 2025-11-14 04:23:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 135097ba-2eec-3487-a5e8-695b6c31fd87 | -3.51628 | -45.55552 | 2025-11-14 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7300be6f-88e4-3950-9a58-55cf09119f9c | -7.06484 | -48.36197 | 2025-11-14 04:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5aa45c80-243c-3817-a82b-b3524a63622a | -9.00674 | -45.45485 | 2025-11-14 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43216cdd-7ddb-3942-9382-68814bd4c8b0 | -10.62734 | -45.00601 | 2025-11-14 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bd236de-5c94-395f-b604-86c793966608 | -3.76621 | -47.7416 | 2025-11-14 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 252ceecf-761a-355c-bac2-02235e7cef24 | -7.36043 | -43.34879 | 2025-11-14 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 727167b9-6f52-3937-bf35-afd9a52794df | -10.31072 | -44.95576 | 2025-11-14 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0139d48b-0daa-3091-842c-d286260a0410 | -4.07233 | -44.13118 | 2025-11-14 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 764a1752-a5e9-3a6e-93c9-16ca7ad78bcf | -7.57647 | -46.62028 | 2025-11-14 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5a5450a-8ebb-36b5-88f1-f461b0748cb5 | -3.36126 | -42.44703 | 2025-11-14 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f4f2723-79aa-3915-85ca-37acfde39449 | -9.66551 | -43.89809 | 2025-11-14 04:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54c68bee-f32e-3077-90b2-cc48d132d79e | -9.00515 | -44.17324 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d94c2a24-4752-3c0f-b9fe-53544ace531d | -1.83384 | -53.80228 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d67033f-a1b6-38a9-a679-cc9bb7ffe86b | -10.72842 | -44.01791 | 2025-11-14 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eb03464-0c65-386a-9597-97f2ece2db05 | -9.44394 | -44.87314 | 2025-11-14 04:23:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 929fb663-6b99-3bcd-9567-e15b4b11eb55 | -4.52846 | -41.10114 | 2025-11-14 04:23:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de542069-0766-31c7-95d1-89e617fd3d89 | -7.92935 | -44.3286 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef22730d-b797-3c70-8b34-55e5cca071d4 | -2.5719 | -54.01133 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2faa8d0-0954-3185-93be-9a1e732a2ccf | -4.10407 | -48.01749 | 2025-11-14 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e2c6098c-ef91-327f-992d-656c6e55c34a | -6.83904 | -48.00603 | 2025-11-14 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29677a25-152e-3443-a3e4-a95b0e506c34 | -4.45822 | -43.91574 | 2025-11-14 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12163b75-ebff-35bc-acb6-5dfde3622e4b | -5.02827 | -41.10058 | 2025-11-14 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 271259b6-f63d-3993-8e6b-9af6e650c687 | -3.46246 | -43.18703 | 2025-11-14 04:23:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a4dbe4c-78d3-34ea-a126-fc1e043ec79e | -7.45231 | -42.5605 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd0ed109-9fca-33f6-a42a-ae9a52a83b26 | -9.95366 | -44.94288 | 2025-11-14 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 186b24c2-b42a-35ab-9384-5d98fdf8a34e | -4.10783 | -48.01809 | 2025-11-14 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c56edef-5036-3775-9d7e-062782eca4b4 | -7.38879 | -48.65368 | 2025-11-14 04:23:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b70e992c-5e82-30ab-994e-3a8492c93b85 | -4.33709 | -45.88359 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3984e08-fb01-37f9-925a-81a1e18e4f53 | -7.89422 | -46.62214 | 2025-11-14 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4456f27-7457-30d6-8a53-e8d298c1e7fe | -10.75643 | -45.01897 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c0ff852-0f41-3f64-b7a5-8cad34221037 | -3.87214 | -42.2361 | 2025-11-14 04:23:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5af139c5-69f0-3a23-8c7c-a2861d9c0157 | -3.74763 | -44.27843 | 2025-11-14 04:23:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e01320a-6611-34f1-99aa-1bd21cd3354d | -7.93633 | -44.32241 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f140cd71-beab-3082-b538-3de4d663e750 | -3.7655 | -47.74599 | 2025-11-14 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ec5f606b-b62c-37d4-a963-f0db419da45c | -3.43076 | -50.16508 | 2025-11-14 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64468052-d29a-3a31-bcbe-ad5fa2959542 | -8.27934 | -55.07627 | 2025-11-14 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a7587d6-0a3e-366c-b974-739e33363763 | -3.24549 | -48.87744 | 2025-11-14 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d949fe3-cab8-3d5f-9ae6-b15e41b4ed8c | -4.01397 | -48.80554 | 2025-11-14 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 082ec8ec-0e77-3ad0-ae58-c171b475b25d | -3.78821 | -49.57348 | 2025-11-14 04:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad6aa25d-ac84-35b4-a6a4-92e255f110cc | -10.26169 | -43.96925 | 2025-11-14 04:23:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d3f06fa-49b0-3fe6-8585-35d8c941aa69 | -2.83883 | -45.48701 | 2025-11-14 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 55694613-1982-3207-9f8f-0a8a64ad41f8 | -3.43371 | -42.42849 | 2025-11-14 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f6729ed1-5721-3b19-9f53-8584efa052dd | -7.35536 | -43.35917 | 2025-11-14 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54e31994-cc4b-3008-a574-ca4380ba95c9 | -4.30236 | -46.27265 | 2025-11-14 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c58f887d-4ee9-3204-94ec-2cc5dff35930 | -7.8899 | -44.31879 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce36e658-9780-3e5f-a805-a84e581ac811 | -3.4264 | -50.16434 | 2025-11-14 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f971f40-bad4-3c43-a412-8eabf34fd894 | -3.81199 | -43.46622 | 2025-11-14 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93485e39-469e-3eaa-ad93-ee603ac0b72b | -8.90518 | -44.44131 | 2025-11-14 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3cbc329-b435-39ca-81b2-c4608dfe9044 | -7.25289 | -46.73907 | 2025-11-14 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecec104b-f539-3a26-9e88-29e64086aba8 | -9.00459 | -44.17681 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e3f66d0-0b20-3095-8e0f-9fe126024a34 | -3.14927 | -50.26637 | 2025-11-14 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e942fa7a-4e59-3745-8b21-087e65b2ab8c | -7.93857 | -44.32995 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e68b57d5-b969-3125-a12c-2aec063fbcc6 | -10.90517 | -44.38973 | 2025-11-14 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c986f50-0d54-3948-acce-a28984a8b14d | -9.19033 | -41.03091 | 2025-11-14 04:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9bc4a291-f90a-33f2-ab19-f774b282b632 | -4.02416 | -43.98568 | 2025-11-14 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dfdb8f0-67fa-3453-a7c6-6edbc3f02b5d | -2.23936 | -46.07809 | 2025-11-14 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42f429bb-f210-3af8-936a-c72145fe86c5 | -7.59932 | -46.38872 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6149d77f-5695-3022-8f32-7794e6b84561 | -3.77205 | -47.72903 | 2025-11-14 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a5ccb3b-91db-3e87-9764-3f47d9722260 | -8.94422 | -45.48418 | 2025-11-14 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d83de44-c644-31cb-bb92-812a2cb863da | -6.8548 | -46.76062 | 2025-11-14 04:23:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4017e419-f9c1-320d-b393-869d1ed39f9c | -2.37675 | -48.67601 | 2025-11-14 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e4b6def-e242-3055-ad34-89fd60b5530c | -1.34101 | -54.60417 | 2025-11-14 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d8ed42e-2802-3f29-b59d-8c33a1273b06 | -3.01168 | -49.4398 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c045278f-61e5-371b-8892-fd185b59010a | -3.35475 | -46.86625 | 2025-11-14 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38140c2e-e205-34bf-8f55-f24dbe0a31c9 | -4.57198 | -43.12415 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0dc8c5e-8293-332a-8da6-005e90a645b8 | -2.51492 | -47.80805 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb32f74f-b181-34e5-bb8e-c7bf9736779b | -2.90078 | -48.05923 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ada929ea-10f9-377e-8c3c-617344d8fa4f | -5.72479 | -42.35505 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| dda3bbc2-4f76-3430-8640-e113493a183a | -5.9767 | -42.59306 | 2025-11-14 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44301e78-4c7c-3def-bad3-ab18a81a15df | -7.33795 | -42.86068 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 74d402cd-75cd-33bb-b73f-490b318c647a | -6.18459 | -40.87561 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c99c8ab9-70da-3784-9e91-5502cb581dbe | -17.63159 | -46.7052 | 2025-11-14 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f7e7603-b6a5-359c-a0a8-e68c96c1f525 | -6.14488 | -44.76358 | 2025-11-14 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8a56e28-b4e1-367a-9819-b65747a7391c | -14.28201 | -42.83667 | 2025-11-14 04:25:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d7655f3-5320-390e-a3aa-cf1f2c75eec2 | -7.11286 | -42.73391 | 2025-11-14 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b3e59b34-38ff-38e4-b1cb-6ec70e28c368 | -13.48668 | -46.71835 | 2025-11-14 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37f8976d-59c4-361b-a089-f6570e762e69 | -13.9177 | -42.88352 | 2025-11-14 04:25:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9ffcd206-15ff-348e-833b-4c6decb7a00f | -12.02205 | -43.73092 | 2025-11-14 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea207c02-958a-32b1-9b52-93089b0d5bad | -12.66851 | -46.75061 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e9a2d78-b69c-3233-8485-2975ab0b6faf | -12.14321 | -48.01997 | 2025-11-14 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1cb23e2-79e7-32d0-a021-e27d4e974c63 | -16.54578 | -49.35711 | 2025-11-14 04:25:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30d39eb7-4323-36fe-a891-8815a7d5c3d7 | -6.15616 | -48.04659 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0fe1ee6f-be0c-3ede-a4e0-19a5ccd3681d | -5.85491 | -47.58434 | 2025-11-14 04:25:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4027cf07-8799-32bd-9f14-01bf9cfb458a | -12.99873 | -43.8419 | 2025-11-14 04:25:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb75524f-85af-3c60-859d-672c125f12a4 | -6.1136 | -41.52915 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 906e0f52-b8af-373f-8b13-09216786db32 | -14.77324 | -46.67185 | 2025-11-14 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48088a93-4949-3e27-a514-2ae8d34a9de0 | -6.16278 | -48.05206 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f0a3e732-1725-3ec2-a3db-983cc5cb66b1 | -13.68484 | -48.4213 | 2025-11-14 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2670a46-9e3f-3fda-8cef-2750adc8fa59 | -6.09358 | -41.71053 | 2025-11-14 04:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d22331dd-eb1d-3fbd-a78a-0becce755d9c | -17.79897 | -44.97998 | 2025-11-14 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c151ed4-4402-369f-82d5-be2408a4b75e | -5.5092 | -40.54995 | 2025-11-14 04:25:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README31.md)
