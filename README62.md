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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8e5896d-1294-3288-a807-549e22b1062b | -17.62271 | -57.59267 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| bdec7d66-4d3f-32ba-a2d0-71c70d62b53c | -9.61514 | -44.38893 | 2024-11-20 04:53:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43d18ff7-d126-3846-b8e3-9bcd40f06e85 | -12.03638 | -54.64544 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faf4172d-7b50-3efd-a73e-9afdbd8717b1 | -17.62551 | -57.59737 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b363f310-1d7a-3170-bccc-cf7ea9351957 | -12.14053 | -51.18623 | 2024-11-20 04:53:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ef9d1af-6ec8-345c-b138-3914690b4df5 | -11.06527 | -41.61906 | 2024-11-20 04:53:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 016c5022-1954-38d3-a519-c3767fc9fc35 | -20.85965 | -54.92811 | 2024-11-20 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de2c000b-30df-34bb-93e5-4c1721677c4c | -11.09819 | -54.62045 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f667239-a4e7-3775-bb8b-3e740af8bc9e | -11.10433 | -54.62513 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 700d7d4a-c585-3e87-918e-a49377e71ce0 | -11.10317 | -54.63232 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2fbecab7-6be9-3943-a490-ff7f3f86c79f | -12.03524 | -54.6526 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8428b913-207c-3578-bb7f-0b52bc89abbf | -9.49747 | -43.18799 | 2024-11-20 04:53:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b3fdd11-83aa-38bf-bbef-dd4aa9eea208 | -16.7425 | -45.76859 | 2024-11-20 04:53:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a003a52e-406e-3c87-9acc-792112fcdc1f | -19.30934 | -55.20719 | 2024-11-20 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e35dfd6f-d1fc-3942-968c-d67b50577f38 | -11.11382 | -54.63039 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3c86b13-25ab-389e-a4b3-c536cceee738 | -20.3017 | -55.06458 | 2024-11-20 04:53:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f42eaca8-98a8-3e96-a9ae-fb86352dda09 | -10.42166 | -44.49002 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1862175-32e0-3dc4-b6a1-b065635acfe3 | -20.20925 | -56.62746 | 2024-11-20 04:53:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 31560611-3d94-3681-82a9-91711014e406 | -10.39744 | -44.47044 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 335edaa2-f1fa-322d-add6-bb016d064288 | -10.42711 | -44.89004 | 2024-11-20 04:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93312a07-d821-3d7b-9cad-a40ea58b640d | -16.73725 | -45.76796 | 2024-11-20 04:53:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47964c45-5403-3bf2-8cfe-f0517540bc4c | -20.05041 | -57.20686 | 2024-11-20 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac5a41f6-6ac2-340d-a20b-d13b803bb6ba | -11.09251 | -54.63427 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec4f5ed1-7846-3eb1-bb3f-9db9751d8467 | -12.94251 | -57.01714 | 2024-11-20 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3553bcbe-ca20-3f84-ac40-45eb49ab333f | -11.09368 | -54.62708 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c268df4-dabb-3890-bdab-37c8f265bb2f | -17.57783 | -57.49394 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9ee478b5-f35f-3f4c-b45b-8787cba98097 | -11.04403 | -44.57386 | 2024-11-20 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b755faf1-8057-30dd-b9d1-8b419b940194 | -8.29725 | -55.10169 | 2024-11-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4848f886-0619-3ace-952c-6c1b5cb0486c | -17.60458 | -57.39974 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fdea5650-a0f3-3889-82c2-9d617082a038 | -12.03304 | -54.64488 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58e5ba54-2920-3105-af5c-b7bb1d4dc55a | -12.27957 | -43.52886 | 2024-11-20 04:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7df782b-e6a5-345f-a798-33745861df8e | -9.78969 | -44.71741 | 2024-11-20 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3693623-1846-301a-9fe2-4dba72021615 | -11.06699 | -41.62307 | 2024-11-20 04:53:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ec853ca7-3100-35c7-8f17-44f07766b5a4 | -9.1433 | -57.55835 | 2024-11-20 04:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5595d9c1-2c8c-32f2-bf20-8db403ecd097 | -9.19411 | -44.72129 | 2024-11-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f7dccd4-99cb-3158-96e5-22ac5b4fcd8c | -11.09483 | -54.6199 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0cf0188f-3298-3e30-aa51-19f3e17629de | -10.39214 | -44.47663 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c1525d2-696f-31b1-bdd4-30fecab498f1 | -17.55626 | -57.51486 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f53bb85f-6b68-303a-adb0-23a078877f53 | -11.10097 | -54.62458 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e8e5eb5-a20b-358c-996c-eed8d21ae7f8 | -11.09309 | -54.63067 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a2f86c2f-fa9d-3b2f-862f-73f153c2cd07 | -17.60182 | -57.56496 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1e816e82-6694-39ea-87bc-616b80642c4c | -12.03783 | -54.64916 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1599daff-6181-39a4-907f-68c5360074c9 | -11.10988 | -54.63343 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8c20b88b-8ee8-31db-b77a-1b2b5984f5fa | -9.61557 | -44.38572 | 2024-11-20 04:53:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57b214f2-bf71-317b-8efb-a0b02a00e36e | -12.12283 | -54.29048 | 2024-11-20 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fcc3168-00c4-3e71-8fb0-0e2d105a5dcf | -9.50313 | -43.18875 | 2024-11-20 04:53:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fb5e52ab-8c3d-36c2-825e-f3a7ec666f94 | -11.24853 | -44.44273 | 2024-11-20 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 822f1ffa-f79e-376c-b47a-398498027a31 | -17.55557 | -57.51889 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c9223820-4de6-34c7-b4ee-32a8bca3b3ce | -11.58896 | -42.97775 | 2024-11-20 04:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54c111e4-7abe-3909-b5b2-36b3c1e1d794 | -10.40228 | -44.47444 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca75986d-92dc-3370-9dc4-6dff2ea45815 | -12.58302 | -52.49521 | 2024-11-20 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c57cdaf-eee3-33d7-b86d-c0085981676c | -11.37219 | -55.08662 | 2024-11-20 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed0d2e9f-e1f0-3866-9fed-9f29c461ab8e | -11.5021 | -54.28016 | 2024-11-20 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c41d0bd-f68d-3dfb-a641-c7bc2e2f67c6 | -10.45117 | -44.88763 | 2024-11-20 04:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b3b0dfa-cfd1-30c5-88d8-ef63ae7cca6b | -11.09703 | -54.62763 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a64e6471-be97-3b52-8c50-4ddecfa3d896 | -12.34016 | -50.00205 | 2024-11-20 04:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04808305-5639-35c6-b09f-15505c320558 | -12.1195 | -54.28993 | 2024-11-20 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 174a9a1f-a29f-3c8d-94f2-ac397336e8b7 | -10.76652 | -44.82488 | 2024-11-20 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04dee8c7-1912-3fd7-a0a4-be41dd6ff008 | -10.45156 | -44.88456 | 2024-11-20 04:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 434e2c02-7d67-3cb3-9bd6-7bf11b015385 | -17.5716 | -57.50939 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 22c13faf-957a-3674-a37c-501ceca57b3f | -11.10155 | -54.62099 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ed102f9-5ca5-32c3-8cc0-012d866812b8 | -10.39662 | -44.47694 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf1008c1-d685-388e-9964-63329769fe6e | -11.09587 | -54.63481 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2553eb1-c17d-3e58-9c66-169f761bcbb0 | -17.56662 | -57.47528 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a017c62e-8453-387f-9979-473b4226832c | -11.36312 | -44.5767 | 2024-11-20 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08c6aeae-7d2e-32a4-892c-3c4ced12c148 | -11.09981 | -54.63177 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c16dc1f1-400a-3370-8b33-699b7f7b0b82 | -11.24809 | -44.44607 | 2024-11-20 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a4f7ab8-ba68-3add-a186-393b95180a01 | -11.09529 | -54.63841 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e98e97c1-07aa-3ae5-ade0-85ceb18999da | -11.10259 | -54.63591 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e181f4f-7dcc-3990-ada5-0514bf87358f | -9.19371 | -44.72429 | 2024-11-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ac5b09e-6344-3c2f-8f79-cc8bf3609419 | -12.14058 | -51.18576 | 2024-11-20 04:53:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8c6a062-cbb0-3dbd-b2b9-e2eff0385eaf | -9.67336 | -46.25492 | 2024-11-20 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c526a8e-fd7e-3fc5-a429-dec2e65220c7 | -12.03899 | -54.64201 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa06333e-c5ca-3739-8d75-c6d1c681d3cc | -9.19254 | -44.73324 | 2024-11-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ad24609-77cc-3dfb-be1a-ba17c564163d | -11.09425 | -54.62349 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82b24a41-f83d-31f8-b79c-669334771d09 | -11.49876 | -54.27961 | 2024-11-20 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b03dfaf2-a24e-3a6f-8707-e74ac2bda831 | -11.09865 | -54.63896 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2fa0d10-66a3-3807-b96e-9bc6d04454e3 | -21.22145 | -56.35164 | 2024-11-20 04:53:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88783626-3893-3a8e-b75a-e0d3548f2873 | -11.10039 | -54.62817 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bd4e94f9-0a6c-3bde-8a31-9379a30bb9d5 | -9.40598 | -54.79737 | 2024-11-20 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2179d68-e243-3dfd-8ab5-abbe1e1315c5 | -10.93016 | -44.88215 | 2024-11-20 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 414aa81f-5a48-3c41-9283-db5e1aa0f74b | -10.99953 | -54.22749 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6215b2a7-b4b4-3ae9-94fb-094674493953 | -11.33634 | -55.05048 | 2024-11-20 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e84884b6-d02d-330a-949b-0da73854098f | -11.10711 | -54.62928 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b2d5a1c0-337c-334f-affe-de053d5f3a69 | -9.19215 | -44.73619 | 2024-11-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da382a0d-3493-3f5f-8280-e477ae45af7e | -11.11104 | -54.62624 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b4d9a13-0cd9-34d0-9bc7-6410088e626e | -11.06125 | -41.61676 | 2024-11-20 04:53:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 58e71c23-1f5c-3929-a3b9-305665349f6a | -11.38081 | -54.92666 | 2024-11-20 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e76b77c8-2808-3436-a2f2-217af8e4e8aa | -12.94409 | -57.01599 | 2024-11-20 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bcea71c3-1ede-3c23-b3eb-03b9d2b4bbb3 | -12.03726 | -54.65274 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33590ab2-87e3-3095-8cfc-52db6d5bf81e | -11.0909 | -54.62294 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cccae1c-eb70-3b51-bb03-e41007eb1349 | -11.31306 | -54.02111 | 2024-11-20 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21476f54-0711-3c8d-bc81-c5c00e030bc7 | -17.55753 | -57.46531 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6b813f83-9c32-39b9-8a1b-4e2114c7bfc6 | -11.06459 | -41.62455 | 2024-11-20 04:53:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c7e2dd56-81a2-32f3-b210-9758670db42b | -10.39179 | -44.47287 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80e121cb-42d8-3aa3-b349-756024752715 | -11.09923 | -54.63536 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f4bbd17-cbe7-3068-a101-d7fd12f2ac39 | -21.31343 | -56.0096 | 2024-11-20 04:53:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf5e812e-eab5-34ea-b6cf-a1af32900b8d | -21.22204 | -56.34793 | 2024-11-20 04:53:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b40cd07b-fc67-367a-bef5-f443cbf28c33 | -10.39703 | -44.47369 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7def1976-7bd4-3f8e-942a-087d293d9938 | -12.0406 | -54.6533 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README63.md)
