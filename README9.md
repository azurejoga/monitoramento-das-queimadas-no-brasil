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
| 3ac59c04-a338-39d9-b5c0-ce075991750b | -7.6138 | -45.75425 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7b0157d6-5c03-31e3-9c36-c3b0c6064a58 | -7.16419 | -49.51133 | 2025-07-02 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa935d3a-986c-3285-90ae-d45880362b23 | -7.30509 | -45.37297 | 2025-07-02 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ae13813-0171-3095-a46a-9c546713df14 | -7.80108 | -44.0246 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3139046d-0ca6-34b3-a4cd-14c28fef8d3e | -6.27791 | -43.68186 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 07451078-68d3-34a8-b236-7a294201a380 | -7.09447 | -44.3819 | 2025-07-02 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44569985-dda3-33de-98eb-45a28ac4c2ad | -7.8052 | -44.02116 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 0f40ac34-bbdd-386a-b325-756d2eac16d2 | -7.78699 | -44.02243 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 019d424d-f646-3c5d-bf97-1666402c23c8 | -7.78819 | -44.01449 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3b72fde4-5e14-34f1-906a-dbecd9a7985e | -7.88075 | -47.89243 | 2025-07-02 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd88b43a-87d2-38af-b864-ad9e0d34f604 | -7.80803 | -44.02927 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7f5926dd-ca65-3891-8aa9-2416564874e9 | -6.54385 | -55.03101 | 2025-07-02 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1df8bbc3-d487-338e-a54f-f692ae992ccb | -7.0841 | -49.59888 | 2025-07-02 04:25:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59155bc5-f5cf-3bf3-9011-b4a3a22bc394 | -7.22211 | -43.0983 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 18d11c01-36cb-307e-94f5-24bd55dcc024 | -7.79051 | -44.02297 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cac378f9-0b35-3d3c-a73f-7cf12c821baa | -2.91281 | -48.23844 | 2025-07-02 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe885d9c-6673-34aa-8f68-26e1193e2e63 | -5.935 | -47.92814 | 2025-07-02 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c3af8ac-a46a-302a-bf71-b0f1aff201d6 | -2.89799 | -48.03022 | 2025-07-02 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f57bcbda-2734-3d2e-94e0-dd91ae4ab807 | -4.67461 | -43.24439 | 2025-07-02 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ac7d616-1d7a-3382-aae9-d550190b2396 | -7.18692 | -45.47868 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d2383be-4ae9-3f83-9cd3-9c42c00d16c2 | -7.78759 | -44.01847 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3b902083-3669-370b-a656-9a975cd598dc | -6.28967 | -43.67558 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e5ab6373-e00f-3546-9366-fca8ad31de3d | -4.17627 | -42.02859 | 2025-07-02 04:25:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7b46681c-82a9-3d99-ad6c-c9c4f01bd55c | -6.84824 | -42.79388 | 2025-07-02 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f0ad88ef-f195-3f7b-a83b-14e192842d78 | -7.72853 | -47.39519 | 2025-07-02 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17389ccb-ab79-3c14-8cf2-28b9ac3afbc9 | -4.5399 | -48.01837 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5464acae-1c0a-3916-aaab-01fb926b2089 | -4.82669 | -47.32228 | 2025-07-02 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 208eace8-5689-3d1b-af11-3462969ed9dc | -7.80047 | -44.02856 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 10cac702-18df-3027-985f-bc118d4a277c | -6.53414 | -55.02632 | 2025-07-02 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf8c713c-4148-3193-9b34-d53b0b07edcd | -4.0292 | -48.06962 | 2025-07-02 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee848a2e-9149-35b3-88c5-59c34c3ff905 | -6.66573 | -43.84906 | 2025-07-02 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd00a8b1-5577-3bc1-8e8e-bdbc05371d9d | -4.37711 | -48.06934 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 148e1703-60a0-3887-857a-f48ae93cd028 | -5.7826 | -43.62636 | 2025-07-02 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2db9dfcc-d01f-3d0e-afab-c226a30c037c | -7.09161 | -44.37757 | 2025-07-02 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9d221eb-2463-3576-9302-8cbd97310a01 | -5.62237 | -43.65906 | 2025-07-02 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 557cf0fa-77fb-3e4b-add3-e6b9f5839c39 | -6.214 | -44.1982 | 2025-07-02 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 956f13e7-2e90-3fea-8943-45c2db38aa95 | -7.29707 | -44.56955 | 2025-07-02 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac9f3c3c-da4a-30ac-a4e4-8c5c227431f2 | -7.30325 | -45.10126 | 2025-07-02 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e91316cc-6f8c-3f14-908f-c4531094bfc6 | -5.61945 | -43.65466 | 2025-07-02 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 671db92e-2653-31b0-b048-33dfaf0689a3 | -7.285 | -45.36989 | 2025-07-02 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 462b9ac1-8185-3c27-a051-b2051aa01104 | -7.79876 | -44.01611 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 42671901-eba8-387a-9c31-1715e223d09e | -6.76563 | -44.69923 | 2025-07-02 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e07411eb-887e-3c0f-9944-cf03dcb48568 | -7.81214 | -44.02584 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b57df46c-f743-397b-959a-582475213b3d | -7.81508 | -44.03036 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 9f478a66-b278-3027-ba34-965661120232 | -7.61488 | -45.74722 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e6940ed3-fc52-33d2-b0d6-0e0a414f1fe2 | -2.9926 | -47.45348 | 2025-07-02 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca1da606-d61c-3256-879c-87d4ab7c024b | -6.25253 | -44.83786 | 2025-07-02 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3323b6f-ada8-3e3a-b09f-962da9561c24 | -2.98919 | -47.45296 | 2025-07-02 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f424cfa-89e9-3203-8081-afbb35734e11 | -7.19912 | -43.1784 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63092858-eebc-374a-8942-f443a8cecf0a | -7.21175 | -43.09227 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| ab7cb9a9-7192-3206-8b01-13a8565f65eb | -7.81224 | -44.02224 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 69451742-589a-3ac1-a54d-d4ae8b2ec684 | -3.90152 | -49.08518 | 2025-07-02 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25717afe-b615-3b99-a502-c193d765fa54 | -6.28848 | -43.68349 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c01dd126-31d9-336b-a9e0-8742eac932c1 | -7.79403 | -44.02351 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8162bc3-8703-3b62-aa0b-3975789e01a3 | -7.8092 | -44.02131 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| e60e4bbd-8658-37b5-9f34-74d709bfc9b7 | -4.55939 | -48.00613 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e597ea6-3dce-3bed-886f-0b30c89af76b | -7.80812 | -44.02568 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4b274002-3198-3b6b-be26-9ddffc55fd55 | -7.79816 | -44.02008 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b547ffd1-d38f-3b78-a683-87a5fde62722 | -7.37194 | -43.8697 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d4df6ed-8caa-321a-88d8-5e83d9bcd453 | -7.79756 | -44.02405 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5be58c10-9f7f-3e4e-93d0-e7a0198c11eb | -5.57291 | -45.20737 | 2025-07-02 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2199eb2a-184c-3101-a61e-1bd3a9f4b90f | -6.8489 | -42.78938 | 2025-07-02 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88931ba5-bb52-3472-ae74-e4b14dacf096 | -6.0229 | -49.22756 | 2025-07-02 04:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bc102a4-64ee-3deb-974b-88eda13af448 | -4.38054 | -48.06988 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e459b620-2960-38bd-b765-2df284e1082b | -6.2926 | -43.68007 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cde41660-1e57-3f8d-83a3-0a76a55f3fe4 | -13.36177 | -46.19698 | 2025-07-02 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9dc4dfda-00ba-3927-8e41-015f5daee3ca | -9.24401 | -50.04509 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a282dde4-3cb5-3d5d-babd-bb7c0c5370eb | -15.92603 | -43.5136 | 2025-07-02 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f7602f17-d3f4-3b1c-8cf7-a68c2697b5c3 | -10.79786 | -49.236 | 2025-07-02 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5b0d808-225c-3f80-81d2-32f393320724 | -12.43243 | -50.02991 | 2025-07-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 472f14e6-978e-3c16-93d7-23c70af25f1b | -11.32572 | -48.68174 | 2025-07-02 04:27:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02d9dd5f-00a1-3e38-9fef-d3d190fdb40e | -7.03531 | -55.50243 | 2025-07-02 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbaa49fb-9c42-370e-98d6-efb1cf399316 | -10.64533 | -44.48812 | 2025-07-02 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7369acfb-01d2-3a85-957d-b228ede6557d | -10.64828 | -44.49275 | 2025-07-02 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50be38ea-0b37-38aa-98a0-e24866140535 | -11.32629 | -48.67815 | 2025-07-02 04:27:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c843c804-f7db-30a5-915c-fb489b2c3943 | -9.25197 | -58.76328 | 2025-07-02 04:27:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80002400-c592-3579-a597-540f791ca845 | -8.89909 | -48.33472 | 2025-07-02 04:27:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21fae605-f759-342e-bbec-c1ef2d35e8e9 | -13.88224 | -45.94465 | 2025-07-02 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da5f7cc9-91e7-3579-b506-0d2f95b55e7f | -10.99419 | -49.39116 | 2025-07-02 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6b3432b-4518-3224-9c75-34b8adabfa1f | -11.84502 | -43.80294 | 2025-07-02 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40ee81e2-dc39-35b6-b27d-dd19ae870139 | -11.33542 | -51.44481 | 2025-07-02 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30808af4-fdaa-3fc8-8372-d244b6e49f72 | -11.24136 | -49.49326 | 2025-07-02 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2dac993-cb6d-380d-9005-f65dce5d9bfd | -8.35128 | -48.46151 | 2025-07-02 04:27:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 786adbbf-ac28-3b4a-b8d6-dddf6ed4f38c | -12.42963 | -50.02546 | 2025-07-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bbc6869-8721-30c8-8bb3-108ae30d34ff | -10.92613 | -57.1285 | 2025-07-02 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2b5d126-8b88-34fa-9398-8359b9d70c4c | -14.62276 | -49.99047 | 2025-07-02 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9381960d-ab5b-3783-9748-88820c28c9ef | -14.48782 | -46.98298 | 2025-07-02 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 614e5429-37bf-3b82-9b8a-29590bfb290a | -15.21921 | -47.15412 | 2025-07-02 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6be5cad4-0552-3eb6-9630-ec2e78f5e7aa | -10.3038 | -57.13789 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 678e1724-0b91-33f0-a340-dc0e8eede310 | -10.30453 | -57.13429 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16e9ee43-e057-3c48-ad31-6714b3bc10c0 | -10.88521 | -56.44911 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fc0a0142-3839-3ef2-b052-8bd0dc1a3eb6 | -10.29832 | -57.13675 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ec087d3-3c26-3c89-8251-6fa558bb9835 | -9.95881 | -54.17519 | 2025-07-02 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a32a88fb-4cbb-380c-a62c-68cb39538c5f | -13.36122 | -46.20073 | 2025-07-02 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1475f01f-90eb-311b-b7cf-60be449caf6d | -8.43507 | -49.20012 | 2025-07-02 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9888138-76c3-3f0a-b20b-190eef56c94b | -10.89099 | -56.447 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1c395bfc-ded2-3e66-b11d-010e5d606ad2 | -9.95963 | -54.1707 | 2025-07-02 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba7ad4c1-ffd6-397c-82bd-272b346553cc | -9.23532 | -50.03102 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f7eeac7-734f-3c1a-aca0-af59246f9913 | -15.00492 | -48.33082 | 2025-07-02 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6288aa09-9b82-3566-b083-763d3dda8b3a | -13.41399 | -47.82335 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
