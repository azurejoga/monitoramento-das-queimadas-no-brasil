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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0519cfb-738e-3cce-bbcf-559bd617db34 | -13.638 | -46.5162 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e1df35e5-0c2a-30fb-a832-8aa66ceb3dd4 | -10.8573 | -50.14713 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90b6817f-5ec8-3438-98d2-2b3dc8183d29 | -12.07555 | -46.38253 | 2025-10-29 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdc320a7-c903-3ee3-99ac-f62fe99a604a | -10.90589 | -50.21062 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2803dbc2-686e-3848-bdb9-5cff291f5819 | -12.55879 | -44.96498 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 156476d5-ae16-378c-ac03-0fd35a969df3 | -12.08882 | -47.25726 | 2025-10-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5554a577-4884-3ca2-80d3-6df6063db5b6 | -10.53694 | -44.59992 | 2025-10-29 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 091df115-560b-3d27-9e1e-c97f16a815a3 | -13.26717 | -47.72343 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 836994d9-15ae-3b09-9614-b40461359efa | -12.18061 | -43.57354 | 2025-10-29 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1736550e-9cfe-3286-bd61-c3af7c23f103 | -13.32219 | -47.45303 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0da03b6c-a911-3396-a6c3-14df5b073198 | -12.18033 | -46.71571 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 124d2461-8f12-3610-98b6-f5db7518132c | -9.5686 | -44.71293 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c5b1fd9-d2eb-3319-930a-34473cc06a6a | -14.52432 | -48.00176 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7ec993c6-f723-3a46-b13b-98652d7296fd | -10.65069 | -48.00105 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1553c268-aa55-3cdc-9999-68e86fdf413d | -12.10863 | -44.59921 | 2025-10-29 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 22ba8bd6-e179-3581-a0d9-c60c8183eadb | -13.02211 | -48.76976 | 2025-10-29 03:55:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4dfd3e89-a720-3d6f-aef6-5877249f5094 | -14.23542 | -43.00959 | 2025-10-29 03:55:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a33e0b6e-af4b-3ca3-8840-fe1296353a29 | -12.69714 | -46.30284 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b661249-9bb6-3850-8e0f-b7affb6d78f1 | -14.99099 | -47.87082 | 2025-10-29 03:55:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bc47cf43-bd34-39e3-a664-296d8225a1c9 | -12.19408 | -46.71833 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 056e0719-0f91-3cf7-8b42-001a202cb443 | -12.85905 | -48.62767 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f35d6a0-df11-3998-ab43-8b22140b8d70 | -12.75745 | -45.17084 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feb0a9dc-55ac-3c6d-ac09-5896373482cf | -14.61108 | -48.39859 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35fa6daa-1d66-3695-b08b-c9b850165ebb | -13.57947 | -49.59557 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ff394d5b-54ab-39ba-9e5e-e7783a26c21c | -10.76478 | -47.83121 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef82c091-aaa6-349d-b802-37fbfe00ff51 | -10.51482 | -47.73522 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4aa94a17-ffa1-38f5-9219-eadf3466cb69 | -9.09203 | -47.81147 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfffcd81-9380-38e0-a470-4173c20b4f02 | -10.94896 | -47.62271 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0ef921e-545d-3e02-9ad1-94105456d1c5 | -10.65518 | -48.00545 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3c84195-243e-32f4-aa08-33e1771bf01d | -16.12023 | -45.75177 | 2025-10-29 03:55:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07026741-1e6a-32e9-b015-efd616d6653a | -9.49225 | -47.00655 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c88dc268-ab89-3449-a21d-33821dbe6c89 | -10.76429 | -47.88942 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf7ae3f7-a331-3c79-a7d4-ee1f770c7ebc | -13.56328 | -47.32476 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21b4edd3-4ace-3eb9-a227-8bd309e26c85 | -13.94118 | -50.33836 | 2025-10-29 03:55:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c8477af-e235-3144-8014-904a7ad9b93f | -13.35718 | -47.66417 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1df86cda-1a7d-32a5-8bbc-c60789f878cb | -13.63863 | -46.48835 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e5e46cc-cb58-307d-becc-d9d79056f109 | -13.47242 | -47.81511 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11826386-2a44-3356-b7e5-3f3c9075e559 | -12.20747 | -46.49405 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31216d72-4340-30cc-8a55-375778b8946a | -11.57696 | -47.94266 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f957d58d-0134-37e7-9562-09562a30d0b2 | -15.11065 | -47.94097 | 2025-10-29 03:55:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6576544-c8ce-3aec-8655-f3b175428a09 | -13.43099 | -47.37397 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 707f84fb-387a-343d-a2a0-8eecb1eb79c3 | -13.94784 | -48.47885 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79313927-2fc1-310f-a758-ed1f713496ef | -10.65368 | -47.90076 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96c7edaf-ca37-300e-89fb-9f95ed123dd2 | -9.44575 | -46.88804 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e3228d2b-0a72-3ffd-bb44-92f22d542f8c | -12.39646 | -46.64867 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 079f1891-9a52-3420-92d5-4f1c7bc9b6ec | -13.56527 | -47.32827 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5f1dfe8-edbe-36dd-93f9-29a3408e897f | -13.57468 | -49.60061 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0c812d2-2fe8-3050-b9eb-301cd43285be | -10.66153 | -47.99992 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 12557eb9-cf6f-3d77-9403-c966f0a5276a | -14.6094 | -48.43353 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a308cce-07e5-3d0c-b078-a15ae8f79689 | -9.34065 | -43.08913 | 2025-10-29 03:55:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab67f83c-c6cd-3d59-b917-42acfdabf25f | -13.57631 | -49.59252 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5314093-86c6-39cb-8156-792296806cab | -10.52332 | -47.74588 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8bcf47eb-dba6-34e9-8750-c1c1f1c56b6a | -9.8054 | -47.75422 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 643c8a44-03c4-3822-8468-767b4da70bc9 | -13.57107 | -49.59064 | 2025-10-29 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a583cfc2-b86e-30fc-9cda-f1dd6606332a | -12.70492 | -46.31027 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 68b8af39-067f-37a9-9075-6a0c938ff2a8 | -9.92362 | -47.12053 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c258fffb-0663-3f09-b371-81a37543273d | -9.90697 | -44.9199 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1eb0d131-e3f8-362a-af77-3939ddacd321 | -11.28696 | -47.55689 | 2025-10-29 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74a8eb79-58f3-325b-a61e-c41dcaf376b6 | -14.26929 | -47.31602 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d889c383-39fd-3f5e-bdd6-57fa638e6aef | -15.63727 | -46.97362 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53c453ec-23a8-36e4-90e9-1b6d81e06a63 | -10.90028 | -48.37313 | 2025-10-29 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f628de65-4e70-3722-aaa4-c1c77d74fe3b | -11.97556 | -49.94011 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0615c0b1-2466-3b23-a8a4-1a1213a62356 | -11.76935 | -43.21961 | 2025-10-29 03:55:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 28888f26-3546-32ab-9666-c2d7b1952024 | -9.88722 | -44.8837 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 343b9cb9-af46-3656-bcd4-388fc7952e9f | -13.25145 | -44.11338 | 2025-10-29 03:55:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c732497-b99e-3549-841b-1b385fac7917 | -13.87524 | -48.48048 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0c1173c-89b3-36c7-a041-0e1807bb05d4 | -10.64498 | -48.00311 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a45c3bbc-8c25-3b63-aab1-ff0cfdee1b55 | -10.85148 | -47.89134 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd2fd51d-1b4c-3a6f-b5c4-4ee0cff8a49e | -13.38015 | -47.41172 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 53cd1511-6536-3076-b045-f0307eef2fc2 | -14.25755 | -48.10526 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2946ed61-d68a-36bf-a455-22066dae8ed0 | -14.41967 | -47.85107 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04a52b2f-3d92-3a82-8197-0c4032fb7659 | -10.88131 | -45.07172 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa9cf0a7-108c-3ab0-b50e-82d4ef38c8ff | -12.55536 | -44.96064 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d818b32e-409a-3b8e-8760-15313c2ee09e | -9.62289 | -46.86033 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 986cf0a4-67dd-3c3d-8f27-b7dd1cbc9224 | -9.50709 | -46.96761 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c48b265-b06f-3d92-bbc4-43c0d19fa6ed | -13.26764 | -47.85587 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ddf25bd-8307-3f8a-8452-5d609581fd1e | -10.62795 | -47.88076 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6ebe500-7f98-3452-a74a-9a0dfabaa660 | -9.3632 | -43.68737 | 2025-10-29 03:55:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d1a2c61e-5c20-3b2e-bc34-dc26cfa5a33d | -11.72223 | -43.38459 | 2025-10-29 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21cd65a6-4fe5-3883-8010-32e704c97c17 | -13.23636 | -47.9976 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a6796df-fffb-3389-a18f-8af2afc1d186 | -9.96255 | -47.14085 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e5599d37-3134-3a8d-afb7-47b5ebc20e86 | -13.22563 | -47.73207 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| de67d7eb-cb97-3d5d-9253-fc35e4a4369d | -9.27397 | -46.38852 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4b41fa65-f62b-358d-b129-6d8e7a467634 | -10.76858 | -44.73977 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc995ab8-3ef8-3098-b29e-c21fc757c3c4 | -13.34669 | -46.34955 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de1c2061-7309-3770-9732-e974ca44bc05 | -13.64251 | -43.69578 | 2025-10-29 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e9768d8-19c6-3ffd-9b88-7ff8cb51c772 | -13.5537 | -47.32434 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5cfca61f-973c-37e2-9ef4-76e447fa5a99 | -10.95566 | -47.61445 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64c9fa4b-2f21-3721-a4b1-d2d7c78b7154 | -10.85204 | -47.88837 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c742487-9392-3fb8-a1b3-880b1c450655 | -13.64157 | -46.5216 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46c86de8-5144-34a3-bf3d-686e195e1fdb | -9.90767 | -44.91594 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a512ca9e-d58d-3295-83b4-6a884478c562 | -12.70935 | -46.31105 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6806a939-6aa0-310c-a7c4-34e66246ce3e | -10.03658 | -47.13505 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa263158-e071-3926-b11b-da4394362f2c | -13.63377 | -47.01818 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab84f27c-fbd1-3df9-81a4-01056027d63f | -14.992 | -47.8656 | 2025-10-29 03:55:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e08f4057-f5e7-3752-a2e9-b0dfc27ae281 | -13.63405 | -46.46411 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3698c7e1-04ba-36e9-af4c-2e043b3a897c | -15.32475 | -42.99085 | 2025-10-29 03:55:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| af5eba6c-9c04-3efd-adcd-2c4102a8c41c | -10.904 | -47.80769 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d114c58-c34f-3885-87f7-aa2bdff12b2b | -10.86838 | -46.04463 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3f9befe-aeb9-3f0d-9e5a-87f49bd4643a | -10.39375 | -40.6494 | 2025-10-29 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README20.md)
