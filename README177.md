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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 813b927d-7fcf-3072-9922-941e7aaeef35 | -13.76994 | -43.53835 | 2026-10-07 16:35:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| af411226-7283-33b3-9ff9-5d9db6ce1427 | -11.22787 | -45.25295 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 402f3dfc-f6d4-3a73-a12d-78a35418f5b6 | -16.85415 | -40.60091 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 3e2aee25-3e50-3bd6-bf0f-5f53e00e90d7 | -11.63713 | -43.67223 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9654b494-24ac-33d6-a427-ffefb92a64bf | -12.18464 | -44.76154 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 1ef954e6-2db4-3375-a61f-4b869369ec09 | -12.2221 | -44.70545 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 7ed99362-109f-35c2-a672-105026f68351 | -12.96362 | -47.07407 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2da70ba7-9248-38c0-8210-214787e6de88 | -14.76865 | -48.8194 | 2026-10-07 16:35:00 | NPP-375 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14cd0013-dd6b-3339-9a3c-d18177649c31 | -12.57006 | -45.08855 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c124df1d-86d0-3bc0-8f20-b5f78807c012 | -11.22471 | -44.86734 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 86bf17ae-9c7d-3fd0-ac32-b368a21d01bd | -11.22794 | -45.28445 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 460457bd-abd0-34c4-a4cf-beddd5c6080c | -11.62194 | -43.67533 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 20b25a6a-79d6-3a50-a263-cbdf2bfaa473 | -12.19946 | -48.42399 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 69c18850-38ed-3457-bb79-1e73f166cee5 | -18.16113 | -42.58171 | 2026-10-07 16:35:00 | NPP-375 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d345d3f3-f974-3c80-b603-b83ec1394115 | -17.11645 | -41.34486 | 2026-10-07 16:35:00 | NPP-375 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9274c257-d85d-33ff-8858-cd7d229e21eb | -11.25828 | -45.1932 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| dfff2163-cce8-333d-b933-167c1073cdce | -18.34111 | -44.51331 | 2026-10-07 16:35:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e3e13000-cefb-384b-ab58-d2691c15b767 | -11.7379 | -43.66042 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a0b70504-8e16-3919-bb59-17b4c6f38f1f | -11.6186 | -43.67584 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f2f2e239-aab6-3da6-83af-a942888dbd58 | -11.84289 | -43.53426 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| adf0c8c3-dc91-3455-931c-809d423c1ee2 | -12.22491 | -44.72445 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 5e360457-714a-3a3e-8b69-9c55e0f11792 | -12.22435 | -44.70496 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f40a6ea6-a5a7-3b43-b761-3e777e9aa5d7 | -14.91128 | -48.08643 | 2026-10-07 16:35:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f7044144-15e1-35d2-99d9-c4fb95d9673e | -12.18353 | -44.75393 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8a58ea2f-8c64-3c56-954d-67db5f5d7c31 | -14.18631 | -49.59245 | 2026-10-07 16:35:00 | NPP-375 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 63506ec1-f81a-3107-b015-52de07321918 | -12.16189 | -44.72613 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| eac53d0c-8d00-3ce3-a95d-10680fe7fc30 | -13.68716 | -49.0937 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 133cc3f3-3697-3521-8111-60ce1af52cb4 | -18.0507 | -44.58394 | 2026-10-07 16:35:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a9c7d690-acd4-3694-8699-6cced8b770af | -17.0171 | -41.03453 | 2026-10-07 16:35:00 | NPP-375 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 7a24a049-fe49-3df0-9190-bd8b4b49c838 | -12.22322 | -44.71305 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8a2f6896-a3ce-3478-9e58-37dcf4557cfb | -11.83902 | -43.53128 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9e206a95-4e43-3e42-b691-20fe71952412 | -12.17832 | -44.76639 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9a69e3b1-6131-3b6f-8167-6df94fdb0f2c | -17.50134 | -39.30792 | 2026-10-07 16:35:00 | NPP-375 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 18b017fc-da41-3739-867c-b90bcabb8267 | -11.70449 | -43.66558 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| ba2b99bf-b20f-3a8c-8580-211798ccea00 | -12.21929 | -44.68648 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b33764a0-112f-3298-b696-371903bdac13 | -11.75089 | -40.35544 | 2026-10-07 16:35:00 | NPP-375 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 352dd072-3f38-3dbd-919d-4614fc7f3377 | -12.22855 | -42.11752 | 2026-10-07 16:35:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e9417ef5-6ea7-357a-b156-8be54cab9e95 | -11.84675 | -43.53724 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 263b7c50-f140-336d-9245-664b897b8195 | -14.94211 | -45.54002 | 2026-10-07 16:35:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 810157d3-5353-3f4d-8af9-56a889f90f99 | -14.57007 | -43.8362 | 2026-10-07 16:35:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9b658ea9-e335-3083-b24b-63e834cdc767 | -12.22147 | -44.72498 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| dd9287be-b645-3763-b627-cd6416014282 | -12.19425 | -48.42041 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| c7184dc1-e800-3d29-b6ea-52718584a413 | -13.69444 | -49.10333 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 66baed66-adb8-3c03-acaf-5da0f1b4b695 | -12.14476 | -47.84881 | 2026-10-07 16:35:00 | NPP-375 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8a87c91c-d7a3-393b-ae37-48d46521af9a | -14.90508 | -48.76262 | 2026-10-07 16:35:00 | NPP-375 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ab9d0e50-5ceb-3286-b964-cb81b2a8b5a8 | -16.89805 | -40.87945 | 2026-10-07 16:35:00 | NPP-375 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5ada362e-c78f-35df-9052-31a63045da96 | -18.1824 | -42.34572 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.0 |
| ed70049d-9cd4-3efd-9a62-b602312e8412 | -20.13801 | -41.69202 | 2026-10-07 16:35:00 | NPP-375 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e03f3d9c-d6c2-3d7e-89cb-905843579ad9 | -16.97126 | -41.21736 | 2026-10-07 16:35:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 511e0f90-21df-3664-bb32-d1e82b23314f | -13.34219 | -47.54513 | 2026-10-07 16:35:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 415c2f2a-bccd-33f2-9c07-bc8049dfa88d | -11.62671 | -43.61647 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| a6d8931b-17d3-3f38-aaa7-cd5324fa8b2a | -13.21171 | -40.08201 | 2026-10-07 16:35:00 | NPP-375 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| 1f43ecac-a8eb-3a46-81a4-6aaf0b41b235 | -11.26175 | -45.19265 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 63dc3598-ce38-343f-88ad-7fb260a30d7f | -11.85062 | -43.54023 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| e4299d44-68c5-3c5e-bd19-8be7106ccd8c | -12.7239 | -38.46479 | 2026-10-07 16:35:00 | NPP-375 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 516cd13c-40a3-3d77-9e88-c07fb9c45bf9 | -13.75084 | -48.12489 | 2026-10-07 16:35:00 | NPP-375 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 614cf9ee-7197-3b4f-9f58-9f27d566fc37 | -12.27426 | -44.42457 | 2026-10-07 16:35:00 | NPP-375 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bd9ac8b9-c40e-30ad-ba1f-012d8274bf77 | -13.42449 | -40.7985 | 2026-10-07 16:35:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1202d625-fde6-3c04-a41f-a746b43a9d43 | -11.22939 | -45.28825 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| b5e23780-d474-3e54-9fa0-b586a2acc4fb | -12.18231 | -44.76968 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 3ad7a705-917d-38f7-92a6-5c61328fddfa | -13.86115 | -39.52921 | 2026-10-07 16:35:00 | NPP-375 | NOVA IBIÁ | BAHIA | Brasil | 2922755 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| ee910264-e005-3cb0-a01d-a865cc83dd60 | -14.37086 | -55.02885 | 2026-10-07 16:35:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8c3172e2-9150-39c7-af0c-1bdbffcf256f | -11.51162 | -41.70693 | 2026-10-07 16:35:00 | NPP-375 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 3daf0ba7-9f61-30a7-b8b5-3f1c65836639 | -16.86027 | -40.596 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| b8243cf6-d467-35b9-8e14-c0dbc780eca9 | -9.71126 | -35.92668 | 2026-10-07 16:35:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 7cde980e-cf05-3a7c-bdaf-d145735780a0 | -17.28849 | -39.28803 | 2026-10-07 16:35:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ee11edb5-de02-3544-8f6e-254a1e588e60 | -11.77728 | -46.7816 | 2026-10-07 16:35:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| ff752c95-a0e1-3d9d-a173-8237b9abd804 | -11.22732 | -45.24908 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 8fc465ff-f61e-3269-8661-1259605348af | -13.89203 | -49.12199 | 2026-10-07 16:35:00 | NPP-375 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6883173e-b9ee-39bc-8f5d-3ce52ae1d007 | -12.44887 | -38.57576 | 2026-10-07 16:35:00 | NPP-375 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 07c11b7b-c035-3e9a-a818-e72951a40cb2 | -13.69952 | -49.10733 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 084394cc-3df6-374d-a9eb-7590faf962ab | -11.2319 | -45.25625 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 70a24bcc-f91c-3432-92a2-032a2fa1b786 | -11.84246 | -47.3765 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1b09d479-e02b-3d8b-b3c5-ec9d97463fdb | -11.9883 | -40.21836 | 2026-10-07 16:35:00 | NPP-375 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 1ebbff11-03a4-372a-bef6-06b9ca63be62 | -11.22535 | -45.28489 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 137c49d7-2bba-38d2-b279-168039dbddd8 | -11.40829 | -43.52007 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0e5f260a-10e7-313b-98a2-e1d25b8dcf8c | -13.3773 | -43.87316 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2cd7a1a6-3787-3293-aee4-c7b73f495596 | -12.73896 | -47.00478 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8d646054-74b1-365f-b29c-bb0dcb822fa1 | -10.87908 | -39.31745 | 2026-10-07 16:35:00 | NPP-375 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 4559eea2-6a11-3b26-985f-fb5f2ccaab35 | -16.84963 | -40.59408 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 9f661e96-1f27-358a-a646-12589b7c0cb5 | -11.7732 | -43.53859 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 67144bea-d531-38dd-9cf2-6968180da056 | -11.76207 | -47.74195 | 2026-10-07 16:35:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0c309e65-9286-3874-9e1e-2075856d165c | -10.45426 | -36.84593 | 2026-10-07 16:35:00 | NPP-375 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 47758c7e-f84c-3012-b7c7-b623af3db49d | -11.83626 | -47.33327 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 93d2ac3c-6ece-376f-99b0-888cf83b4cf9 | -16.89414 | -40.87639 | 2026-10-07 16:35:00 | NPP-375 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1594ed13-f489-3457-b930-ebea36a43930 | -14.61286 | -49.09619 | 2026-10-07 16:35:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85f07a1b-6f38-30a1-89d4-f8da7279fa49 | -13.68325 | -48.79916 | 2026-10-07 16:35:00 | NPP-375 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e2ef9e8d-f10e-3c57-b219-51efc5d08d38 | -11.22369 | -45.27328 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dc0ba1f5-0756-3c7a-9ff8-26a6bf571b51 | -14.18499 | -49.59547 | 2026-10-07 16:35:00 | NPP-375 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0887744d-6d56-315c-92ac-57702c179f78 | -17.62919 | -39.92089 | 2026-10-07 16:35:00 | NPP-375 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5fc152d9-4e19-3827-969a-9048d16ff6d0 | -10.9661 | -38.80466 | 2026-10-07 16:35:00 | NPP-375 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| e6f85ca2-4be6-3d5c-af96-979272ec6106 | -14.43869 | -42.28662 | 2026-10-07 16:35:00 | NPP-375 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 9056d402-043d-35b4-94e5-4ce35e0ffdc8 | -11.47594 | -39.60526 | 2026-10-07 16:35:00 | NPP-375 | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 97b4c4b8-372d-3c02-9ec3-742b7c2b69fb | -11.24074 | -44.85713 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9fcf7af5-55b0-39ee-a0b5-f460987bbecc | -12.23917 | -38.80282 | 2026-10-07 16:35:00 | NPP-375 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 250debc7-5ccf-3658-b8d3-62faaefc63d1 | -11.81603 | -43.52831 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e6b737e6-323d-3ab1-ad76-105a1ef10c4a | -11.61362 | -44.1474 | 2026-10-07 16:35:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 57cf0516-184f-3116-9188-49ba68981b05 | -12.44867 | -47.80755 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fb8a3ebb-25b9-30ff-a51c-3ee11e192ac5 | -12.21818 | -44.68648 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6f8c90d4-310f-3dfa-be53-e92a689a4319 | -14.7428 | -47.45823 | 2026-10-07 16:35:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README178.md)
