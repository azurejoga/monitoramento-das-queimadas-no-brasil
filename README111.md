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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06c1bb70-d4e3-347d-beb1-753dd16bd71f | -11.1245 | -52.0359 | 2025-09-10 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 5302cfc0-5d5e-32b9-851f-99a76a67ef7b | -10.3885 | -50.5264 | 2025-09-10 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| fd741e00-2ce0-356b-8432-81c1f5d511a1 | -6.2085 | -41.0381 | 2025-09-10 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 7091d486-34d9-3430-b2ee-28fd3bdd90ad | -6.2009 | -45.6162 | 2025-09-10 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| a654b2f3-c806-37ac-9076-301313979e56 | -9.0579 | -46.9688 | 2025-09-10 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 952670ac-2a66-3a0b-a96e-fe80b8a9e00a | -10.1654 | -46.195 | 2025-09-10 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| a6e2d29a-ea7d-3ae3-93cf-21d532d21f95 | -9.0229 | -49.8048 | 2025-09-10 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8d1f0bbc-3f51-321d-b4b4-cdc16fe8115f | -5.9193 | -45.7492 | 2025-09-10 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 336c02df-097a-3a27-a7b1-4125d2e13184 | -11.4702 | -50.3461 | 2025-09-10 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 183.0 |
| aee6d8b0-ab83-3e24-846f-24d6cd92db0f | -11.3905 | -43.5365 | 2025-09-10 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.9 |
| 2d0c0a9a-07ec-37e2-a319-8403a8125d77 | -13.1367 | -54.9171 | 2025-09-10 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| c77e994b-7ce9-31be-9d43-1a87dc1000b7 | -8.0416 | -48.6656 | 2025-09-10 13:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 153.4 |
| b24d5237-d213-3fc7-b3ea-76b99169f76d | -11.4465 | -43.6224 | 2025-09-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 348.2 |
| e02c5253-d07e-3be3-b893-f5517e97cdba | -9.6818 | -46.9015 | 2025-09-10 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 55566d77-a19a-3760-814d-db30b05d2d8d | -15.2881 | -53.7777 | 2025-09-10 13:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a759d469-fd04-3ce1-ab62-8d47a9b0c876 | -11.4702 | -50.3461 | 2025-09-10 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| f465bb4e-5044-3f4d-8770-208b3a66bdad | -9.0417 | -49.8031 | 2025-09-10 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| c30998e7-c19b-3ae5-9a66-06eb0a72f889 | -13.1364 | -54.9376 | 2025-09-10 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| af1bacc3-d479-3745-9237-66756c43bc66 | -9.0579 | -46.9688 | 2025-09-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 20997ba5-1c98-311e-a1b5-1201efadcdca | -13.1176 | -54.9191 | 2025-09-10 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 1ad87b3c-4e2e-3a15-98e2-89386ca1cdce | -5.5702 | -42.9062 | 2025-09-10 13:50:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| d5d5c97b-8a70-348b-8668-2535f489aace | -6.2597 | -43.3895 | 2025-09-10 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| fe19fa00-f9b1-36ab-aec6-9101ef02c585 | -11.446 | -43.6461 | 2025-09-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| caf748f7-aa42-3ad2-8e6c-30c28877194b | -15.2877 | -53.7987 | 2025-09-10 13:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 2509b569-ab3f-3784-afbb-02d51682994c | -11.1247 | -52.0149 | 2025-09-10 13:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 259.4 |
| b02061df-9600-369b-b41b-71e1476aa9b2 | -11.7706 | -50.5901 | 2025-09-10 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| ef5bfc12-bf38-3ed7-b536-2d72bf6b0bd4 | -6.8895 | -47.9115 | 2025-09-10 13:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| edff11b5-72b3-36f2-859c-6700ee8be4c3 | -18.0218 | -47.1319 | 2025-09-10 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 8137dcbe-0417-348d-8b21-82a9af88142e | -11.3905 | -43.5365 | 2025-09-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 40d63e29-a571-352a-aae5-1afd512c5119 | -9.7591 | -51.1172 | 2025-09-10 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| a43c7b05-253d-3e34-baa3-1a1e4cac15bb | -14.4054 | -53.4063 | 2025-09-10 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| ff7b69d9-b9cc-30b4-a987-d97e3b5dcfb0 | -15.801 | -52.2472 | 2025-09-10 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 4a177c3a-6d7a-3fc5-834b-94c9e770a09a | -8.0794 | -48.6407 | 2025-09-10 13:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 206.2 |
| 2cb6cce4-a44b-3226-ad50-4cc3ba47c425 | -14.8877 | -55.8567 | 2025-09-10 13:50:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| a389054a-df4d-3e37-a8b6-9adc017c2c19 | -8.994 | -46.0808 | 2025-09-10 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 7d3768be-c948-385f-b53b-854b22d93e49 | -14.907 | -55.8546 | 2025-09-10 13:50:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8c5b96c9-b68c-34a1-8e69-ac52776b1889 | -10.7224 | -48.2863 | 2025-09-10 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 6c6e869d-e4a7-3d3f-9cb5-7a31d0965e2e | -9.6821 | -46.8791 | 2025-09-10 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| cfbe1098-9c09-3a9c-8744-9822cfa740dd | -9.055 | -45.7583 | 2025-09-10 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 59c36138-f70d-3c34-8024-09164c5efd6c | -9.7011 | -46.877 | 2025-09-10 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 9f8975be-042b-3b6f-a611-0f16eaef9ce0 | -10.954 | -46.7943 | 2025-09-10 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1c4c6a2a-9f16-326d-9801-05eee0e5557e | -11.771 | -50.5686 | 2025-09-10 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 26e441bc-b069-37ff-93c3-fa1a839194ba | -6.2409 | -43.3911 | 2025-09-10 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 3f2682b7-da54-3e5a-ade8-4e27c40910d2 | -11.3389 | -46.5419 | 2025-09-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 8cad0da6-36d4-3cef-ac7e-726f294bb5a8 | -8.7361 | -47.0904 | 2025-09-10 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 066dd0a9-d8d3-3bbe-adae-67ab32b75b36 | -14.7542 | -45.3156 | 2025-09-10 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| a44eee97-9c50-375f-9f70-23527ebf5c28 | -11.4469 | -43.5988 | 2025-09-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 6d4a5180-2037-3566-94a0-9fb2a32fef83 | -7.4639 | -44.9433 | 2025-09-10 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| dd227cad-e653-3c26-815f-2113ea92206a | -10.8898 | -47.2494 | 2025-09-10 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1be4e879-bac8-38f6-91c0-8b075a8459bc | -8.7549 | -47.0885 | 2025-09-10 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2a75e33f-42da-339e-99b6-43075cc2e204 | -11.3393 | -46.5193 | 2025-09-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 239.3 |
| 6af1ffb0-120f-3c0b-bf55-f363ab49e2b6 | -6.8521 | -47.9143 | 2025-09-10 13:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 597d511d-7936-358f-841f-50aaaeda5521 | -11.9535 | -51.081 | 2025-09-10 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| e2a195c2-1436-3aa8-a6e6-41c0f7cd1ae2 | -10.1467 | -46.1747 | 2025-09-10 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 89620b94-54ad-3479-a038-fc3fdaddde43 | -6.2407 | -43.4144 | 2025-09-10 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| c65ed317-b535-3a1b-879f-9305e0d1aa26 | -9.0232 | -49.7834 | 2025-09-10 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 13a26fde-ec89-3298-85da-9b765d6bb0ce | -14.7536 | -45.339 | 2025-09-10 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 441.9 |
| 8b9566ca-9874-3c90-ab04-c0f412f60f79 | -11.1245 | -52.0359 | 2025-09-10 13:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 214.2 |
| 178a16c4-1bb9-3ed9-80d8-1e95ea552adb | -9.0229 | -49.8048 | 2025-09-10 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b2101ae5-9a30-3f0f-8dab-db180cb9535b | -7.5218 | -48.2536 | 2025-09-10 13:50:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 207.0 |
| 5e827bf4-3b46-3a58-8eb2-f77702240cdd | -11.4097 | -43.5336 | 2025-09-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 685ea7a2-1028-3cb4-b919-e73508e8ce12 | -9.1142 | -46.9851 | 2025-09-10 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 67556279-8072-38e3-beee-b884660c7c3e | -16.0604 | -49.9741 | 2025-09-10 13:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a89b058b-436e-3062-9f51-ca9f24e477e5 | -19.282 | -47.9946 | 2025-09-10 13:50:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 012bec95-84ae-38dd-97d4-0e9f4ca8c670 | -10.0137 | -50.3297 | 2025-09-10 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 298.8 |
| 24f942d9-e283-3923-ba78-99c41bd0a89e | -7.5409 | -48.2085 | 2025-09-10 13:50:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 6889aae1-888c-3770-ae09-961b3548bcc8 | -9.3437 | -46.7603 | 2025-09-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 6381cc4a-4054-3615-a19d-910b243b4b51 | -11.4657 | -43.6195 | 2025-09-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 5cc15ee2-3dbf-33d0-a82d-6dc4a90b2037 | -9.042 | -49.7817 | 2025-09-10 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 887f4f8c-8bee-367a-94d4-44ba88682d0d | -15.1374 | -52.4039 | 2025-09-10 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 01ce14cb-bb51-3933-ba49-b2d5a3ab651c | -6.3804 | -44.4664 | 2025-09-10 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| cef986bd-249f-3b24-83f0-5a36ec337fcb | -11.4652 | -43.6432 | 2025-09-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 8d5fc995-b2b4-3bb8-9d21-24c0aedd1b87 | -6.1896 | -41.0398 | 2025-09-10 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| 9b96f7c1-ee68-38e7-b403-5c2e77ad9bea | -11.3901 | -43.5602 | 2025-09-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 40a7a8fc-3e72-3974-8993-a8329efd7d2e | -7.522 | -48.2318 | 2025-09-10 13:50:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| b87d830a-84d0-33bd-98da-d5a8c2911d74 | -5.6788 | -43.3425 | 2025-09-10 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 43af901b-430f-3a9d-8b01-8546f27ec3b4 | -11.507 | -50.4276 | 2025-09-10 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 640933d0-1842-3f3e-8024-18ec52f03730 | -6.3806 | -44.4434 | 2025-09-10 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| a04200d5-f70f-3c55-b47e-cca62f44acfd | -7.5033 | -48.2334 | 2025-09-10 13:50:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 1a0448fd-1e90-3c92-87e5-e05cfc4e933b | -5.9193 | -45.7492 | 2025-09-10 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 6de315f8-2578-3669-8a46-18b03154577f | -11.4093 | -43.5573 | 2025-09-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 77d9753b-5193-341e-bf47-b8c1566efb20 | -6.2595 | -43.4129 | 2025-09-10 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 195.3 |
| f20f4491-d71e-3e91-b5dc-3a9d782ef6ed | -6.5572 | -47.4992 | 2025-09-10 13:50:00 | GOES-19 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| efc93542-6250-3b2f-82e0-63dfe352942d | -15.8201 | -52.2659 | 2025-09-10 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 31d77ca5-06dd-3752-82ad-928308ab4773 | -9.0603 | -49.8228 | 2025-09-10 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 548.5 |
| b0b49430-a840-347a-96f5-8231c9ae58f2 | -6.8519 | -47.9361 | 2025-09-10 13:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 953c83f5-881a-3c9d-a2cd-1de3fa083088 | -9.7599 | -45.4048 | 2025-09-10 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 778aa322-86b6-3e3e-ac95-1b1be735ae8d | -6.8523 | -47.8925 | 2025-09-10 13:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 0f5d41b8-dc78-3d1a-865e-18f453c98872 | -12.5796 | -44.6412 | 2025-09-10 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| b31e529f-75d8-3e2b-865b-b7735ecec9df | -7.4845 | -48.2349 | 2025-09-10 13:50:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| a4962851-e4a9-3d54-859f-66ae3f37a2d7 | -15.1021 | -50.1249 | 2025-09-10 13:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 62fd1694-8fad-3cda-bd83-be7ae57456af | -9.0768 | -46.9668 | 2025-09-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.9 |
| b557f67c-3111-3dac-a95e-26692e52c54d | -8.9943 | -46.0583 | 2025-09-10 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 15b44cf8-8b1c-36a1-8137-c23efffeb600 | -9.0132 | -46.0563 | 2025-09-10 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 9a692133-1ed2-3967-912d-3013aa089376 | -7.522 | -48.2318 | 2025-09-10 14:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 74a651f7-2492-3968-82aa-1ba727751c7f | -10.1464 | -46.1973 | 2025-09-10 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 151.1 |
| f8785308-e53a-3f7c-ad10-5f93459814b4 | -6.8521 | -47.9143 | 2025-09-10 14:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 6244974d-5c1f-3cbd-84d6-080fca3a33ac | -10.0157 | -51.6821 | 2025-09-10 14:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| a9a3b1b8-bcc5-3799-8939-7493ab2d6c1c | -11.507 | -50.4276 | 2025-09-10 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 14499dd3-2b8e-387d-8a7f-2b2daf1f639a | -8.994 | -46.0808 | 2025-09-10 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |


[Clique aqui para ver as próximas entradas](README112.md)
