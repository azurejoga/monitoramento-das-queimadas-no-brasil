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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31983082-02d6-3c72-8645-51bed5f17f54 | -6.14351 | -41.75871 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ffea4eca-0320-3b28-810c-9d1d34c5295e | -7.9428 | -44.14379 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7c56d24-75c9-3d17-ac5e-a63ae746bae0 | -6.45338 | -44.57843 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c92f9d4-2114-3da6-a8fd-3f80eab11b1a | -4.87036 | -45.7775 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e6e9df5-7c07-3d77-adc2-9e1c15799d6f | -7.57212 | -42.68573 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 19ef80e2-a448-3e8d-a1b1-97fbd73e4216 | -6.99812 | -41.99802 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1caf3f64-9043-3d3f-bcfd-0b0129bd1285 | -4.25716 | -45.5834 | 2025-10-15 03:47:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99b6ed43-db3a-39aa-a359-23c8ba1e0a1a | -5.34171 | -43.7443 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18b7117e-8bb5-3b3a-a6c5-87783bbbf6c1 | -8.46218 | -44.19015 | 2025-10-15 03:47:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12145533-2a57-31f7-83f9-5d3b3867d7dd | -5.91067 | -42.83032 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5257d5b3-e869-352c-855b-f8f0820e8b89 | -5.58287 | -44.74849 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c71e0359-5a13-3457-a2db-6fb323255f3c | -4.89071 | -43.46451 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2564b7fc-d56a-384a-a823-1d3785848902 | -8.22114 | -44.07127 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52383fad-6fe8-3da6-ad4b-3261562b2926 | -5.39116 | -44.04243 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b164af14-6bb8-3157-bd06-76e9a93f8f44 | -4.85897 | -43.20478 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78ad45bc-49e5-3468-ae25-45636f50de4b | -5.39111 | -41.16138 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d33ed68d-93da-3491-b114-c752092d70d5 | -5.86869 | -43.8661 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ab5d9d4-29b7-3f5c-b81f-aabdcc6b4313 | -8.20711 | -44.00475 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d4190c1-3722-3693-b83f-693fdb2fe05b | -5.24633 | -44.47377 | 2025-10-15 03:47:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e3e9dae-fe39-369a-b5b2-72198e83745b | -5.03194 | -44.73593 | 2025-10-15 03:47:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 533bcdb9-21d1-36b1-aa2e-1dd14f69f11e | -10.04194 | -48.71093 | 2025-10-15 03:47:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e732ddb9-27f7-39fe-ba58-0a9360b4a598 | -5.58975 | -42.84811 | 2025-10-15 03:47:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 000969b3-9f5d-3a92-8d0c-9d837b720120 | -5.05826 | -40.47008 | 2025-10-15 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 58b16237-833a-3116-9151-6ffb0c5746e9 | -5.87169 | -42.79573 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 69db2753-5e6d-3946-a41c-10415c238dc8 | -4.75716 | -44.10916 | 2025-10-15 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc5c365a-d9f2-305a-8a7b-5d1903e03aa1 | -7.75571 | -42.44493 | 2025-10-15 03:47:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7966f6f9-87fb-3c1f-84f5-3b0798df7ade | -4.77 | -45.74212 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3ae5215a-fd5d-3b3c-8d57-20f1c61d40ff | -4.35758 | -48.20032 | 2025-10-15 03:47:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 059d2599-3088-3200-a961-a76ca9562081 | -5.47294 | -44.66371 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32d2dd76-5455-392a-b123-67c0c26302a8 | -4.76567 | -45.74065 | 2025-10-15 03:47:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4583814-ebbe-303e-9942-f8a8c04ab25b | -5.00018 | -44.49716 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1541e671-4af4-3f61-9005-00f4965ea4dc | -7.55515 | -42.71587 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92f7a667-1254-31ea-8365-b5efde39b599 | -8.21637 | -44.03988 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47c86613-5230-3acb-9cb9-1673dda3bb35 | -8.24387 | -43.34472 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c92bc47c-49fb-37a8-a52f-725e639d989b | -5.27568 | -41.04866 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6af8767-7d4c-3a6a-8edd-b6c89a292e94 | -5.4235 | -40.66431 | 2025-10-15 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bcc6106a-2ae3-3eb7-9b24-077e1d17327e | -7.74407 | -42.45742 | 2025-10-15 03:47:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 880b970c-991c-39b7-827f-90c581be7f42 | -4.64648 | -43.12878 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 031ee6a6-a52c-30f1-b3b3-e1ee3cf3b60a | -8.19574 | -43.98146 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1032c0df-479f-3d2a-a3eb-e154ba502ddd | -6.0293 | -43.39738 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 744c52ef-f96a-34c8-801a-054dfd5fb21c | -6.37872 | -41.48895 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4bf4c4c0-e579-3717-900e-aa0dda5a2122 | -8.27216 | -43.41017 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fec5bd96-f676-3f1a-991b-380cd2983343 | -5.39649 | -44.04325 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 109f3fc3-8c28-38ad-9c85-18a4eeb8104a | -8.24484 | -43.33929 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 50c74fbf-9c1d-3874-a0e2-c5f34be949bc | -7.28812 | -41.95491 | 2025-10-15 03:47:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e98381b-6505-3d80-9662-166e6e5b6ea0 | -4.85796 | -43.21077 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0bc0267-7211-3f97-a197-3929aa20014e | -8.17571 | -43.95553 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a75b8c3e-bf58-3e0a-af2e-20b2eb5f78f4 | -4.83385 | -42.77876 | 2025-10-15 03:47:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a3cd5c43-7b48-3642-99d5-9136fd976245 | -8.461 | -44.19679 | 2025-10-15 03:47:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 766f6b28-0ec5-3381-9df0-1de6f8622350 | -6.42759 | -41.82985 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54f49004-cacd-34bf-a3fb-d29978141e4b | -7.27897 | -42.95505 | 2025-10-15 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fae2ed02-d224-3c27-b491-65301a7651bb | -5.39248 | -44.04552 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e21f756-9549-3c7c-b5c4-c0ac7319a91b | -6.88874 | -43.96216 | 2025-10-15 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bdde90d-9f44-3463-950a-ca5d3dd5fbcc | -7.57082 | -42.70876 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2889d8d8-6cfd-382c-8c04-a80824ce8591 | -5.87333 | -43.8702 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3aa15f1-805e-398f-87f7-22b708671904 | -7.94951 | -44.13571 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4acbe39-e0c1-38fe-8a8b-f88104a9437a | -8.19727 | -43.98065 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 906e68c1-6b0e-3e79-8160-b38f442e1309 | -7.53775 | -35.20026 | 2025-10-15 03:47:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 79173899-37ce-39f7-bf01-4ecb9b531c5d | -4.90101 | -43.46626 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 454cafcc-c263-3d4a-9050-67a396fb4af4 | -7.16447 | -42.50763 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d2ec2786-c5b2-386f-866c-37bdcda69cb7 | -7.50398 | -42.1414 | 2025-10-15 03:47:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ad489b24-fc5b-3889-a70c-f371ab86a7cf | -5.33002 | -42.56262 | 2025-10-15 03:47:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a3df3a1a-092f-39cf-a11f-cdf03c8481b1 | -5.58909 | -44.74556 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8bbfa86-1334-3eed-a2bd-30c264e4ffa2 | -5.43618 | -44.22519 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 783d7f0a-0118-3744-ab98-8a24943f07c3 | -4.65004 | -43.13843 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 99ee1cd9-9323-348b-b894-c644e8019f15 | -7.56485 | -43.89355 | 2025-10-15 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3931196c-2bbb-37ea-9ec2-019cb5d37515 | -8.19629 | -43.97851 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d2ddadf-ed98-3126-8d73-20d9df04862a | -5.42783 | -41.34186 | 2025-10-15 03:47:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 28db907f-4991-383f-8629-7b9a36808190 | -4.77668 | -45.73915 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ab99cf0-34a6-39cd-a6bd-8c5a4a865c71 | -6.26352 | -44.34299 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0842c56c-8563-3942-9312-22841c61bffa | -4.55071 | -45.42234 | 2025-10-15 03:47:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9877a999-7559-3470-ad00-eb06f62d5d1c | -7.18362 | -41.38998 | 2025-10-15 03:47:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7e8b96b1-d45a-31b8-bd61-3955105cfda7 | -4.87675 | -42.76411 | 2025-10-15 03:47:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b902519c-295d-358a-bf4b-948097b43aed | -4.35059 | -48.19907 | 2025-10-15 03:47:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6d480b1-bec3-3c81-9852-f11e6160720b | -5.9791 | -42.88287 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b9344131-7cc6-34bc-b031-874aab5b9bb0 | -7.5372 | -35.20374 | 2025-10-15 03:47:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27b2a633-6639-3ef8-b0aa-421ced0d8dcf | -10.41326 | -42.56505 | 2025-10-15 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 631a47d6-e365-3af2-b939-a84c87ea6c6d | -6.2285 | -44.17033 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 704589fb-4941-3a06-8832-dc57c2d53c7e | -6.14502 | -41.77684 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8e7bfe94-829e-37e4-9dc1-c409eb526f5d | -5.01088 | -44.49575 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69bf7e11-a242-3aa5-acbc-d22aef6f34ab | -10.51693 | -43.36651 | 2025-10-15 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62740c53-8715-3e01-b7df-a959d04ae9a4 | -8.45715 | -44.18892 | 2025-10-15 03:47:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41ac2bd5-b9b7-3dbf-ab91-67de51d590bb | -5.07153 | -41.1921 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c0317a4-27fc-3d74-9875-184f63de1b9b | -6.02361 | -43.40033 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b38a952b-62ed-3e0f-9fd4-83fcfd6fed2f | -8.28599 | -43.44537 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c5c4199-bf93-36f3-9938-d14769d886e6 | -10.82154 | -47.98836 | 2025-10-15 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b42716e-2f3c-39cf-b112-f6551bd1a2a9 | -11.2315 | -39.23899 | 2025-10-15 03:47:00 | NPP-375D | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 176a635f-522b-3b11-a276-50a5a7862a78 | -7.25256 | -44.91536 | 2025-10-15 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c07ee7a-ef79-3ac2-a1fb-2ed300d81c99 | -7.93822 | -44.13983 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4d52f5b-91ca-3c56-8920-aed1270602a2 | -8.27699 | -43.41109 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| efe8622d-508f-36e2-b900-43a9394aee20 | -5.42834 | -40.66117 | 2025-10-15 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5c6b5832-bec9-39be-abd8-b5758e378501 | -6.16874 | -44.30073 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30f87dbb-9641-3346-ace0-7230f1cd7f73 | -4.63622 | -42.52559 | 2025-10-15 03:47:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f8e5d09c-f658-3189-84fe-655ab579272c | -6.43011 | -41.83142 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ab1a5a8-b80a-3c52-b8a6-c3b09ea7e5c9 | -8.21952 | -44.08022 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56a82ac4-67e8-3596-9e3f-d8105184458c | -5.54449 | -41.32188 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1fe259d0-50c6-3519-b09d-fc58d26297f5 | -9.26909 | -35.63556 | 2025-10-15 03:47:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0cfe788d-3c1c-3286-a990-381247969333 | -6.3358 | -44.02272 | 2025-10-15 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b71c79d-f60a-38aa-b158-98652dbe1b0c | -7.66917 | -42.3786 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 34c5fcbf-1e1c-3a7c-8d4c-d03ea4efe68e | -5.86978 | -43.85991 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README18.md)
