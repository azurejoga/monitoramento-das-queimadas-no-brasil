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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 632c79fa-a5cb-3a16-a440-b2407f55e470 | -2.7041 | -48.6562 | 2024-11-24 00:21:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f38b960-ab6a-3fd2-8dfe-6c8a8ef79c72 | -3.0815 | -49.187801 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9013125e-bf87-3bc9-9d4c-09ff6151509e | -2.168 | -50.119099 | 2024-11-24 00:21:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7180fa1-f491-36d0-b96c-1d6b1ac4b35e | -2.3536 | -49.112801 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8f59360-87a2-3234-b793-72944d1ad856 | -3.1577 | -49.893501 | 2024-11-24 00:21:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90fabba1-25ca-3324-aa0b-f3a358dcd761 | -2.8566 | -51.814201 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75e7b80f-d269-338f-8fae-5daa05cdbe0b | -3.471 | -51.987801 | 2024-11-24 00:21:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df258ea8-d68d-3165-b029-03677b8586fa | -3.2822 | -50.034801 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97f4b386-13fa-3630-bd10-15022db74bbd | -3.4857 | -48.2384 | 2024-11-24 00:21:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ce655c-e1db-383d-98c8-dcfb68a2ba5d | -3.2504 | -53.2626 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cb2aeba-ba6d-322e-9bf4-8f92a001cc1a | -2.2471 | -46.866402 | 2024-11-24 00:21:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459dd398-ac0b-3241-b886-1e4bc8a1d09c | -3.3029 | -50.3573 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 373ed759-3587-36f6-829c-5b87dc9b07d6 | -2.7321 | -46.100899 | 2024-11-24 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a4550b8-fe13-3581-b11b-477c5cfc3765 | -2.2117 | -49.855 | 2024-11-24 00:21:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50b852d5-4478-3a0e-91c7-15d2cc5bb1d5 | -2.096 | -48.884102 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fabf1058-274a-388d-b33b-ec62131fe469 | -2.748 | -48.6679 | 2024-11-24 00:21:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5445a7e-99fa-359b-979f-953fd3900ab6 | -20.321699 | -48.808102 | 2024-11-24 00:21:00 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cbcce0cf-9bf3-3584-9c49-62151a4fa6c1 | -2.4488 | -49.077499 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e64933-d168-3baf-933b-01623c72f806 | -2.2033 | -48.903198 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7420a90c-b9f7-3ba2-9dc3-51087288b64e | -4.0266 | -46.670101 | 2024-11-24 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b335198a-e461-3a2d-8e12-4a8df91c6aa9 | -2.2821 | -53.616798 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da7b889f-5eae-3294-b8b3-dcb5c91ab3c0 | -2.0816 | -48.865898 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4972c00d-e15b-3b47-9f3f-d8ad999a2dff | -2.2542 | -48.992001 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99e5485d-d22c-3958-af98-28a1eacd1cd1 | -3.2537 | -54.205101 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f352ed0a-b6da-313d-a59a-06ea1b1d0f7d | -2.7303 | -46.092999 | 2024-11-24 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53a4b7e2-cfde-3285-8399-0d59fc8caac2 | -3.7853 | -52.292801 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a4d723-e04f-3805-bee1-449fdf31ed0c | -3.2798 | -45.5224 | 2024-11-24 00:21:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d6d17f1-dca3-3160-b617-2a1d1f70598e | -2.6167 | -51.799599 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0e0ee21-8e40-32db-b38b-abd8dc6f627d | -2.58 | -54.033501 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8316beca-e2b5-313a-9df9-d91b18b75fe3 | -3.219 | -49.799599 | 2024-11-24 00:21:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f198070-5f65-3c1a-a01c-f07d0420fbe4 | -2.2235 | -49.8162 | 2024-11-24 00:21:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39169d94-3db6-3dd8-bc9c-4d69028ff16c | -1.8314 | -46.6241 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5f150ff-e98f-3b22-b78c-df48fa748f31 | -3.4943 | -52.000099 | 2024-11-24 00:21:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2167e6fb-37ab-3ab6-a469-ab0c31868052 | -3.2449 | -50.650299 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b37a34ac-41d0-3ac2-9e4f-312d6adefbd8 | -3.5018 | -50.464401 | 2024-11-24 00:21:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69550ce9-7a43-3988-bfca-0605ec5613f8 | -2.0722 | -46.5051 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0869272-8254-34cc-9f70-6aad02ae9121 | -2.2454 | -50.4632 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd27cbee-aabf-319b-8820-cdfda946d61a | -3.1853 | -54.313499 | 2024-11-24 00:21:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a652261c-1f1d-3c49-b76b-7d7958a3d64d | -1.8251 | -46.641701 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9dfb60b-02a2-3379-bfc6-4b8e523de58d | -2.4469 | -49.2066 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff8f4c7-8e34-31a3-b69c-b74a72f2cea2 | -6.8402 | -44.381401 | 2024-11-24 00:21:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 571d0e78-7096-31ec-a846-36428dc64509 | -1.8268 | -46.649399 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c09e53a-76f4-32bb-82fa-4b6da34a16e4 | -3.0955 | -51.317699 | 2024-11-24 00:21:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bef63494-ce7c-32ac-8a6d-23b6c8460763 | -3.0648 | -53.2122 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4c68b2-26f8-3f3a-994d-31b98a9398df | -3.0718 | -50.935101 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 670c8bde-c0b2-3ef4-b9ef-8d55594b06e5 | -1.8216 | -46.626301 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38885221-be9b-3ef0-9c89-c8c9f1ddea1e | -1.4628 | -46.044899 | 2024-11-24 00:21:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ec959137-1b7d-3f33-909c-c4e5ba0ff0a8 | -3.1551 | -50.570999 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f1aa05-bdfb-3c28-a293-cf17a9bba63a | -2.0988 | -46.259899 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7036bf0-be8c-30d5-bff6-db2a10708092 | -3.1969 | -52.5583 | 2024-11-24 00:21:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53f6ebb3-549d-3cb1-a6d8-a8a1d27a1e74 | -1.1302 | -48.3498 | 2024-11-24 00:21:00 | METOP-B | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b98504d5-5181-38da-b3fd-0a025bd6d449 | -3.5123 | -53.798199 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0084db65-499f-3ad1-a26c-d1549052fc2a | -2.4607 | -49.039101 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5730a2d4-683f-3beb-af6b-013753089234 | -2.1297 | -46.622002 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f51e94b-5eb6-390e-8ca8-f61d89fda927 | -2.7353 | -49.114201 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6c31f35-db33-3bb3-ae08-ac2e94fa462d | -2.3074 | -49.044601 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d10130c-30e0-322a-98d1-536e6f80c19e | -3.2678 | -50.6147 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c397ca07-1e22-3d51-9c85-eb5f884468fe | -3.2341 | -54.209301 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aea31535-f243-3d2a-b219-a8da391914da | -3.2682 | -50.432598 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5af37745-96ae-3ce1-9dc0-fadbbaca12ba | -7.5661 | -49.397202 | 2024-11-24 00:21:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b6d4c48-50f0-3192-bc92-05a4bb9c9021 | -2.9089 | -54.268101 | 2024-11-24 00:21:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d4e43b2-2d3a-340a-8006-b0bec7c41993 | -2.3716 | -50.3834 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd7a36f-e980-339e-91c7-1125af8a8a45 | -3.2806 | -50.027802 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71040a6d-f683-3c13-9b57-34f6a88be5c7 | -4.433 | -44.580101 | 2024-11-24 00:21:00 | METOP-B | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4a4a8dd-d0aa-376c-9f20-f1bfae8d6fbd | -2.2851 | -47.306099 | 2024-11-24 00:21:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae55578d-27db-3a6c-831a-b24430d34dbc | -3.2488 | -54.229401 | 2024-11-24 00:21:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55f38f4a-b52d-314f-bcc0-f23b0e4f5f9d | -2.17 | -53.620602 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5469cf7d-b160-32d9-aee3-5e37e3deede3 | -2.0288 | -54.459499 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef4a3525-5bc0-3784-87b6-c74a3a0cdfb4 | -1.6104 | -52.5882 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd68cfc-9f1a-36ad-a247-b1d0f3da76c6 | -4.2003 | -45.357399 | 2024-11-24 00:25:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 29ef8a94-daf5-358a-8afb-5c52f8836db3 | -2.243 | -49.216 | 2024-11-24 00:25:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3476fc4-49b5-30ed-9f69-4b55a4168b72 | -1.4028 | -54.458599 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6de4d4e9-bd14-355c-9e6a-f8dabf8a5b66 | -5.5878 | -45.206001 | 2024-11-24 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 214b8627-02d8-348d-a8d1-3dd309ffed62 | -3.59 | -49.341 | 2024-11-24 00:25:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c25e4a74-b0e5-3cfa-9c2b-22e536d4324b | -3.3849 | -50.309299 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 762d0fa3-df5c-3d15-91ce-7feadfecd0f0 | -2.7059 | -46.256401 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2e5e609-453a-3bf8-bb3e-4279554174dd | -1.2269 | -53.674099 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdfea4bf-618b-3a55-9230-794627e84316 | -4.6306 | -49.664001 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d96843c3-028e-3879-967a-3e737368fe47 | -1.6132 | -54.3899 | 2024-11-24 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7939bb51-cb9d-327e-89ae-b0a5a5e27b45 | -0.887 | -52.756199 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5472d368-676a-3fcf-9bb8-7942db407ae1 | -2.1786 | -48.930199 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44717907-e55e-351e-8c7e-ce269453f652 | -0.8894 | -51.714401 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0c027bfa-8733-3254-9dc6-dcc0e0a9d2b0 | -4.1786 | -45.621899 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8e02070-72a0-337d-9ccb-35092bbab2af | -3.1038 | -45.7882 | 2024-11-24 00:25:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5cbbe005-a81b-3f9e-931f-76470d667abe | -3.4189 | -50.3694 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8831cf37-6ab0-359d-8ae2-31fbea07a976 | -0.9541 | -51.636501 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd292e59-20e9-343b-913c-56ab1642fd9c | -4.5273 | -42.906399 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 746ba55e-a35d-3249-a7e4-884ac3c626c4 | -2.0653 | -50.303101 | 2024-11-24 00:25:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b9cc611-104b-3bf5-a359-0d9ca38994d2 | -2.0107 | -51.160599 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 769ce56c-83d0-3460-9add-89bef966d2d1 | -0.9149 | -51.645199 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 169ce6b1-76c0-360c-900c-110be8b9ae7d | -4.3817 | -49.748299 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18a35be3-d7b7-3a9f-af6b-069a9183978d | -1.2342 | -51.783001 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49f645bb-4c53-34e0-866c-d2418cef3c73 | -4.5343 | -42.892601 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90f9dedf-81ce-34b3-9011-a1f4ab5b6e39 | -2.9365 | -46.680302 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eba8303a-bf43-38f7-b8e0-44693b8b91b6 | -1.48 | -52.510899 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ceccded-d3d4-3a9b-8fda-0bfcebac0cb7 | -3.6832 | -50.630699 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 914366b6-002c-3d1f-9f3c-2f6e24ab333a | -4.629 | -49.656898 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5646a347-6bc3-39a8-96e0-70ac977da7ea | -5.4965 | -46.244301 | 2024-11-24 00:25:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74f265b1-84e8-3a26-9717-3a2ee947bd1f | -1.3642 | -53.827999 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e080564e-c736-3e84-82d8-bc020b01ce99 | -0.2679 | -51.606998 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
