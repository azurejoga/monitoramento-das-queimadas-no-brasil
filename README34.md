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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33107b45-6fe4-38bd-849c-c1a343b1d397 | -11.80661 | -45.01131 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05d1c6ee-4c60-3b78-a813-bea748d5a502 | -12.03256 | -39.46334 | 2025-10-03 03:45:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6ca2b62d-9fe4-38b7-9f12-5d2fae78842a | -8.59152 | -44.77963 | 2025-10-03 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed88e333-79b8-3316-9875-6b8efe524cc0 | -16.34036 | -42.37946 | 2025-10-03 03:45:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef8d4f9b-891b-39bb-b376-0cd086a6ad15 | -15.21927 | -47.18467 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f624d42-79ae-3b33-828a-c49a27d68ccf | -15.30069 | -46.28759 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d12271a2-5b66-305d-b686-e6c564893618 | -14.19701 | -46.1165 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b738881-8c7e-3ab8-afdd-c8182260292f | -13.1238 | -47.84743 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fe815f67-1537-306e-94ca-16c864f6f05e | -13.1981 | -47.80385 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 755c9b28-c15b-33b7-ab22-fce7f00a673e | -14.41691 | -46.15844 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dae8ec13-7d0b-3462-be4d-08e2c5130816 | -14.89763 | -46.96679 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9881f641-40b3-32a0-b08a-e19438146dfa | -12.37664 | -46.51442 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d365163-d988-3c33-8d41-47a660cd995b | -15.60622 | -46.92485 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 798f7964-0105-321d-968f-9e5af016f63e | -14.43786 | -46.10601 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb1c1724-5ed2-3687-b556-186ef52ce3b4 | -11.22962 | -48.20379 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ab04059-d790-3cfc-8afc-e1e0b0edc06c | -11.62679 | -47.9909 | 2025-10-03 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 076bd72f-a2d7-369c-a11e-c64bf0baf7c8 | -14.28921 | -45.88826 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33e4cb4c-87f6-3935-8682-4997efc43e29 | -14.38159 | -45.94478 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f54f8f3-c07b-3249-88b0-5d7d9ac4393e | -15.35686 | -47.06813 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a14bde4-30b1-36d2-93c6-898934cf4e07 | -13.33054 | -47.59513 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b76bd56c-d92f-3ce3-928e-e10dd13d6da0 | -11.58996 | -47.63546 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 062ff50d-2413-324d-8bd7-da54f4a6260a | -9.90067 | -43.72446 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 897dad98-f835-364c-8138-2547f2df3658 | -11.11527 | -43.19199 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89e1b308-0c22-36b1-8b10-6b3d9e1e2117 | -14.59735 | -46.72672 | 2025-10-03 03:45:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d63f7e2-aa41-31d7-a33d-b1adb284003c | -12.41386 | -45.16388 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51e73715-4de9-3c0a-bfc6-ed48ec0ac0cd | -9.31885 | -45.9631 | 2025-10-03 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74faf13e-31a3-36d4-8599-0e61a220eddc | -13.54142 | -47.29334 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7107b9c3-c4df-3163-9c54-2d07534e07e9 | -13.16849 | -47.88925 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f080b0e0-bf9b-3b76-af4a-11bc6da91cb7 | -11.85615 | -44.96566 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b33217c-6e53-3791-b051-1763c0af125a | -10.75717 | -45.34398 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85e9ebf1-3625-3989-bf4a-ebe7bd8ec95c | -12.20872 | -47.78617 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96799b55-77ed-321a-8a29-2c81b0998c07 | -13.75597 | -48.08598 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8e7e54fd-8882-308a-97db-b896ba3cdef5 | -11.90508 | -46.26702 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28abb7ed-d84e-3627-b076-eede9259a184 | -13.55952 | -47.29089 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdbffa27-9634-3140-8e6f-914ef1b01de6 | -10.22887 | -48.2424 | 2025-10-03 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec541501-1829-3389-81af-9cbe8ea83ccf | -11.14676 | -43.38081 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 58a74478-eb7e-32f7-b7f7-76ded2a4118e | -11.34839 | -44.97131 | 2025-10-03 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23106170-075c-3221-92f9-e839259d67f6 | -10.76364 | -45.3384 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c1f5e90-12ba-32b7-ae0b-15247b7db6f6 | -12.61855 | -46.96822 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0e6c6af1-eae8-30d5-b485-6e2920ff48d5 | -13.13478 | -47.88462 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 358e69f2-1804-35c2-9eaa-3c179065d3fd | -13.34207 | -48.1297 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b371a73-65cf-3b10-b860-788cc0bbd062 | -14.89936 | -48.34084 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4025bf8b-6a05-3c18-99c0-1cc70923b233 | -14.70547 | -48.2016 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdd0aa47-fb39-3471-a363-6df2955a130c | -13.15135 | -44.53162 | 2025-10-03 03:45:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1d694e3-b516-3559-b240-ccea3247c3ea | -12.12459 | -43.43699 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b41d24f8-f251-32b8-9218-91f2140e6eda | -10.3529 | -43.73258 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73454918-6be3-3368-b4d6-9b595c82f254 | -13.75695 | -47.98103 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b89ec728-d1b4-3882-bbaa-555d85bad16f | -11.50206 | -43.50755 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f44d77d-c4b8-3514-9a1b-ff0fe434691f | -13.46313 | -47.22993 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f24493a5-6c24-355d-9a37-3690e8ba167e | -11.1469 | -43.4065 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e465c812-6abd-3f26-a7a6-31168d929ef7 | -12.36893 | -46.5247 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce8dd2ec-cf74-3198-92eb-76a9ca31ed7c | -12.11469 | -43.44029 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5d1d7a8a-5006-3e39-923f-d2e778896f22 | -14.94205 | -46.91273 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7da630b6-5a2c-3bf4-8de1-a2bdaf2260af | -15.2198 | -47.18762 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 162a2f99-1289-330f-b440-d8c3df9f7cde | -13.12295 | -47.85167 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| de2a070f-77e1-347d-97f2-437a6793c5d9 | -14.01334 | -44.96988 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1ee724ec-e1d3-38f1-95c4-58daa11ec170 | -16.33644 | -42.3788 | 2025-10-03 03:45:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34549aaf-da25-39bb-9668-4e508208afcd | -12.89126 | -43.13197 | 2025-10-03 03:45:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 391c376f-9fa2-305b-98db-f022f2a3c772 | -9.92248 | -43.76686 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 47d03bac-b2f1-3bca-8e58-95d99983595c | -11.91114 | -46.26492 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ddd76a3b-4155-3120-bdaa-615b2c93537f | -14.45627 | -46.34506 | 2025-10-03 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2540118c-7582-3591-91ae-1489437b505b | -13.66518 | -47.30408 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 52cdb51a-f2ad-3064-9d55-0c2f81097ecc | -12.93046 | -45.08885 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 604798b6-d252-3b45-b872-0580e5483475 | -10.87816 | -47.82604 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dc9dbd6-8f6c-3859-afab-679aeea46f64 | -11.3489 | -44.96862 | 2025-10-03 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 568a3a1d-6e2b-332e-95ed-7a0f6dabcf5a | -11.68248 | -47.49857 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16ed6b94-f8e3-34f1-a6dc-1db266edf69a | -10.86559 | -46.67053 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 08164d3a-5d98-391b-8753-8c9ae4f2564e | -14.19762 | -46.11337 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 307b41da-f9eb-30a1-be7a-d6a5a66098b8 | -15.35138 | -47.06753 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75b6886d-09d0-3af6-8f90-53de6ea8883e | -14.91128 | -48.34249 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 160b4ef7-d192-33d1-b99e-23a277377354 | -13.1444 | -47.83619 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ceabae15-6948-3431-908e-fde005fd9dd8 | -13.96734 | -48.11059 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aef32387-b0c8-330a-af09-77d6e2590a1d | -12.67541 | -46.85612 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c88ef401-6fe2-36fb-9bac-a829e86a54e6 | -11.63163 | -45.05802 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72a7c51f-b33f-335c-ae80-f5eb905683e4 | -9.7575 | -47.81676 | 2025-10-03 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20229bbc-e260-3cc2-b1f4-7a33765e6e46 | -13.97334 | -48.16044 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4bb82ae5-6df8-35f3-bdee-e33dfa5ef523 | -12.37737 | -46.51069 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba2e10cf-8325-3a25-ac59-f4ab7965011a | -15.58994 | -46.9331 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18b8a58d-1c95-3a52-b8bf-9792a8e4c0db | -15.82927 | -46.24647 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5d16b37-4143-302e-9093-e668aaa6376b | -14.90304 | -46.96782 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7238a463-edda-32d0-9b32-fa70061d3bd3 | -13.68074 | -48.03255 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d28bdca-bb61-32bd-a5c8-28f9acb03563 | -14.92941 | -46.89202 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 94d4dab1-3f13-307f-950c-26405e713124 | -11.55623 | -47.64875 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bace34fc-c47a-391d-8167-61b7ef72534e | -11.16417 | -47.17907 | 2025-10-03 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c3274b6-0765-32e0-ace6-c364e58eee18 | -14.90707 | -46.97572 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e393cea-0c9a-3e0d-aeca-5595fd9035a6 | -13.23497 | -48.49539 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7bfa9e4e-e40a-3c96-a3cb-b9ffcdb4cac5 | -15.37482 | -48.60088 | 2025-10-03 03:45:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0007ba25-0b31-3d83-a74d-1b5e94e053d2 | -10.30633 | -48.28345 | 2025-10-03 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1592c5ed-4343-33ac-9a9a-5a665b02bf9c | -14.65434 | -48.24956 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eeee0619-f2e1-38c2-8fca-fba50cacee9f | -11.09855 | -47.86839 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab14bd7b-c8d9-3b02-98eb-f4872284013a | -13.26073 | -47.25946 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4067f13-c80a-3e52-b7b8-564017e3d769 | -15.80605 | -46.25725 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19a61978-37c8-375e-8e31-767a55bc878d | -13.33989 | -47.21675 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4bbb32b9-f950-332e-ae27-1a86580b8781 | -11.49312 | -45.00147 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6d9e488-a42f-3ad9-a370-a579c535e042 | -14.379 | -45.94528 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| deedb41b-53ae-3591-88a7-1e977e4a2067 | -8.90689 | -45.04209 | 2025-10-03 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8319c283-2c3c-3c66-aeab-f52d03259d16 | -9.92554 | -43.7233 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 947a8f48-8580-31e9-aead-1e80055dadc6 | -15.57527 | -46.95103 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d4b7385-f139-3629-afae-524cf38bc3ec | -11.86816 | -44.98431 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9b4aa3a-2598-3fe0-a12e-08862bb37b2d | -14.88815 | -46.84735 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README35.md)
