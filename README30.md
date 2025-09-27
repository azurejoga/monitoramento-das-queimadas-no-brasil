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
| 3017a9de-7e89-3d9d-82e7-210d39df1ab6 | -6.70292 | -42.75621 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 92665740-ca79-38e0-9cc1-6ec8339bbefe | -4.57663 | -44.06957 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0099f6b4-651b-3c14-800b-b95d3db108c4 | -6.55234 | -43.84507 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 685ad2d8-5b03-3d33-a500-4945d5f809b8 | -3.99876 | -46.9654 | 2025-09-27 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cdc22c1-2fc3-3491-b177-0f520f167e4f | -4.57331 | -44.06905 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fe5cfdd-b6e2-3efe-8212-434b3cce3960 | -7.13823 | -45.51143 | 2025-09-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fea88257-9366-3d6b-95ed-ca26a98cef1e | -5.82387 | -41.28648 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 725f0da0-a0bc-3191-b9ce-bcd1f9fb9322 | -6.76217 | -45.62759 | 2025-09-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f794d6d0-d3a0-3b95-8e7e-b45f221cd11b | -2.26392 | -47.19399 | 2025-09-27 04:21:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f132be0-01a1-38f1-aafd-74c76e00902f | -6.42673 | -43.07998 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3b0be45c-c9de-3fbe-b866-ba722ba30f24 | -5.73778 | -42.55634 | 2025-09-27 04:21:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f256643-7e92-3fe8-8c82-32399567bc87 | -5.29109 | -42.7807 | 2025-09-27 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a90d0495-6d03-3ec1-8477-b2c9e727212f | -6.52998 | -43.83431 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc7a95c0-0cf4-3003-b7da-2ccaabba00e2 | -2.44711 | -49.02626 | 2025-09-27 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aca3638c-09fd-3050-9214-4d2502c1a187 | -4.14565 | -39.99499 | 2025-09-27 04:21:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9931bba9-552e-339f-b70c-8845789a38e3 | -4.32849 | -45.27956 | 2025-09-27 04:21:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0a50fb9-0717-36ee-867f-3525aa29630c | -6.8932 | -44.75771 | 2025-09-27 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f101ab1-db63-3a92-8d59-6aa2286a6302 | -7.04803 | -46.4184 | 2025-09-27 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88ce7096-a752-368f-9724-6f5276bdd015 | -6.45634 | -43.13687 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c66b39e3-f3ea-3ea5-850a-1f82804c853e | -6.62901 | -43.8284 | 2025-09-27 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab910cbd-2013-310f-8679-30cd5f0732b4 | -3.96448 | -38.51731 | 2025-09-27 04:21:00 | NPP-375D | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d73a124-6e36-367b-9524-6264b3ee8096 | -7.12116 | -42.18383 | 2025-09-27 04:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3ac9abd2-cbb5-3f99-af67-e112ed549d8a | -7.04478 | -43.03319 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3c84856-af15-37ea-a2f0-8ee6a12eda94 | -6.93112 | -44.64269 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff454799-0895-3f30-b7a1-c72294534705 | -4.79015 | -45.34446 | 2025-09-27 04:21:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c48a940-bcc6-3e9d-935f-021122d5f45c | -6.12754 | -43.45629 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26a81489-d394-3ecd-b9ac-7a6a2675a5d9 | -5.33383 | -47.40297 | 2025-09-27 04:21:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccafa871-c54b-3f5e-aed9-3fc3f3004ba2 | -0.91215 | -47.54489 | 2025-09-27 04:21:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26489126-8ada-3660-8fc5-668e3c6c3511 | -6.61407 | -42.93069 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1665d848-8d41-3f35-9654-00ca61b5d9fb | -4.48307 | -40.78619 | 2025-09-27 04:21:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 69dc486d-36fd-3373-9304-c8a030c012e2 | -4.99071 | -47.35897 | 2025-09-27 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b28780d-250d-38d3-9efd-f05a9399eecf | -6.2599 | -42.47083 | 2025-09-27 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 834da66e-c4ff-37ca-9b37-0ac7b0dd00e2 | -3.58184 | -49.08481 | 2025-09-27 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f523fb30-10a7-359a-af64-85a0ea9cc31c | -5.20045 | -43.71785 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46afd2ce-776d-3edf-ac42-9478a37f449c | -5.73276 | -42.65068 | 2025-09-27 04:21:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4f0e7a1d-d0fb-3b92-a1e0-0d73d8cdf422 | -7.14157 | -45.51196 | 2025-09-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fc437cc-d1a0-3628-80b6-fd3a3f86c0be | -6.92846 | -44.64218 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a654502-f753-3e2c-afef-ce44b30a006a | -2.48851 | -49.26799 | 2025-09-27 04:21:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3edea749-600e-3e0b-a314-fa314cbc4ee0 | -5.53246 | -42.82135 | 2025-09-27 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dd4d4dde-dc3b-3846-b83b-6db44845fc2d | -7.62358 | -43.84404 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bf890fc-a1e4-3905-ab0b-f00bca151ef4 | -6.24345 | -44.09606 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6fd59c8-3d21-3a30-a2e4-3f77e18155b5 | -6.42388 | -43.07577 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fdaddbd2-a7f5-3106-b007-396f2f077687 | -5.95787 | -44.55675 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 699b9f20-32f0-357a-abd6-b50a547ce2f4 | -6.18572 | -46.50494 | 2025-09-27 04:21:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f209f7a-2b7d-3fca-bf68-36b05629265b | -4.64749 | -50.96609 | 2025-09-27 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebb146dc-028a-3186-a1f7-b8cc80b4c539 | -6.32543 | -43.15074 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84ece5ce-637f-3ddd-9ef0-aaf14b9a75d8 | -5.674 | -44.85349 | 2025-09-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a926d1b0-e3ce-3cac-9345-2254cd5b7388 | -5.88049 | -45.61808 | 2025-09-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cf049da-cd33-30dd-a659-ac0e9aa586ee | -6.06994 | -44.07547 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e52158d9-5518-38d5-9e55-a5537189d99b | -3.83457 | -40.33395 | 2025-09-27 04:21:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ad05985-979c-3287-8715-ece7b812f3d0 | -6.12474 | -43.45216 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d231f60c-521e-3b5b-973a-33c6adae482b | -5.71466 | -42.61401 | 2025-09-27 04:21:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1f4e71f0-58d0-34d8-8c66-973039ddebcd | -6.49033 | -43.27631 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd218607-51bf-3526-84b1-3a51195b5518 | -5.29166 | -42.77705 | 2025-09-27 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69a24b70-fd7b-308e-9482-c6eea5fefb2d | -6.99586 | -42.39202 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c7f96a23-f405-308f-8c86-5680b9ab2929 | -4.59144 | -50.65594 | 2025-09-27 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 67b88853-935c-3626-abd1-fccb4bc65de7 | -5.53189 | -42.82504 | 2025-09-27 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 554f5f0c-70b8-3330-a82a-79527ca36bc1 | -5.85716 | -47.26797 | 2025-09-27 04:21:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa818307-46df-3c01-b8e4-65f50fd9fa77 | -5.0744 | -44.85498 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 83b60dc8-417a-388a-8ffb-969095550d29 | -6.70054 | -44.58512 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87ac57d5-9807-3c0b-b589-01e97e12b346 | -6.92736 | -44.64914 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a77ba62-e29b-3fe6-a674-cec9b3fcb497 | -6.42785 | -43.07266 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3a03e06-e4d5-3dc2-a4f7-766c268867f9 | -6.70277 | -44.59259 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6309afa1-5bb8-31aa-8c8e-746293437316 | -6.49388 | -43.28023 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a8d488b-25c4-37d7-a440-f0c9bce6e2af | -2.26759 | -47.19463 | 2025-09-27 04:21:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79a83680-1272-3ac1-a312-bf21224cdec5 | -4.53572 | -48.65127 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fbafbea-ad52-3412-82f4-040779049768 | -6.1281 | -43.45272 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4958fa52-2bde-3d42-8c56-8aeddbf462f6 | -4.16683 | -44.27134 | 2025-09-27 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a46e6a25-e2f4-3961-a647-b53a93580af2 | -6.2081 | -42.85086 | 2025-09-27 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11233a2b-cb1b-37c5-9130-80663309cf53 | -6.06606 | -44.07842 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c9b37c5-bb24-3876-8b19-a9d89739eec8 | -7.28085 | -42.97298 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 15f355b5-8ad2-3170-b553-7fb1417c680c | -5.36784 | -42.30367 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 73616b56-f0a7-39fb-9a56-d10cc0ca89c2 | -6.69444 | -44.58058 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4b9ed20-0e91-34af-b22a-060382f31126 | -7.58604 | -42.32411 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fb3fca56-11dd-3be4-8d8b-c068738843d7 | -5.79963 | -42.83144 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 715470cc-0425-3f99-9854-8bc9af0b4fcd | -6.40786 | -43.31558 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 959df51d-6119-3adb-885d-3268a818f28f | -5.72691 | -42.30612 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b7cc59fe-51ca-33c7-8436-ee7e197c4a8a | -5.82207 | -41.29307 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e4c2163c-9a26-344a-b18c-fe7954db9764 | -7.60597 | -43.05642 | 2025-09-27 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 29881264-8eb7-39cc-9f56-ba6e0ac537ff | -0.90832 | -47.54432 | 2025-09-27 04:21:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fe87eb8-b080-38c9-a872-d1fcb9d7362e | -7.14825 | -45.51303 | 2025-09-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83485d0b-486b-3a9e-9f92-eaa1e18eff8e | -6.75045 | -44.63215 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e14b0a5-f9c0-3c70-8004-950952d8c3c2 | -6.81612 | -44.47501 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16d857fd-47aa-3d8b-92ab-c2a4ab094d96 | -3.05961 | -48.70615 | 2025-09-27 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd8f2d9c-a67a-36fd-91c1-38cbc69e4082 | -2.96156 | -48.5937 | 2025-09-27 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08f818d2-4165-3cac-bc45-bdf3447d180a | -4.66852 | -50.97921 | 2025-09-27 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70af8500-902b-3730-a18d-357b79a98950 | -6.70694 | -42.75298 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2143da11-3169-302b-8be5-991f2d55dd5d | -5.4918 | -43.08341 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f458dc6e-2023-3edb-9852-450453b8ac7f | -6.54619 | -43.84051 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3426f3dc-7320-3095-9459-66f90498420b | -5.4839 | -43.08957 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26e2d285-e81c-3392-8ba7-b589a78c42ad | -6.18215 | -41.84525 | 2025-09-27 04:21:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1b086986-dddd-3817-9f75-cf0eb1044fcd | -4.38584 | -41.92191 | 2025-09-27 04:21:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 576e8aa6-8e8d-399a-8c9c-146bc1b4f452 | -6.0666 | -44.07495 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e1f4a2c-ea86-3f30-b31a-bdec65065ded | -7.27046 | -43.01726 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6ecc2f50-df8f-3678-9f95-274b239131a0 | -3.96507 | -38.51349 | 2025-09-27 04:21:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21a2bc11-51e0-38b1-8ec2-f5650dab6f6c | -6.42444 | -43.07211 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f75002b-677c-33f3-89ec-6adbceeb7873 | -6.94861 | -43.24848 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c79eb91e-e123-3957-82e2-9222aea6e7a4 | -5.73219 | -42.6544 | 2025-09-27 04:21:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7c3812b8-3906-3245-aac7-f0dbae299143 | -3.83081 | -40.33337 | 2025-09-27 04:21:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1fd9a322-9c9e-307b-bb20-789198683904 | -6.70061 | -42.74812 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |


[Clique aqui para ver as próximas entradas](README31.md)
