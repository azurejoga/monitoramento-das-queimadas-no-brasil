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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b480d22f-a7a6-39f3-aa1f-3f1f62b9d22b | -6.93326 | -43.62569 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab9c419a-8c66-3605-a726-544e0b99ac91 | -6.36369 | -43.32397 | 2025-08-19 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8686fcdd-fa80-3767-b97a-11aff9f9567a | -6.24421 | -44.83145 | 2025-08-19 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f624f60f-21a6-3ffc-b540-f7a71f9d606a | -6.94352 | -43.60078 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f57a7b87-86a0-344e-8f0c-d1ea48822579 | -7.58698 | -45.43 | 2025-08-19 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fab0e2cd-9a77-3e15-b31e-d57851159362 | -6.45157 | -44.5633 | 2025-08-19 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07ccc157-20e9-35fc-8bcf-1eed1d3b0dd2 | -11.57252 | -44.85148 | 2025-08-19 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea69da01-805b-36f0-ab28-a7a42fb11916 | -5.97696 | -44.11592 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cc18567-b275-3ee2-b516-134bd90e32ad | -6.74709 | -41.53777 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ad6d625e-a0eb-394f-b017-eeb81eda90e5 | -6.51732 | -43.44712 | 2025-08-19 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 28adda99-90b6-39ca-85a6-84e7c2f97d12 | -11.57733 | -44.85631 | 2025-08-19 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4db79c94-7e62-3fba-ac22-bcce746bea60 | -6.9608 | -43.60011 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7744e6b9-ee56-3843-9b52-e0fa1c31153b | -6.74689 | -41.54801 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5aa95c7b-deff-342e-a5d0-7ced09c1e17c | -6.05498 | -43.74917 | 2025-08-19 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b0518f0-9016-335b-ab08-34b3970cfe8e | -7.16428 | -43.51018 | 2025-08-19 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1462cf69-c04e-3d1f-a398-8f9a18a73480 | -9.85037 | -44.6819 | 2025-08-19 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 378fdf1b-7ab1-3698-8310-809cd12b9814 | -6.95041 | -43.59433 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6414363-e123-3792-8e5e-0ed10b309fd9 | -8.23522 | -47.86024 | 2025-08-19 03:36:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88a9a325-5176-347d-beac-27669c6d625e | -7.01768 | -44.27695 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff3a3d46-d125-38a9-8280-4a05b2502af7 | -5.9744 | -44.13499 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 950abd51-07c4-3469-bdcd-ed64551580f3 | -6.41904 | -42.49442 | 2025-08-19 03:36:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d7470285-0213-3610-bb07-5d1a63ed935b | -11.49275 | -42.95281 | 2025-08-19 03:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 81c4b856-1641-339a-8e9e-302d04f60e0a | -9.26817 | -44.53669 | 2025-08-19 03:36:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edb05a96-57d3-3c02-b744-82df7471811a | -6.9464 | -43.61646 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0511abc5-5c81-3101-911f-3effeff1a916 | -6.53034 | -43.44155 | 2025-08-19 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6d789a93-109b-3f8e-a507-8a488ed3da49 | -6.94707 | -43.61278 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb81e83a-3bac-3db1-abf6-523ff3ba7199 | -8.76836 | -46.69114 | 2025-08-19 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fac5f77a-13ee-318b-b365-c7ab50cfac5c | -7.30413 | -46.2906 | 2025-08-19 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce0ca953-2083-3cec-bfa7-da66186789fa | -9.85057 | -44.69426 | 2025-08-19 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ae24490-e5ef-3260-b6bd-75f84af6178f | -6.95727 | -43.58799 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cad1bdf0-3cdf-308c-b436-52fe571b8123 | -6.6757 | -43.67773 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1c3d3e3-e937-3c0c-b256-424c67f7585b | -6.95327 | -43.61012 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ada68890-923c-374e-87fb-5d19d592b09d | -7.13236 | -44.60107 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9612e51b-32a2-3672-a8cc-1597006afe76 | -6.94016 | -43.6193 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1fad6ae4-e9ae-3d21-ab85-cd037c41bcd8 | -6.93112 | -43.60603 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97346cd5-d622-3211-955d-1cd7fe1f776c | -6.93303 | -43.60144 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 182e10bf-d69c-350b-90d1-18ff3ece7e6e | -6.92814 | -43.59671 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0ac69460-2628-33c0-a552-06200a160329 | -6.96768 | -43.59364 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| d4bb6af0-7171-3b09-8a1f-31aea6563fea | -9.85534 | -44.6867 | 2025-08-19 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 745e149d-9380-3fd3-93f3-98a9a8254f4f | -7.14952 | -44.21098 | 2025-08-19 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 356b0803-c394-30ee-8d05-9254fd4684bf | -8.09319 | -44.83834 | 2025-08-19 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4efa8c9e-0369-368f-96ac-e3c7b192b58b | -6.94554 | -43.58964 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 203f5b31-7809-317e-95a4-083711febcdd | -6.93882 | -43.62669 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28a8e7a1-0c39-3545-abcb-c150acb3af4d | -8.70366 | -47.87079 | 2025-08-19 03:36:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcee01da-31bc-3963-8f5c-6efeb696358a | -11.44775 | -47.32545 | 2025-08-19 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aadb81f6-4121-38f7-b8d1-810fc6b9fe21 | -7.30299 | -46.29659 | 2025-08-19 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46b1e4ce-7b00-3de9-a190-fc6bfd94d711 | -6.93247 | -43.59861 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bce02de5-6f37-35ec-89ea-541432bbee8f | -7.28624 | -43.68398 | 2025-08-19 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bc8da66-7e8c-3e34-ace6-608428f1a1a4 | -6.15105 | -42.69933 | 2025-08-19 03:36:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37c9d3f5-aa77-39c0-b791-185ec6d11117 | -6.15729 | -47.27999 | 2025-08-19 03:36:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d1822a2e-94a4-368c-8bf7-b9066cfc5970 | -6.93595 | -43.61096 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94de58df-ef8e-3ef7-8c8f-8962ff337f28 | -6.3582 | -43.32294 | 2025-08-19 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 796d0b07-4b7f-3d31-a673-3745a824434b | -6.92693 | -43.5976 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9694d69f-68b3-31f3-86f4-8c39b0308690 | -6.16178 | -47.28275 | 2025-08-19 03:36:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33c66e68-7081-3013-b359-5c9757ad690e | -7.14861 | -44.211 | 2025-08-19 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1e2b30e-7123-35ef-ac0e-a0b5efa9b23a | -8.23386 | -47.86722 | 2025-08-19 03:36:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2019e32a-5828-3886-876c-014693578399 | -5.97625 | -44.11983 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca1e696b-5f7c-3263-b83e-928512cfc27f | -7.58609 | -45.43474 | 2025-08-19 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b044059f-1f0a-3c09-b6b5-ded4b30a1465 | -6.6787 | -43.68144 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b58a7d5-2fac-3919-90fc-97e27b823f44 | -6.14465 | -42.7047 | 2025-08-19 03:36:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5a27775-9fbc-3651-b3c0-c9ac09463007 | -12.03767 | -44.0158 | 2025-08-19 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c219d626-06e9-3855-ab16-f0d6011c6d10 | -6.45077 | -44.56768 | 2025-08-19 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c49956f4-134e-3475-9569-244a662dfc33 | -6.94505 | -43.6239 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c880656-3ef3-3047-9bc6-3c9f38203759 | -6.75296 | -41.56099 | 2025-08-19 03:36:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| beee4ccb-9225-3803-ac32-1ca9c503c53c | -6.95947 | -43.6075 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f279ac52-ae09-3c8d-8541-677e84c35b17 | -6.96701 | -43.59736 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8bb26667-59c6-3563-b641-d868a94d0c99 | -6.45237 | -44.55889 | 2025-08-19 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50ce955e-b0d3-3921-a6a6-28880d491d29 | -9.49327 | -40.37213 | 2025-08-19 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4252b5f8-58aa-368b-825a-9bcee5245a40 | -11.44666 | -47.33081 | 2025-08-19 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 589d9d8b-f11c-3af6-a6f1-a43144a3e945 | -6.5185 | -43.44419 | 2025-08-19 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a36b0e45-01eb-3e48-b57b-489f2f61c598 | -6.61596 | -43.8838 | 2025-08-19 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8163ce84-3bae-3187-9258-055153428468 | -6.87597 | -45.2108 | 2025-08-19 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10108d44-12a0-3c0a-99bc-7c6e5f104deb | -6.61526 | -43.88773 | 2025-08-19 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8191ccb0-2e04-3f0b-8a2b-f193326f1a0a | -9.85384 | -44.69479 | 2025-08-19 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94ce9fb5-6881-31be-bfb7-72ccec7e8938 | -10.83159 | -45.04298 | 2025-08-19 03:36:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28830e40-c158-333b-a1b7-403b69a09a79 | -7.2611 | -39.67412 | 2025-08-19 03:36:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a74877b-3c82-33a3-b25b-2fa91c01a9ab | -6.36182 | -43.271 | 2025-08-19 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9daef576-3da6-3c1f-968e-866db202f6e1 | -5.92019 | -46.00277 | 2025-08-19 03:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f716efa-f3c1-39b3-ad1e-47c4122c60db | -6.93368 | -43.59773 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 43c4b0ef-0e41-366e-bcdd-e59b7e7f53f9 | -6.94488 | -43.5933 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02f00a66-8af6-36b6-a588-ca342acfcc03 | -6.96281 | -43.58897 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b30ef8e3-d834-3b30-bb9d-4eab85896ec1 | -6.6794 | -43.6776 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8154dea-ffbe-3175-bd40-77e64afb39ad | -7.593 | -44.40076 | 2025-08-19 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7697901-ee5a-3aa8-a423-8ebe3ddd021c | -8.71196 | -47.86527 | 2025-08-19 03:36:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ed91dda-656d-33bc-a5d3-97fb32c9ad5b | -6.92558 | -43.605 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99f45ecd-35d6-37fa-ab40-fdddba605686 | -11.98287 | -40.86289 | 2025-08-19 03:36:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4919f5e8-1d6d-3ef9-a7a8-727a4113825d | -6.36117 | -43.27467 | 2025-08-19 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 535ab6a9-4073-33c5-8dcb-58a6215e6fd9 | -6.96633 | -43.60114 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 34ee08af-d29d-352e-adc9-69b470b9466e | -7.29534 | -43.69699 | 2025-08-19 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f782d460-4bf8-3d1b-bb46-c401f9620b6b | -6.93041 | -43.6165 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ad5e4a4-9624-3942-9754-a1b6aa3bd4ca | -9.85459 | -44.69073 | 2025-08-19 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bc3aa97-ef00-381d-a63a-b5780c146740 | -6.8706 | -45.20548 | 2025-08-19 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d18c184-b6c6-35b1-96d0-c1ab78973e14 | -6.95392 | -43.60653 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0cefa0a6-b07a-3e6f-a3a7-63d5eda2e2c2 | -5.97581 | -44.28983 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf74dfe4-c1ac-34ba-b3fc-e8eb2374e74e | -6.94 | -43.58866 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4b261d32-cc96-3e88-aafb-6840a21993ed | -6.94083 | -43.6156 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f46f2391-04be-39b2-b295-f82c10bbd2fe | -6.58213 | -43.08961 | 2025-08-19 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 303307c6-eb07-3552-8f8e-b1764de06ba8 | -6.95458 | -43.60287 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d3312531-8495-38f2-bb29-d1306211bcbc | -7.13815 | -44.60271 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65b9a87c-2f2b-39ac-9f52-3398251ee471 | -6.94573 | -43.62014 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README15.md)
