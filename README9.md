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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3e09f89-252a-35b8-a7bb-fe67ca43aa88 | -13.43341 | -43.85756 | 2026-08-05 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 06adfcfc-e651-3e69-9b9c-57971f717075 | -15.43928 | -41.37967 | 2026-08-05 04:02:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d35ec09d-c3f2-3b82-ae34-63e1484df091 | -12.57863 | -46.94967 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 1c1af9f2-c377-391f-b50a-1a5166a46d84 | -15.4426 | -41.38025 | 2026-08-05 04:02:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fef3263a-05ae-34a2-8d9c-5adc2ecdbd4f | -10.63469 | -47.48299 | 2026-08-05 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3bf1bd5a-2353-3e8b-85bf-cc8620496d1b | -17.33597 | -42.63412 | 2026-08-05 04:02:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c2d3807d-7743-3864-beb9-68073b5103ff | -9.60312 | -47.76835 | 2026-08-05 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 237d2fb0-3caa-3b63-90e4-75880ce6325b | -12.43482 | -50.52401 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4a9924a-bf91-3937-89b0-5cf5c452e3cc | -12.44467 | -50.38196 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5caa6cf2-1113-315e-ae73-a01c45a2c568 | -10.91776 | -50.42377 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e97ad83a-2126-3cc1-8b05-06b9eec77e2a | -16.54959 | -42.65529 | 2026-08-05 04:02:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c77d4742-0ec6-367c-9f1c-483279e6f127 | -13.43733 | -43.67939 | 2026-08-05 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8209deb2-4f8a-3b6a-b337-244a75acbd8d | -14.17481 | -54.41249 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fad690ae-2e9f-32a0-a393-faee423c1c7a | -14.18943 | -54.44525 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd6a1ae8-fb80-37e2-bbf4-742ecbe9c133 | -16.92555 | -44.90973 | 2026-08-05 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4576ecfb-ec34-33df-a169-ec9996de2cc0 | -10.65458 | -45.22494 | 2026-08-05 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44c6f9f2-9691-3323-99e8-9fbe300bcd86 | -11.10906 | -50.40269 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6e98f81b-8a9e-397f-8612-74b91c5fc4ce | -14.02702 | -54.08289 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efec8b85-4638-3795-a59b-cb18c44bf370 | -14.1899 | -54.41059 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e14b86d2-2a38-3a71-866d-81cda50b4ca7 | -15.44924 | -41.38141 | 2026-08-05 04:02:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 92599e35-a38e-39d5-8e21-52c8f8c9c80d | -11.55092 | -47.71007 | 2026-08-05 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b75477ec-d329-3d12-bc90-8a29f70be36e | -13.24897 | -54.27001 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26731a6b-3220-3a52-8523-3da18138e8e0 | -12.45114 | -50.37915 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 351d94d4-23a1-338c-bf18-52f61f9f6f3b | -12.59829 | -46.9199 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ae63aeb-298c-377c-b4f9-eb988f8a2680 | -12.4355 | -50.5225 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50b8fd74-ac72-3528-9ba8-2dc5f225bd96 | -15.44592 | -41.38083 | 2026-08-05 04:02:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| edbb038f-5a93-3b5c-becf-4d61220afd96 | -12.59286 | -46.92386 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d0c07c5-25f1-3f29-b01d-726eb918543d | -11.51819 | -43.24768 | 2026-08-05 04:02:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 22faf4f0-2b74-3dc7-ab06-c3eec8cb243d | -14.19362 | -54.42666 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 833bf813-b837-35d2-9388-fa7e7b0e007c | -12.60374 | -46.91584 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 315104e3-834f-3af5-a205-a2846ba211f4 | -14.19767 | -54.44126 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 855c544c-9cde-33fa-a102-a37237f47346 | -14.03759 | -43.85504 | 2026-08-05 04:02:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32e5cd29-e2ae-3b8f-a297-56017c428d49 | -12.6 | -46.91077 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48b8bd91-eb7f-3d29-a626-aa3b7c146086 | -12.59544 | -46.91005 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c0aa637-d44b-3438-b1a2-8445c363b865 | -12.58864 | -46.94645 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 19ad2635-a86c-3fb1-a8ca-fcca8c676caf | -16.00376 | -48.16339 | 2026-08-05 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 727a4286-94ba-36be-9634-c0aed1b17f30 | -11.10491 | -50.424 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7668706-58ce-3630-965c-d446f8c0f2b2 | -11.55814 | -47.71066 | 2026-08-05 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86ff4bd4-e24c-3172-a064-f909fb2dfb13 | -14.1784 | -54.40738 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 46042ff8-ca75-3f99-ba57-49f95cf5f716 | -10.45348 | -50.22663 | 2026-08-05 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e68c457-a4af-3295-a659-eac99e159dee | -10.7559 | -42.09142 | 2026-08-05 04:02:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c09445b-d3dc-3474-a8a0-2a210bfae045 | -12.92689 | -49.482 | 2026-08-05 04:02:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4b77653-16fe-3ab7-b8f2-e64090d023eb | -17.33997 | -42.63095 | 2026-08-05 04:02:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3dafd2bf-a351-3814-a123-a5ebe29ed5e2 | -12.5841 | -46.94556 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1996e390-8b9c-3f30-88c3-8a1d4dde6300 | -14.26327 | -45.30003 | 2026-08-05 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca6b094b-2d02-344d-81c9-94e03c697d7e | -10.9119 | -50.42257 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f00cf74e-1b68-30b0-8071-d922d6099a17 | -14.18306 | -54.40844 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0bf7a15-94f0-3a76-86e1-bd49d4687b1a | -9.14149 | -49.66468 | 2026-08-05 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 084102dc-e9a3-3d55-99a9-f9a26a584a97 | -14.18497 | -54.44429 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ee18113-6fc1-3e44-998e-16c243d77ad5 | -12.4812 | -50.38406 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 526ba306-4b05-3668-9314-1867e53b7408 | -13.44173 | -43.67569 | 2026-08-05 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| ebd367fd-11e5-3c76-ab00-5ff38727956e | -10.45931 | -50.22783 | 2026-08-05 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f93ffa8-64b7-3a82-a489-de4b5dffca2a | -11.03987 | -42.752 | 2026-08-05 04:02:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2120830-278a-3556-a7d7-5a6004989ecf | -14.71299 | -47.14593 | 2026-08-05 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e74c791-2944-389e-a0da-67be0d247ff3 | -12.6021 | -46.92464 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d581518f-b533-3f47-85c5-97908bd4ad3a | -12.59663 | -46.9288 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22e32048-012d-31f2-95f9-ff9b946c2ccf | -17.3326 | -42.63351 | 2026-08-05 04:02:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b4940989-f0a7-3c1c-ad21-a4229040f772 | -12.58743 | -46.9278 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b32b0a05-7265-3fa3-88e1-8c471392e401 | -12.48039 | -50.38807 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c00bdbb7-faec-3353-8c36-f77c51b4ba97 | -10.91689 | -50.42807 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6792be85-465a-365e-9f1e-49f73a974e08 | -12.59457 | -46.9147 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9bbca592-9e1b-3441-9373-ac0a21bf893e | -12.43642 | -50.51579 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8d0478f-a414-3d4d-b55f-f88ed1f535b7 | -14.15773 | -54.40146 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1ff0ef4-cc2e-3254-af76-1bb54ead7148 | -10.74317 | -37.07722 | 2026-08-05 04:02:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7168439a-b2a2-3616-a018-db94a6ce45c8 | -10.14042 | -46.36516 | 2026-08-05 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d449999a-97e2-3720-bd84-c102e20b0264 | -11.04398 | -50.43208 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fa34860-1d15-3bfc-95b6-767af801e262 | -12.14242 | -48.26447 | 2026-08-05 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e27f460-b7e5-3fbf-9113-22d54b73feea | -9.60257 | -47.77133 | 2026-08-05 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d9a5d50-0e45-32ba-ac6f-440cf373bdc6 | -16.92636 | -44.9051 | 2026-08-05 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bdb57cc-b4fc-3a53-b123-d6a286e2f922 | -13.43787 | -43.85371 | 2026-08-05 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 563cc1fb-c2ad-31d5-a010-2d560bcd109c | -14.85968 | -46.79796 | 2026-08-05 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24b39e09-8134-3011-bfd7-6f2d0e295cf3 | -11.52186 | -43.24833 | 2026-08-05 04:02:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fc8fa788-daf5-32de-b019-05784bfa28ef | -11.04347 | -42.75262 | 2026-08-05 04:02:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0fa405b-dc1d-31f4-9cc2-094ad8bf1576 | -9.14685 | -49.66738 | 2026-08-05 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a413476d-5a83-3b93-b1c6-552580074fd5 | -12.19979 | -52.87209 | 2026-08-05 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8066835e-7249-3150-b03e-e145b0dfa668 | -13.43807 | -43.67501 | 2026-08-05 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 672927c1-6687-3de4-a348-d9c3a3fb748c | -12.58497 | -46.94093 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b881fb8-ad90-3862-9a8f-18bec409d78b | -10.63372 | -47.48841 | 2026-08-05 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d896b8c-681d-3602-a560-002642cce2e3 | -13.242 | -54.26814 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c90f6fef-b546-36bb-9507-50c199cad91a | -12.46983 | -50.38165 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdb4a018-cd99-3d2d-a41c-e8a178306180 | -12.49308 | -45.54439 | 2026-08-05 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d2bc4b36-86e5-380f-9353-9455a70c124b | -9.14107 | -49.66635 | 2026-08-05 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e327e3b0-52af-346b-99ce-6cc04276d0bb | -15.40493 | -42.31783 | 2026-08-05 04:02:00 | NOAA-20 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee571403-0c2a-33d8-a7b6-cde8f5f249a1 | -9.60816 | -47.7694 | 2026-08-05 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7b3c234-1508-37f7-bdf3-db6671a1c0ed | -9.14182 | -49.66226 | 2026-08-05 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d030194-eee5-3459-ba84-28aed8e1a156 | -14.35304 | -47.51774 | 2026-08-05 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb7f29b9-e1ae-3635-874d-9f89ecb900a1 | -12.44536 | -50.50321 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 434f5d51-7c0d-31c5-9693-38ecdc0f18a4 | -14.25931 | -45.29929 | 2026-08-05 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6932e752-221b-3135-93d1-d83020e10584 | -10.79135 | -47.70827 | 2026-08-05 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b34f5987-5fa1-3499-b719-60c70862a28e | -14.17704 | -54.41358 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1266d93-f8bd-3076-8f65-1983d483f54f | -12.59121 | -46.93271 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9816651-60e3-341a-a680-0e3f54476fa2 | -9.60761 | -47.77235 | 2026-08-05 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e28865d-949e-38f2-9198-640389eff99a | -14.38268 | -45.85239 | 2026-08-05 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 909aa86d-b923-3ecc-86a8-a87800462000 | -12.49078 | -45.54212 | 2026-08-05 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30d8f1ef-f4f1-3226-bf9a-a4feb21fad40 | -14.02852 | -54.07603 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ab42166-2604-3ab8-a46a-9cd21a9ea80c | -11.10823 | -50.40695 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f74668ae-9739-32f9-8e33-6386167c940a | -10.9133 | -50.42497 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c583b2dd-f2ef-3c4b-963e-d7bbd5e6cebc | -14.1918 | -54.44661 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7427e511-811f-3adc-ac7c-9165349579b5 | -10.79051 | -47.70694 | 2026-08-05 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16e96049-c210-3f33-bb83-eb51a6b55900 | -12.58952 | -46.94175 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README10.md)
