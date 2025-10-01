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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba1f0733-ec84-3c8c-8a0d-0515c3cc8e84 | -9.39991 | -54.71734 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a983d8e4-67c2-387d-a7a7-f1774e3779e7 | -12.56523 | -43.42363 | 2025-10-01 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee05f629-6b30-3053-8d77-df758b6120f2 | -11.86769 | -48.0196 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65c297ce-f3cb-3d20-92ae-866d78768ccc | -15.26175 | -49.26988 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d05b8624-f7c0-3956-8320-d5c95d675b34 | -13.31326 | -47.21407 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e8a8794-58df-352b-96f1-fb31d7aa47a2 | -13.99823 | -45.0367 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f06c307-afee-38f5-9543-bbb0b0362ae0 | -14.75254 | -45.7766 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d02924c9-8577-399e-bc1a-06f9a4d766c2 | -12.1754 | -51.42094 | 2025-10-01 04:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6737989e-0a61-3661-8e85-c519713626d3 | -14.59739 | -48.2257 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e76557ed-05a8-35c6-8f9b-f85cb46cc67d | -13.76687 | -47.97091 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3529105d-e310-343e-abdd-e4409f1dbfb8 | -17.2056 | -46.97966 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b328eeb-0130-3d5d-98cb-2c6e2f39b0b4 | -10.9488 | -44.33008 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cee3c1a-c585-36b3-bdcd-2821a49a613b | -12.74925 | -41.82094 | 2025-10-01 04:21:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 171c069f-7987-3476-b8d8-1a7488098d34 | -14.18729 | -46.11359 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc990677-afcc-3106-9139-5c269cad6cb9 | -12.2297 | -53.87787 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14c11ac6-42b0-36fc-861c-8ac8a3a1cfed | -13.24636 | -47.31346 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf982ba-99cd-34a2-a092-c403cd0fc882 | -15.30082 | -46.19199 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63116b4d-6529-3e17-9700-b20bae410e1f | -13.23079 | -47.32537 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66bfec42-2868-3de0-b879-8e69cc747b28 | -11.45437 | -45.02631 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d42dddbc-357c-3f24-8fd9-83735526609b | -12.78417 | -46.86013 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c622b8ee-9413-3b90-838e-593d7557b61b | -14.59759 | -48.30973 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e13b5f91-8eef-3f86-8cc7-2abd9acad19a | -11.2755 | -47.81358 | 2025-10-01 04:21:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1233c1f2-cfb2-3dc7-a263-971d21a02d9b | -11.82416 | -44.96427 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07d8c611-511f-3335-b979-a46ee6894b40 | -11.85198 | -45.0052 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1897d589-c366-384c-b960-051ea105eec5 | -15.47576 | -45.86991 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d421098a-5e34-3bb4-893e-1e4729da6f1f | -16.37078 | -47.03493 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38807896-5a62-385e-846a-ed49824cd6af | -13.67266 | -48.08083 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c368b448-d91c-390e-a815-bc9ccdf4919a | -13.34054 | -47.86908 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73553938-5036-378c-b539-6a3000917e31 | -12.18011 | -51.41799 | 2025-10-01 04:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd48a610-dc15-30a5-bc04-d8b080f9f28f | -14.74867 | -45.77968 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b054deab-21c4-33a4-8fe8-54eaa2f40e00 | -9.42836 | -54.71193 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e8f55e7-ee25-375a-8781-eab8978b357c | -12.83764 | -47.03658 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28da246a-202b-39e3-bf8f-1f978d21784d | -10.38959 | -48.14082 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 25087b93-4340-3997-ba94-5400a2182c7d | -13.37472 | -48.15775 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e34b6b3-f7bc-3996-b802-97d3a81e9479 | -15.24962 | -46.97883 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c3ce746-3016-3d40-b3b2-663182f9ca2b | -15.35559 | -47.08385 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 59c9a352-106a-35e6-b610-103ff186a4d3 | -14.43857 | -46.358 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 133bb2fd-b05e-34a0-a12e-ea3d53837458 | -17.20891 | -46.98021 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e541fc6e-a437-3704-80db-b00ef298c503 | -11.19934 | -47.76209 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bf1bd334-40d0-3feb-b026-4c06bb05d10d | -13.97653 | -44.88203 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56c0c7bf-fb55-3d70-b638-7504e5bbcf4e | -12.84432 | -46.86626 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca3db96d-cab7-3ba6-b34b-e3b98ac0debb | -10.35052 | -43.7421 | 2025-10-01 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2b5623d-e37b-36a3-8ef8-bb358132c760 | -15.17301 | -49.08552 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 211ca808-71a0-3efd-ba2e-7355fd5f1892 | -11.36674 | -44.97649 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b83d3d7d-1d03-3a59-8338-64155a8036d4 | -12.24276 | -47.78945 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1a6f6c0-f973-339e-a96d-2078a58e363f | -14.71957 | -48.27264 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fed7234-ab72-3a58-a0e3-e8dc275350b9 | -13.77765 | -48.0112 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 150c0f2d-6d6b-3d5f-81e4-eab0c3a83fea | -13.98619 | -44.90998 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 657ae4f4-d450-309b-a65d-17ad2b515725 | -12.89277 | -45.26785 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a9f7c78-2dff-3e87-b3c5-3ab303a0dee0 | -11.79839 | -46.61441 | 2025-10-01 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 18c4b92e-3411-3c92-b3f2-ada18aa667a9 | -14.59819 | -48.30606 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21b7c846-d028-38df-9a12-922881f042fd | -16.24317 | -44.06322 | 2025-10-01 04:21:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c9e5ad2-9eab-3fc4-aa84-90c0327461e1 | -11.4339 | -55.05467 | 2025-10-01 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 464fdda4-30ca-3e63-a7da-b4e38207af99 | -16.13059 | -49.145 | 2025-10-01 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08b01d43-d934-3695-bcff-697764cc9bee | -11.85646 | -45.02043 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 57abef41-c5ce-395a-b379-46ed52a467fd | -16.42921 | -42.40836 | 2025-10-01 04:21:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4113a31b-27b2-34aa-bc8b-a35a106a9e3d | -14.76248 | -45.75607 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75962428-5305-30f5-954f-b3d635acdfa9 | -11.84474 | -44.98577 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96264e80-c9df-352e-9b87-a4533283d250 | -14.50251 | -48.4436 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c57dc4f7-10a5-38db-a41f-be36a7c14478 | -15.60786 | -46.91071 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 596f92cb-c71e-3beb-a6e5-e851d8128c62 | -15.83842 | -56.39019 | 2025-10-01 04:21:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0d0c941-94b5-3bb3-ad4e-39e4c32b9833 | -15.29925 | -46.4003 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdd49c40-8fe1-3835-b61c-56debb53462c | -15.38828 | -49.18747 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b10ca96-e3ce-3309-b838-ee77a2294474 | -13.2981 | -50.65668 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89ab5639-2f8f-35d7-91a8-70d5cc7ef44c | -11.81199 | -44.97699 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 317d5274-44d2-3bea-a5fb-8dea29124e1d | -11.85313 | -45.01987 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 28d42704-c94d-369c-892c-42f54e0f2632 | -11.4486 | -43.51777 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f421bcd-a382-324c-8e3a-6bb3055ad53a | -13.45794 | -47.24573 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 299ef59d-c563-303a-a3a2-36d38bf7e85e | -16.19666 | -49.99525 | 2025-10-01 04:21:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 86709413-6451-35a1-9651-28da30a7f619 | -14.69057 | -45.28721 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8626f90-c9d6-3ea8-ae4b-caf846104b22 | -10.4471 | -51.26712 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5a16705-a130-30ec-8e73-d283123385f0 | -13.41669 | -48.15704 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 862ad80f-99b6-3edd-9b9c-50c4faa990d6 | -11.81182 | -44.911 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 618a94dc-feed-3572-a2c8-613052060b28 | -15.24052 | -46.22999 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc7c202a-b0d7-3cff-ae50-4590b7730814 | -12.79074 | -46.88292 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e08c934d-9b7e-344c-bf5a-99d6f36045c7 | -14.90381 | -51.67352 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 27aeae6d-d048-3891-9765-458e271f7b53 | -10.28839 | -50.46492 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 15a94e7f-2ba0-3994-aa6b-96ba8967ad02 | -10.82336 | -47.95672 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5f94b616-8c46-3ff9-a39f-1b9d5e0240e6 | -13.67572 | -48.06225 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd09d2ab-3382-39a3-9ee5-08b2ae15cb86 | -14.71069 | -48.26332 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cea1f87-238a-30f5-aee3-1ed45283833b | -10.90865 | -46.55874 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 83dc9a3e-bbe8-3a1d-afe9-44f757914eba | -11.82967 | -44.95053 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 776d4190-7b95-35a3-8e91-b715b4f9c740 | -11.14846 | -54.31119 | 2025-10-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8835d017-fd25-3ac4-adb6-608edb5c468d | -13.33228 | -47.85613 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 49256ff7-6bc2-342d-8021-e6051f9a3032 | -15.76635 | -43.67704 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a838234b-33ee-3f5f-9aef-bc4c78581c3f | -10.90504 | -47.62586 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b71e08bf-dc47-389c-8712-aef3c9c61c53 | -13.33106 | -47.86362 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17c8546e-45aa-3bb5-9e22-106026b5034e | -11.98701 | -47.01259 | 2025-10-01 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7b161aaf-b9b0-3ffb-baa7-2916fb563c55 | -11.85585 | -45.00215 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 15c757f6-19c3-3025-abe8-71ffb90810fb | -15.29751 | -46.19146 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1082d456-d565-3788-b585-c5eeff3bf12a | -15.76275 | -43.67649 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca7b7220-3828-3d41-8b9e-c5ba0634bbdc | -12.76892 | -46.91223 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c311b2c-bf01-3227-98bd-640f8ec6ac69 | -15.26107 | -49.2739 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9d88dc6-9b28-330e-bf64-6c88c9c04b8a | -13.58438 | -48.03952 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 91505656-65ed-3f6b-98d5-8888765c77c9 | -15.6716 | -45.24185 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31529e18-a44c-3911-9143-eb190a5148a7 | -10.83813 | -46.65985 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed965769-69fb-369a-9f5c-eff7d4c2241f | -14.75989 | -45.21503 | 2025-10-01 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48013571-25e8-30a4-b005-44be927f7594 | -11.20423 | -47.73181 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c201495e-020b-3b36-996a-31cd01485898 | -15.75804 | -43.73686 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 513363ff-5e58-3796-873a-6b5ec9861dc7 | -11.81702 | -44.98872 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README66.md)
