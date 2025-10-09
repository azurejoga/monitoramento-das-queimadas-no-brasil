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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86e621fd-80dd-3dbf-b5c8-fa8fd7b3e194 | -15.55678 | -45.32335 | 2025-10-09 04:00:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e6b89da-adf6-300c-82db-b8d20b310dc0 | -11.77754 | -45.15167 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b264ddd2-9b1d-3ba0-bd43-9c418f30e6e4 | -15.81527 | -43.78123 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1a0ae97d-b7f0-3a0e-a7ca-1f7de3b7b03c | -13.82737 | -45.8206 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3958d3bb-0e61-3d3f-8e6f-9dfbdd1ddc7f | -12.04992 | -43.50031 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9452d63-4948-3f22-8968-47489c72d863 | -11.77269 | -45.15482 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b596856-4000-38f6-8e6b-8b7f5f7884d3 | -14.72504 | -48.36855 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de677869-57fe-30a1-b2cf-a4875bbaef26 | -15.39582 | -48.04821 | 2025-10-09 04:00:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 594108c2-68ae-33f8-bf52-7e8d5a6b399d | -14.19015 | -47.02939 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3699e856-989a-3b8e-9018-4bdd279f42f7 | -16.19912 | -43.65928 | 2025-10-09 04:00:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0e3c119-c01b-3914-8b21-4ea2d1998ca9 | -11.80198 | -45.03919 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c098279-1e2b-3778-8687-c7e7ef711e36 | -12.58276 | -41.28581 | 2025-10-09 04:00:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 77dc9f1e-8d89-39db-90a2-35320bbf3fe1 | -13.82608 | -45.80407 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b025a47-3a22-3e33-873e-9f2451f340f9 | -11.34302 | -44.88436 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 336901df-f8d0-3c85-aee4-3bebecdca82a | -13.78602 | -45.85682 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 624a6245-57e5-3ff3-a124-c1c18e477ec5 | -12.24507 | -43.78026 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dd9d911-ee53-329e-ae99-0332daefe7e9 | -15.9206 | -43.29901 | 2025-10-09 04:00:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85d0199c-e7d3-39b8-a856-46ba857b2c0d | -11.87284 | -44.92583 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29e4bee9-ac05-39f2-b26a-ad7dce3c1d65 | -13.48428 | -42.02372 | 2025-10-09 04:00:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 91fa4b26-a850-35c0-9f72-bc27bcededed | -11.65519 | -47.53661 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8e7a74b-6012-3d68-89c1-905ede2dbc87 | -10.34867 | -50.28769 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ef83366-4b41-3bbf-8cb3-018e9b19261c | -15.25314 | -46.3656 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f02951e1-b524-3095-bef5-9032abcfae3a | -15.29624 | -46.18008 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 263330e2-7a2a-32c0-94cb-a6ec7cad9d74 | -15.22652 | -46.36738 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fa48295-ef7d-3396-aaa2-4db9a5d961c0 | -11.24719 | -40.34021 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| a9dccf80-0711-356d-8469-2f435d290823 | -10.826 | -42.82047 | 2025-10-09 04:00:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0dfe1d3-097b-398e-be1d-ebd1c436f716 | -13.80626 | -43.93015 | 2025-10-09 04:00:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a426244-0d8c-366d-af7c-465bf4e46dbe | -13.4781 | -42.02774 | 2025-10-09 04:00:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e4ab8a9d-bff0-3bbf-879b-31d1d710deeb | -10.82233 | -42.81984 | 2025-10-09 04:00:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7acd4fd4-026b-39e9-ad89-fa5b5698c1e5 | -11.47706 | -43.47791 | 2025-10-09 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e61ea95-39b0-3b0e-aa10-9e5b0994fe8e | -15.3252 | -41.73811 | 2025-10-09 04:00:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8b48ac3a-4973-3523-9828-844c83b76709 | -15.29582 | -46.15898 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e887ec3-d004-33ae-86ab-8b7dbef1eed7 | -15.28222 | -47.87239 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd55b877-8db4-38ee-9d32-5a650e102684 | -11.76579 | -45.14554 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fab5956c-251c-37f8-b7f1-d679004043ef | -15.38782 | -47.3007 | 2025-10-09 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35bbdcae-0861-386b-b799-a3b1fceaff02 | -16.06632 | -47.76928 | 2025-10-09 04:00:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df701ac1-262f-3fa6-9ccf-e9fa056e18d9 | -11.86998 | -45.50482 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02a31a24-551f-3914-a278-c1fa78e5ded0 | -11.68845 | -44.25792 | 2025-10-09 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcbc344e-5124-3322-b4d1-f3d2df36a5fb | -15.49018 | -47.96847 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 909d783b-4040-31ec-8c67-6b4ddc7ba49b | -15.75347 | -48.72532 | 2025-10-09 04:00:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f4d4210-7785-37a0-9a68-64b569dca1ba | -16.75003 | -43.97916 | 2025-10-09 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1d7f84bf-f142-347c-82d5-9256456734d7 | -13.79016 | -45.85779 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beb4b178-f6ed-36f9-9941-df969cc429f3 | -13.48626 | -42.02111 | 2025-10-09 04:00:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1158df52-77cb-3c3b-bfff-7b1cc265b784 | -15.47357 | -47.95409 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe909ba8-fcb2-3c68-a325-621ef3f7fe43 | -15.31692 | -43.8544 | 2025-10-09 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4ddfdc6b-79dd-3aac-a969-33eb6e24d306 | -15.48394 | -47.95063 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d2065fa-2fce-3d07-98da-8b905467871e | -11.75256 | -45.1396 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28156d59-ec54-3b61-a05a-eed614bae807 | -11.88912 | -45.54514 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4682bfde-7d89-3e7f-a1ce-5c9f0b919418 | -13.82463 | -45.81199 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 20bc88ad-3778-35c6-8add-baddd14d85f2 | -14.25734 | -44.38517 | 2025-10-09 04:00:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ac5b8ee-81ac-3902-9e15-c1dbeaa06b6c | -13.82664 | -45.82457 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8f1db173-fdd3-3816-870e-929810beedda | -10.55797 | -51.45801 | 2025-10-09 04:00:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c99dcb7a-db85-3ede-a338-310f1721af29 | -10.8504 | -49.94072 | 2025-10-09 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d53f1c3-f074-3534-bf40-0498cd7512af | -14.84358 | -48.36561 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64b8fa1b-8e4f-3645-ab5d-c6e4ba09349e | -14.28647 | -43.6978 | 2025-10-09 04:00:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c64a4d47-20b8-3420-8532-c2e846a73365 | -15.23228 | -46.35999 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57049a14-ce2e-3df1-99af-b80bba460804 | -14.97563 | -46.29535 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79283126-d8b7-33c3-95d2-392443247f92 | -11.9871 | -45.21476 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9d543bc-d98b-3add-be7f-140f79049b96 | -12.74481 | -44.6128 | 2025-10-09 04:00:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b1cdfd5-0593-3e20-8ce1-380daffbb6a3 | -11.66629 | -47.54139 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d4ebbcb1-39f0-3e73-b30f-84c8fbed39e2 | -13.66616 | -44.30844 | 2025-10-09 04:00:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7714586a-dbbc-3407-92fb-b5908b74ee42 | -10.86278 | -44.63178 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 127cc490-7f87-3077-86db-c5c3187f7570 | -15.29485 | -46.1876 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b3b8755-67b2-3b66-a672-49efbec06ab0 | -13.58732 | -48.67012 | 2025-10-09 04:00:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47d738c6-2de5-37e3-b5b3-4cf29630fbdb | -13.80486 | -45.84875 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4dc0d94-10a3-3f28-aea2-cf339dfcfb51 | -15.4839 | -46.86786 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35fa64d3-b3a3-3233-ac14-ddf41fe280c0 | -11.77683 | -45.15557 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6877aff5-a22f-35ba-95c0-86d6fff5ec69 | -13.7902 | -45.8577 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 626688b4-7253-3d05-a975-728306e8f248 | -13.79867 | -45.83532 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b64e9e2-57ee-3e90-8251-b86eac91c93e | -13.79145 | -45.87427 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee73e5d2-fd5f-3bb9-995d-29f6ca7576e0 | -11.23879 | -40.34974 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2cd9d824-bf81-319f-8c53-d52cc3043dde | -15.25231 | -46.37006 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c797baf7-d782-3dac-bbf0-667416d53c92 | -13.29949 | -47.16539 | 2025-10-09 04:00:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2aa88857-9073-3d18-9c35-59b6c670aef7 | -15.06216 | -42.33386 | 2025-10-09 04:00:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 70756daf-f1f0-3d47-b366-494204832efb | -13.7902 | -45.88207 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca62d45f-4254-328d-923e-901d303e58b3 | -15.28592 | -46.16576 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9995692d-af35-3f69-b80d-d22fcb4e4691 | -13.79361 | -45.86259 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fd893f5-9517-369e-8d40-16b783c89257 | -16.37472 | -42.30648 | 2025-10-09 04:00:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dd6f39e5-dd63-35f9-8e7a-9b9b29c2c8e8 | -14.79023 | -46.10061 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e1b20e2-662c-3652-92c1-3618985abba0 | -13.02887 | -43.90217 | 2025-10-09 04:00:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 432f9c28-6e6b-37ac-94fb-b75eefae24d1 | -15.47142 | -47.95778 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fe90abb-7a86-3681-aed2-46322f166f5b | -16.37535 | -42.30273 | 2025-10-09 04:00:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b0ae742-63ab-3378-9177-d9707e8753d7 | -15.22002 | -46.37861 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66a050f3-4dde-34fa-92bf-258e88b39676 | -15.52659 | -41.85271 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fd81d810-3c3e-3886-9080-a8c7fda4cb2e | -10.52149 | -50.03186 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a150c291-61c0-3ec0-841b-9146220539e6 | -15.07045 | -46.613 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0276514-4a37-3822-bcd1-a83f2752889a | -13.81977 | -44.43313 | 2025-10-09 04:00:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 371e1280-91e3-39e7-b8de-f80e79c778c4 | -15.78541 | -46.25304 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98bf26e3-a0a1-3c0e-bb60-f670c950b55b | -15.52598 | -41.85641 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25f7995d-f152-3e47-bb51-7062245b44cb | -10.71024 | -44.0689 | 2025-10-09 04:00:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09d6026f-a792-3f0c-a6a0-02dd355c9210 | -11.4733 | -43.47723 | 2025-10-09 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2138e67e-9c69-33f4-8661-312d202fb869 | -15.37237 | -47.3326 | 2025-10-09 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9629967c-667a-36e7-ac85-87e4765be326 | -12.14657 | -47.75249 | 2025-10-09 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 070e9b25-0643-36d5-b598-647292a07158 | -12.65057 | -43.42552 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1900eac-77c5-322e-854b-711ed526609f | -13.03184 | -43.90752 | 2025-10-09 04:00:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea3fb67f-225a-3bf2-bbb2-9079717806c8 | -11.89713 | -44.95567 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 210df60c-630f-32f6-acca-0252de0eae6b | -11.77825 | -45.14768 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fcc6f0b-9772-328f-921c-8b184dfd0597 | -14.92957 | -46.79094 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a3900073-83dd-3d6e-b776-7896f548cfce | -15.39117 | -48.04696 | 2025-10-09 04:00:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef2904a0-d4b6-3454-a1fc-3b1ec37d9e75 | -10.22796 | -46.09407 | 2025-10-09 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README28.md)
