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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e02f7b8c-e323-3294-9218-6d82fefdb5d3 | -6.2635 | -45.33508 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afe76834-eacc-3fb1-a96c-6d436bdede9c | -11.02507 | -45.89067 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dddf8786-10ac-3e66-8bf0-1cb269fa5de3 | -8.52634 | -44.947 | 2025-09-23 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd64a731-6e5a-3a01-bfe7-85623a2ddcc8 | -11.41992 | -44.95427 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 280e1d9d-bee8-3d5d-bb67-4b00292c7986 | -3.64022 | -51.90827 | 2025-09-23 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6e346a4-2104-30fa-b44d-ceb142078adb | -11.40831 | -44.94775 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be213ee8-03f9-37e0-a9d1-256c5bdf7c81 | -6.67659 | -38.4987 | 2025-09-23 03:57:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 528d42cd-9911-355e-b8e3-06ce616bfd69 | -3.51526 | -49.44641 | 2025-09-23 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63a709dc-d465-364d-ab48-f8dd1ebee44e | -4.39676 | -44.3718 | 2025-09-23 03:57:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0236f1a1-faad-3416-8d8a-3328ef808184 | -9.99865 | -46.28627 | 2025-09-23 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea375618-9045-37c6-80e9-42f7b204450b | -8.01341 | -45.46422 | 2025-09-23 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0de5aa31-06a1-32ed-a0bd-43df3f2baad2 | -11.50029 | -43.55906 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 991a09be-4623-3ea6-8fa6-ef54aaf127e1 | -7.4637 | -42.62811 | 2025-09-23 03:57:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 61b4b03e-2357-30f6-9c5c-b9131db3b837 | -9.18856 | -44.62155 | 2025-09-23 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33fd8465-21e6-39c8-b2bc-d97195485450 | -7.07005 | -46.19971 | 2025-09-23 03:57:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b0405cf-5742-3258-a4f3-3657b9800640 | -10.95323 | -45.74212 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c70497c-2111-3107-85a2-8e61c68ea76b | -11.41862 | -44.93776 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 741150b7-989a-3ab9-a8dd-175d5cfa99ba | -6.19325 | -44.35434 | 2025-09-23 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c25cfe0c-1374-361d-b753-29ff618911ba | -7.35994 | -44.53994 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9deba0f-8ca1-39fc-b863-d8c0c5e8bb22 | -7.28932 | -44.15154 | 2025-09-23 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ac5d07d-f963-3ba3-b652-89b12128c9fd | -8.94742 | -44.48981 | 2025-09-23 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c5ebfe3-8f4d-3f7d-93c9-12d6834d0032 | -11.60632 | -45.0272 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce4548b3-369e-3bad-9a4e-eb969df2f791 | -11.92957 | -38.33224 | 2025-09-23 03:57:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 75a15514-ac5f-3b39-87de-dcfdcd2ba3b6 | -8.80879 | -43.07716 | 2025-09-23 03:57:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81d46133-3997-3cae-9b15-58bef4c2c684 | -3.51688 | -49.44746 | 2025-09-23 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 447fd360-13f8-31a3-93a9-97b370870c46 | -7.6039 | -44.44114 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d9d01b-51da-3088-a42b-68313ef0327c | -6.89274 | -44.76404 | 2025-09-23 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d43fb43-800b-325b-8e19-6749834058ea | -3.63897 | -51.91182 | 2025-09-23 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4327fbcf-0e3b-30f6-bdc9-78fb4292259d | -10.3407 | -46.05865 | 2025-09-23 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 890cf4d7-894d-381b-b6bb-45882f56702f | -6.09759 | -43.15627 | 2025-09-23 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9db22677-0f64-3121-afa7-a41bd971c81a | -4.49168 | -48.11931 | 2025-09-23 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44d991ea-2572-36d8-bdfe-35d35609b171 | -7.08215 | -46.35673 | 2025-09-23 03:57:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 697b3405-6161-3c0c-ae23-78c56ec60da0 | -11.21029 | -46.16133 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3c67a6e4-350a-35d2-ad32-2b97e3279464 | -7.60257 | -44.43951 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbe6314c-76a5-3d71-8047-71326eea13f5 | -11.47775 | -43.53123 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebf1bcce-8736-3863-a1fd-5ba99061fe0c | -3.63048 | -51.91746 | 2025-09-23 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a962d680-7ce3-3869-b5a9-1a7aeaff9e53 | -7.88426 | -44.02942 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ba23587e-875e-3401-9c31-4026713335ca | -4.96792 | -48.01865 | 2025-09-23 03:57:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ce5e2a9c-55c8-3f8a-96ee-5e6bd3b4c01c | -9.48156 | -40.35567 | 2025-09-23 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 06f54339-940b-3abd-a41f-e887625527c1 | -11.43699 | -43.51898 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84fdf18c-4e6d-3be7-84ed-af81dc39bb6a | -3.68967 | -49.556 | 2025-09-23 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 905df8b0-0837-3d7f-a1fc-5d0187216763 | -9.0099 | -48.02157 | 2025-09-23 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b0f6ed7-a617-32a2-9329-ac173a5bf08c | -7.88199 | -44.01766 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1daf99c0-e502-374d-9eeb-a904f2e0f609 | -7.36238 | -44.54227 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 533f846c-7868-309e-86e1-ec5bc7ee365e | -11.45049 | -43.53104 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9bee5d1-3866-3535-961c-8335a99d384d | -10.3401 | -46.06009 | 2025-09-23 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66fce35a-8efe-37b2-9944-aab977a042a2 | -6.25256 | -45.33543 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2b20a4d-d840-34bf-b128-cd33f4e5107c | -7.88014 | -44.02869 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02fc114e-8611-3d77-b869-ba9407dec277 | -5.12177 | -40.74584 | 2025-09-23 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8685b0d-5cd5-373b-a588-32fae51b1632 | -9.30245 | -35.69546 | 2025-09-23 03:57:00 | NPP-375D | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d8bc896d-8698-3d51-862c-2dea12e666c7 | -6.96069 | -45.20495 | 2025-09-23 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4cdcc71b-b7f1-36cc-b79e-dd0761ff0305 | -11.41037 | -44.93629 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84fa3004-d054-30f2-88b0-14fe487675b0 | -6.59233 | -44.54805 | 2025-09-23 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bbdca909-f7f9-3e08-a5c9-2eba89afd10a | -11.82074 | -43.16152 | 2025-09-23 03:57:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2a77123b-0637-3c06-a234-434e410924c8 | -7.70095 | -44.90717 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 32f5d853-ae1c-3616-808d-f5e800b2cb12 | -4.77975 | -47.25308 | 2025-09-23 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3373717-9bd3-3213-b5ea-536c5179c770 | -6.26185 | -45.33671 | 2025-09-23 03:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c228f9d6-dac1-30d6-a0c9-861f222cc7fe | -7.03954 | -41.99728 | 2025-09-23 03:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1755e749-93a3-3842-8317-1afbe14ae46c | -7.46586 | -42.6305 | 2025-09-23 03:57:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fb6b018f-9371-3ce1-a1af-b387aa8c52fc | -6.96521 | -45.20575 | 2025-09-23 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8028b9e3-c159-333f-ad38-9693b3b5cc8c | -5.75381 | -42.60631 | 2025-09-23 03:57:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09da15d3-f1a6-34f1-98de-4522e5f71afc | -11.53465 | -43.62587 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9ecbd80-2ae2-362a-b250-545fda94c61c | -7.04138 | -41.99482 | 2025-09-23 03:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a0183b7f-381a-3c1f-93f0-d4a5f0994bef | -11.89365 | -41.26731 | 2025-09-23 03:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4a52fd31-c4e6-343d-aff6-244f947ae458 | -11.53248 | -43.61586 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72a0a2b7-51e2-32d6-9452-8312dcf8acbc | -7.76947 | -44.72037 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 048377a6-480f-3ebd-8d8a-1a70a4c550f4 | -10.00318 | -46.28764 | 2025-09-23 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98c296e4-562c-342d-8212-41468e58986a | -7.03531 | -34.91441 | 2025-09-23 03:57:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 670cb22e-5232-3e54-8f63-45f8263f10c7 | -8.76233 | -38.9773 | 2025-09-23 03:57:00 | NPP-375D | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 049ddd6b-1777-3e9d-b8c3-5f699945e39b | -7.7964 | -46.19738 | 2025-09-23 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17d04fca-cf4f-386b-ae79-d73813ab23f5 | -7.2399 | -39.25751 | 2025-09-23 03:57:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7dd6e65-fbfd-3604-b1b4-46e2330de606 | -5.45279 | -44.00253 | 2025-09-23 03:57:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3646c13-131b-3699-bae1-ee99510d747c | -8.0159 | -45.44999 | 2025-09-23 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b28f8eb8-6c75-367c-8d08-f32452f2f420 | -9.31639 | -39.17694 | 2025-09-23 03:57:00 | NPP-375D | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 03367e5f-61a5-3a54-9b59-a51aa95b4809 | -8.13505 | -44.46441 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ace3a2f7-7a36-3185-ae76-ddbaf9964775 | -7.88321 | -44.02184 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 53fbc1b9-cfd5-386b-94f1-58f21301874d | -10.09135 | -39.55709 | 2025-09-23 03:57:00 | NPP-375D | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7e21c96-0a23-302d-ae5e-9cebc6d8bdd9 | -4.96299 | -43.23228 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1a3fc5a-3274-3dd7-a441-dcc9b606a7a7 | -6.35814 | -43.36005 | 2025-09-23 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4fac97f-82aa-3339-9b7a-59885e373f56 | -11.60885 | -41.61948 | 2025-09-23 03:57:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 42e4f9fe-357b-3e7d-89c1-f145aa005ca8 | -7.8908 | -44.02695 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51a8ae3d-89f9-31f7-b835-d7d9d445f98e | -11.21397 | -46.16658 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1014a06-b7a3-33ca-b9c7-a96245f35298 | -9.73075 | -45.94768 | 2025-09-23 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ced30daa-a4bb-3aef-9dfe-4679062807b1 | -10.33986 | -46.06322 | 2025-09-23 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 899d81db-9cf1-3a92-a4b7-d3820389f69b | -11.48154 | -43.53189 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83d1cdf9-fcc0-3e75-b3a1-1776580c97f1 | -3.63176 | -51.91005 | 2025-09-23 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3173df2a-8e2b-3850-8876-7f33697dec11 | -11.02471 | -45.9022 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f1505b6-bf74-3e75-ab63-0eed75c13980 | -3.52074 | -49.45261 | 2025-09-23 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c46d64d9-2621-391c-af67-8e7ec244f6cf | -6.90611 | -45.57327 | 2025-09-23 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f57ab263-2dc7-35b0-b9a9-28670165f8ab | -10.98489 | -40.29774 | 2025-09-23 03:57:00 | NPP-375D | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d9e57cf0-ef1d-3546-941f-d2d5c22da5d9 | -11.02427 | -45.89505 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7448dc56-118d-3310-a69d-a715502cb884 | -11.6091 | -45.0285 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ea224cd-9864-3f4c-b45c-c701a6c4b04e | -10.54901 | -39.82241 | 2025-09-23 03:57:00 | NPP-375D | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c2e7aa3d-9cf2-3634-9fda-6aada66c9b50 | -11.44455 | -43.52036 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 444d728c-0481-32e0-be9b-810cf57fae45 | -7.34027 | -39.70433 | 2025-09-23 03:57:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 72eff4c1-f522-3e7b-868c-7cd6b59e5c21 | -7.89144 | -44.02328 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c15c26a-de98-331a-a5a1-bf76695b6a7f | -4.48039 | -47.67645 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e949fe2c-32c9-3b13-bdd4-c3ec3306c2f3 | -4.96709 | -43.23292 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a7c4c4a7-39d0-3f2c-8f04-43791267720c | -6.89641 | -44.76894 | 2025-09-23 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f8e34022-deba-32aa-81c0-062cba690a07 | -7.3397 | -39.70789 | 2025-09-23 03:57:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README9.md)
