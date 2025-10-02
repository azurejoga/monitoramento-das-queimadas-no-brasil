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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 894bac2a-9fbe-3777-808b-9f58d0a4581d | -16.09955 | -51.0444 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a78066f3-5029-3654-8abb-29d4471b9211 | -13.15726 | -47.82033 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4f1d84d-1972-3665-ad41-aae636ecfeee | -17.95758 | -44.40905 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 08360ea8-3b47-3cd5-a466-9ff2308ee269 | -12.26531 | -47.81331 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc67f3b6-e97a-30e8-967e-d01fdfed5fb4 | -14.89528 | -47.18446 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3aa16fe-98de-35eb-926e-1216b26e23f2 | -13.21692 | -47.35257 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a58527d-5095-3ab1-8d8a-a335a3907c09 | -15.93399 | -57.50852 | 2025-10-02 04:32:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1f9f292-015e-32dc-b0e1-2cd5d4f4f364 | -16.04781 | -45.7277 | 2025-10-02 04:32:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02d132d2-421a-381c-b608-d57ad397488b | -16.0374 | -50.89741 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 531aed5c-3dcf-3d7f-b3f2-837d0869fa0c | -12.86308 | -46.93342 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a1e55c0-22f8-30bd-abce-e2de0594b814 | -16.02121 | -50.86579 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e80e31d5-9405-3b47-b13c-8c503b6bbabe | -12.2603 | -47.82336 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55d3d68d-fc5a-35df-84af-39d0d9656bfd | -12.75113 | -46.88983 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cac3662e-0f61-3f92-967e-bda45a29cc9d | -14.68964 | -49.60534 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dea08f5-fe3b-3f2c-9ebd-fc9298965e3c | -15.34986 | -46.27416 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7281900-739b-33dd-a08e-d04be6d5937e | -12.88374 | -46.93303 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f6ec120e-a9d1-3e92-8dde-3c7558f2a6cc | -13.6836 | -48.0628 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34632c8e-3bcc-3f05-b4bd-01daee58f429 | -14.2118 | -44.92899 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ec56e60-45c3-36fb-a19e-35fb70c34fa6 | -12.94487 | -48.43067 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 642d2049-1c56-34ee-af45-90ea4877d21d | -19.45754 | -44.28152 | 2025-10-02 04:32:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f72bd3bc-dbd9-3b6d-9050-30aedfa01cd3 | -15.50466 | -45.90533 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de1e9ba7-8662-3c70-8973-7c91cf7bafba | -12.86655 | -47.02185 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7374a69-c452-36eb-b8c6-2351bec80881 | -13.06194 | -47.00181 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73dc53a6-f77c-33c5-90e4-d0cb028dd0cf | -15.25677 | -49.29386 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3ef648d-8f7a-38b3-a92a-58878ef18b31 | -13.78051 | -48.00632 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11383cf4-d67c-3e94-9dd7-82da31a29c35 | -16.0339 | -50.89687 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a09ed533-4d11-37c5-8199-9089826bd851 | -13.37215 | -47.29031 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74d4e6d7-838d-3ea4-a2dd-608991c64d87 | -12.68848 | -48.55013 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e69ba64-679e-33d5-9f82-dcc4f1b11194 | -11.59392 | -50.1685 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8c09fafb-8ba1-304b-8315-e698baa94424 | -14.60296 | -48.23663 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3d7cec6-2d91-35fe-8408-7b6e141f3a6b | -12.81635 | -47.01382 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f54af460-6852-34ae-be58-973aa4088a55 | -16.05478 | -51.03175 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dcb9d395-c59a-3905-82e6-33f2745a487b | -12.84858 | -46.93839 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57665be4-82ee-3130-bdae-1f61c57d06a3 | -12.63152 | -44.85672 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ecb2bc1-261e-3f36-9dd9-030265d9c338 | -19.72183 | -45.88941 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82edc210-2230-3f57-84ec-97bbc6c3f68b | -15.50759 | -45.90989 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6e27d595-75aa-3d9c-8804-5df8851c2d63 | -15.26071 | -49.29078 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 480303f0-2600-3dc9-b002-127f52192cc6 | -12.81245 | -47.01684 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 204332d3-1101-39dc-a634-cfbaa3ebd057 | -12.69072 | -47.56279 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c14ac71c-d1e1-37c9-bad4-60fb41605cf7 | -14.4259 | -46.12019 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3080c43-89db-3278-a782-11ef1fb6d521 | -15.34601 | -47.08653 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce099ab5-9753-3670-9696-c8c07ca1850c | -13.32544 | -47.32649 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71992224-d6bc-376a-ade0-677bd18f38f9 | -15.39768 | -49.1873 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f83a4fe0-9254-30b4-a68c-d8cb0287854c | -13.77212 | -48.03778 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bccddfa2-2299-3222-a67d-dbaa57c6643b | -13.90905 | -48.07102 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5205cc65-60b9-3d66-827e-92687dfd2fc9 | -13.20356 | -47.32844 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06b15b27-089f-3606-a80b-9c9bb7d51ea2 | -13.53975 | -47.25047 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 750ca9a6-c94f-3c8a-b42a-a00fed7e6041 | -13.94206 | -48.09447 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 832ce47c-e7a3-37d9-aa4a-90166a93e08b | -13.1795 | -47.78761 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c18b8adf-e97a-3a0a-a28c-cf48f643c51a | -13.00459 | -45.20484 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 040f06ae-a1b9-3da6-9f94-8eb830634c71 | -12.24956 | -47.78845 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34ef3264-ccc1-3e29-9e77-487495b8a0d7 | -13.66522 | -48.09259 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f4241b2-812a-3dc9-9e4f-3f3f87ca3faa | -12.42366 | -45.17125 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6e623c5-c670-3f3b-987f-936ebf170e7e | -14.02499 | -47.95847 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ea4f7e1-cda1-3a77-b865-7bb7d55e9160 | -11.86549 | -48.01307 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 560d4e0f-dbc0-3fbf-92fb-d4d5b54c216a | -15.10564 | -48.37088 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4df09563-366a-33a1-a866-03887fdf853e | -12.25699 | -49.16108 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd8ba93e-81e4-3d65-ad37-9be41fbc0bfb | -18.62849 | -50.68669 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ec173ab-fa5c-3312-8c2c-86ca41b2e65d | -13.65992 | -47.3068 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c8ad8ab-ed5d-373c-97e9-ef72d3122013 | -14.21781 | -44.9388 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6343e564-b03a-3e28-a8c2-23446a853c8b | -13.77433 | -48.04545 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9749f3a-c740-34bf-846c-4a12c4a175f6 | -13.95702 | -48.10789 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d00f4a65-480b-344b-80f1-2d98db2a7865 | -13.4772 | -43.51099 | 2025-10-02 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03455118-2271-3cc9-bd0d-fd60de75fecb | -14.35529 | -43.84328 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36114b34-feab-3588-aa86-d2fde075a56c | -13.32478 | -47.2205 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 352b5a39-436b-3fee-be0a-a337955fba7d | -13.7578 | -47.97701 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4aa1ce45-f42f-3b56-9b89-1e094a0aad1e | -15.81783 | -41.89386 | 2025-10-02 04:32:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ee0d5dd-7717-3f40-b808-310ff2c80dcf | -12.80752 | -46.90265 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9baacc2d-9b66-3b96-b115-92cdc4e64a77 | -14.18759 | -46.12813 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d09a3ac0-5a28-3c2e-bd5a-c3d98a819659 | -13.75443 | -48.69695 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f206b087-948a-3ebb-bc66-ac7a6a7565b2 | -17.08152 | -48.55914 | 2025-10-02 04:32:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e00268f7-cb5c-391b-991e-75bfcd33bf59 | -11.84984 | -48.04684 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cde9f88-4f37-3138-85e4-8a7e52d8a500 | -15.25097 | -47.90258 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b848e7b9-8488-3daf-b3de-565220d3fa74 | -20.1356 | -42.85914 | 2025-10-02 04:32:00 | NPP-375D | SEM-PEIXE | MINAS GERAIS | Brasil | 3165560 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b352171a-2924-3f82-9bca-5831e8f35661 | -13.75777 | -48.69749 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 498c35ae-8f7d-3889-a589-5914becc2b5c | -19.89852 | -44.93502 | 2025-10-02 04:32:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b27fe9b-23c6-325f-8190-097193ace422 | -18.60897 | -50.69883 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac5423ba-0e1b-3de1-a32a-0251212b9b1d | -13.54812 | -47.28498 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 715234a4-302a-3472-980f-f91ed4bbb721 | -17.1155 | -47.11319 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16de977f-4fc2-3446-85a7-799b348a5859 | -14.90313 | -47.22316 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99b77408-0e3a-3da3-855a-4bda15844a5f | -13.05468 | -47.00433 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f57dee6c-ce04-34e4-bceb-2fe9a3d5de0f | -13.36604 | -47.2856 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01df19a3-2e0f-3280-bfa6-17871de70b57 | -15.94999 | -43.3043 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 840ba88e-2079-368c-87d0-b4f06631764e | -17.20778 | -46.9858 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e299c4b8-99e9-3408-954d-9938fab84be1 | -12.65814 | -46.94873 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5f26bd6-ebcf-37a8-afa7-76248cb1591d | -12.88764 | -46.92999 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf5e5636-36d1-3244-99cc-7609784b6fbc | -13.86987 | -47.95134 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f299f742-3c42-38e1-a0e7-62c66f8695dd | -13.77709 | -48.04956 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ea7400a-24c8-3676-b60e-f9f499b3226f | -18.59085 | -44.51613 | 2025-10-02 04:32:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69074e0a-a15a-3ba9-be9b-ed205cc91ba1 | -13.19221 | -47.83699 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef760862-23c2-39d8-8dc9-c3757edf7770 | -14.6222 | -48.3094 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b40bbb9-d8b5-3d7a-94d5-6623bd5c2bc9 | -12.65417 | -46.86341 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c163ac52-0822-3687-9152-22f5700b5fa5 | -14.9026 | -48.3296 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a6c5d0b5-9cbf-33f1-831f-1512a007affc | -13.36291 | -46.62905 | 2025-10-02 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d5b7a8a-c439-30fc-ade9-893e8881d7b7 | -17.17921 | -47.03622 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 3d4ae392-5597-30a9-b52e-b683da3b833f | -14.15831 | -46.13537 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0044fd6d-7a4d-39e9-b2dd-07cf91bf6daa | -14.43605 | -46.35223 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9873bd9-a2a0-3528-857f-087954dd51e7 | -13.75211 | -48.71132 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e67bab0-0c41-3155-ba4f-f1d49abe179d | -19.59281 | -43.81516 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 827bde12-884f-3d3f-8cc6-c80c4a5fc088 | -13.22414 | -47.35017 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README87.md)
