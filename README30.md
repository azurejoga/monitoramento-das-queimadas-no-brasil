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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26530331-ac74-334a-9966-88b932464a46 | -16.31737 | -58.25632 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4e931c78-a7eb-3dad-9e45-0f2e0893b108 | -16.29915 | -58.27464 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 74f649c4-4026-349b-9626-e6fe13147acf | -10.5521 | -46.9785 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| c2bf984c-b0c2-3287-9c24-789c1c73bb75 | -10.4947 | -47.0078 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 203cca68-eac3-38cb-9957-4852d52c7a1d | -16.3047 | -58.2676 | 2025-06-20 05:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 7071dde5-83c2-3f1c-87c8-f020fad45aa5 | -10.5137 | -47.0055 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 451918fd-8e61-34f0-ad6d-fc9edbf8b7e1 | -10.4364 | -47.104 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 163.3 |
| af480cbc-cd35-3b31-94b1-f2f5e8b75cdc | -10.494 | -47.0525 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| bc84e858-7218-3f0d-a20f-0d485bb08f71 | -11.1468 | -46.6347 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 561a7584-02c9-3f96-9130-92633aaea57b | -14.0404 | -53.3669 | 2025-06-20 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 25417a68-78f7-3179-9b5d-129fda933e56 | -10.5134 | -47.0279 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 1774e5d4-15fc-3891-8f3b-f8ec1a997fb9 | -10.436 | -47.1263 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 0f72af89-7ade-31e8-9113-a58fc93e6a0f | -10.5524 | -46.9562 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| bd379439-ec4a-39ba-bb96-80311ea37afa | -10.4944 | -47.0302 | 2025-06-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 155.8 |
| a47d1b79-ebe1-3f52-ad22-18d52a011393 | -4.77231 | -47.24881 | 2025-06-20 05:50:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| af63cbc1-8445-3f7e-a267-af9d7bc38550 | -4.37931 | -48.07143 | 2025-06-20 05:50:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7020ac39-8854-3cb8-93bd-86b2cbdc5ffd | -7.20933 | -43.07284 | 2025-06-20 05:50:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| bc39db6b-9e97-3af8-9662-95de0519b157 | -6.67288 | -44.24529 | 2025-06-20 05:50:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 293ccc7f-a2bc-3da1-a772-7ae4e6a2436e | -3.02858 | -49.42551 | 2025-06-20 05:50:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3ea30b8a-258b-3de2-99e1-de0ae27f280a | -2.91227 | -48.23368 | 2025-06-20 05:50:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b40c7ea6-9f2a-3e5d-a85b-08a776e8f440 | -7.22029 | -43.07987 | 2025-06-20 05:50:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 1cbc3b3e-0f7f-38b2-acbe-e61f7b642869 | -7.21147 | -43.05785 | 2025-06-20 05:50:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 3c806c51-073f-3fad-8480-7378ae2e1824 | -3.03803 | -49.42692 | 2025-06-20 05:50:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 77384e2c-5cde-3686-902a-a4ae7a812eb5 | -7.21104 | -43.0632 | 2025-06-20 05:50:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| ef401966-0478-3d3f-b163-1917a2710f6f | -7.22061 | -43.07444 | 2025-06-20 05:50:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 89486f1b-f9f7-3fa5-bd0f-a5d344d70e8f | -7.22275 | -43.05943 | 2025-06-20 05:50:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 35685cab-7d5e-3530-b1e3-85cfbf700a82 | -7.22232 | -43.06483 | 2025-06-20 05:50:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 4b791690-1e54-3289-ab47-909de1f61794 | -11.13818 | -46.62454 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ffb10174-0406-3f79-bb8a-5e0842a1761a | -11.94254 | -58.73229 | 2025-06-20 05:53:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 84457937-de7c-320d-a259-6a3ca30e97ee | -10.49231 | -47.01925 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 198c7bb0-5e46-3af0-95e0-e1d9572cd719 | -13.39318 | -48.44962 | 2025-06-20 05:53:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9fcd5924-f94a-388d-9812-d46bcf78c5cd | -10.48953 | -47.03838 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 24cfcf19-9c10-33d5-829a-cce169b72dec | -10.92312 | -49.27385 | 2025-06-20 05:53:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dd9659f1-2f49-3907-963b-cf9c2de8a9f6 | -10.55424 | -46.97507 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7bb6f87e-dbbc-3036-b7f0-f9f34f2e2707 | -10.07501 | -52.74429 | 2025-06-20 05:53:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 13379b21-5000-34be-a0fb-47f6925ff8ff | -7.96851 | -46.2254 | 2025-06-20 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5a9a0c70-0e69-385f-809a-349dd80f37fb | -10.43444 | -47.09827 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 08b37658-1d11-38ab-9add-e5b556b26810 | -10.43308 | -47.10776 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| c6f68189-6254-3309-b54f-ec1bc4dccde3 | -10.55562 | -46.96545 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ceaf8ef7-6611-34fb-9bc4-dbef2a980550 | -10.50144 | -47.02051 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9bf05cd5-4f60-3b5a-baa5-651d7082c0c7 | -11.14609 | -46.63607 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 837a82ca-54a1-34cb-8254-732e97ca52b7 | -10.48815 | -47.04789 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 97420303-1ccd-3716-81aa-a4ab8f0a2ee5 | -10.50004 | -47.0301 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 2d1bdd46-3073-30e1-b3e1-fea41caa8e32 | -10.52098 | -47.58317 | 2025-06-20 05:53:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ee47c394-7074-3427-b7f7-9b408671bec5 | -10.50284 | -47.01091 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 3351c6b1-50cc-35ae-bff1-c9d87fd6fde2 | -9.45743 | -57.83553 | 2025-06-20 05:53:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| afe7474f-647f-349d-a5a4-d9bdf4151b9a | -10.66055 | -49.36837 | 2025-06-20 05:53:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 521c17c8-53a0-368a-b624-26a710cfcc9d | -12.21839 | -45.52941 | 2025-06-20 05:53:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| efe5004c-15e8-3bf4-94fa-faf6de07244a | -11.12634 | -46.65834 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f0d9c322-7664-3c69-b8c8-0a8d7d34878f | -12.50579 | -58.34972 | 2025-06-20 05:53:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 4c636084-44ee-38b1-99cc-c621fcf29777 | -8.26018 | -44.95663 | 2025-06-20 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f38381cf-b94c-3c94-b4e6-7781156a805e | -10.49371 | -47.00965 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2f2575da-69a6-366b-8268-75bd45c5c641 | -11.14751 | -46.62595 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 9ce09b96-033e-39ff-be46-b8ef2af7e6f6 | -10.557 | -46.95579 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c28596b8-3c4b-381a-a85b-cb22cf11ec6a | -11.13676 | -46.63463 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 227a856f-148c-3654-aae7-023cd37bc929 | -12.20295 | -49.61909 | 2025-06-20 05:53:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f398c40c-b718-342f-8282-67ea940b1bb3 | -8.16371 | -43.14841 | 2025-06-20 05:53:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 8bcdd624-75ac-3dea-ace9-2174292a5ce5 | -13.09545 | -52.29416 | 2025-06-20 05:53:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9d02c8fe-4eda-3bd2-b82d-990834895b79 | -10.54372 | -46.98339 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| bc7a778b-bcb6-31db-9073-7adb49e9cba6 | -10.72569 | -49.55062 | 2025-06-20 05:53:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bdb9e627-6b3d-3e4b-8734-1308172226a5 | -12.34221 | -49.30685 | 2025-06-20 05:53:00 | AQUA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9bffeddc-bebb-3c68-ae59-86a83f9a69b3 | -11.46869 | -47.28705 | 2025-06-20 05:53:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 239d012e-bebf-34a3-b9dd-00cfd2e45579 | -9.47794 | -56.07669 | 2025-06-20 05:53:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 8e53ed5c-9335-3584-9a15-7a6d33d8e82b | -10.49092 | -47.02883 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| d8e1d5d8-1051-33b5-a813-071e6a753fb2 | -10.5451 | -46.97373 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 74ce23f3-437b-3ec7-abc4-c006a9d5b723 | -9.33085 | -47.83248 | 2025-06-20 05:53:00 | AQUA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bb8991e5-1192-37bc-a605-76ad28b41a0e | -7.96988 | -46.21586 | 2025-06-20 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9a9f7e3b-49c1-30a5-b594-df05af78b583 | -10.93818 | -49.42921 | 2025-06-20 05:53:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d7eb64dc-926b-3b64-b633-138c8ec9b504 | -13.24081 | -49.83107 | 2025-06-20 05:53:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 25582cd6-84b9-3884-8a90-8fa41e7bb47d | -10.50423 | -47.00134 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| d2885069-2cfe-3ae5-b2c0-a8ab5f8bfdef | -10.07717 | -52.73088 | 2025-06-20 05:53:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b3562ee5-dfc5-3dd2-a24a-d9d0bb7aee4d | -10.4818 | -47.02753 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c8b6ea8f-1f29-3012-b289-fee4fe5e00ae | -12.35102 | -49.3082 | 2025-06-20 05:53:00 | AQUA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 43616ed3-f95b-35ec-ad32-2f56e5b36932 | -11.31374 | -45.20056 | 2025-06-20 05:53:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| aeefa563-281b-398b-b077-b4a11feb88e0 | -11.95097 | -58.72926 | 2025-06-20 05:53:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 803cc844-b17b-3732-a135-811dd17c874d | -10.43172 | -47.11717 | 2025-06-20 05:53:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| f3eaf7dd-6e6c-39ac-bef9-1af608f2f39b | -9.33218 | -47.82353 | 2025-06-20 05:53:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 244eb345-3a4c-3145-8ac7-50d07f73b0ef | -14.43219 | -48.91528 | 2025-06-20 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e7bb48dc-5a5e-36e1-af45-924febf55315 | -16.30358 | -58.26586 | 2025-06-20 05:55:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.7 |
| 18e9767d-d18f-311a-89a6-05d2defd8490 | -14.02947 | -53.36691 | 2025-06-20 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e2063ffc-b51e-3e84-bfe5-6faf8fd4fecf | -14.03984 | -53.3687 | 2025-06-20 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 420796ac-2854-3b89-86bd-bec80ba1825e | -15.47535 | -46.59767 | 2025-06-20 05:55:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 91d695e0-6512-3059-bd92-d66976836173 | -14.0316 | -53.35413 | 2025-06-20 05:55:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fc20678a-a520-37e0-83ab-a7079662dfb9 | -15.4769 | -46.58599 | 2025-06-20 05:55:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| acf5569d-6273-3db8-8199-be929bd70f17 | -13.77501 | -54.1913 | 2025-06-20 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1b17f622-c6df-3ea5-96d9-d01adb24e82c | -10.494 | -47.0525 | 2025-06-20 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 968782f6-7372-3c83-bc04-c29d0242cb35 | -10.5524 | -46.9562 | 2025-06-20 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| ec6eebc0-3152-32b9-b80a-8e16eda7d699 | -10.5134 | -47.0279 | 2025-06-20 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 3f3952c2-9290-39a5-9ae4-c29b0f4be3b3 | -10.4944 | -47.0302 | 2025-06-20 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ae21650c-964c-3586-9aa9-e80a3d723ee7 | -11.1274 | -46.6598 | 2025-06-20 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 2b220d8b-564f-39a8-914a-977d633cfc14 | -10.5521 | -46.9785 | 2025-06-20 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 72c36d56-be58-326a-a63e-efe9422ebfaa | -11.1465 | -46.6573 | 2025-06-20 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 93a30dc9-4d8a-3399-9401-b93cb4666790 | -11.1656 | -46.6548 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 695fa61c-4d87-32b4-ae02-faa3b46f8f3e | -11.127 | -46.6823 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| da386384-423f-3723-910d-d63c0f2d53b2 | -11.1274 | -46.6598 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 1d16caea-43d8-3cbb-bc22-28b8d4943cd7 | -11.1468 | -46.6347 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 729147d5-f8fb-3d6f-a2d7-cd076dee80c6 | -10.4944 | -47.0302 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 30544427-9230-3532-b2ff-300f90d3b6b1 | -10.5134 | -47.0279 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 223ceb7f-5c5c-3ace-bbe4-1094bb7f6427 | -10.494 | -47.0525 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| efd886bb-09e5-3283-bcb7-aabcbb20a52f | -10.5521 | -46.9785 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |


[Clique aqui para ver as próximas entradas](README31.md)
