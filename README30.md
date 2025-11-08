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
| 78fef4ef-4436-33e1-96b8-3fec3abbebf3 | -3.65573 | -50.2711 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd1d93e4-739c-3dd0-9455-7703bb1215db | -2.48539 | -49.11216 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f98d81bc-429b-3aae-8cdc-f89a35952eb9 | -2.70864 | -49.54752 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fa00fd07-52c1-3565-b299-9c6049cf91f8 | -3.0898 | -50.32314 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cda0e7a3-dc1d-36ba-b96d-d8427740c867 | -3.45291 | -48.82125 | 2025-11-08 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14f73278-533e-3211-894b-e8750bb2a1b6 | -4.72577 | -42.93774 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 82c49c48-61e9-36a2-b4df-3696c9e5eca6 | -4.6862 | -46.39952 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50d3285e-ff82-3da1-93a5-08fe35d9d2d4 | -3.14785 | -50.29303 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 474a34df-e694-3ffb-91fb-41326d04b571 | -3.25271 | -52.91349 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b40d757c-f538-302c-a910-35229fda5ffc | -3.52057 | -52.89481 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d3881a4-800e-378e-8a78-f8e50727ddf5 | -4.71888 | -42.92545 | 2025-11-08 04:55:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73ebf2fe-f9f9-354e-9fd6-49199857c617 | -3.65595 | -50.27396 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87e497f5-af89-35c8-8d9a-b06c948353fd | -2.26057 | -47.87574 | 2025-11-08 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ceb0b731-cbeb-3c0f-ad31-ab06c5d9d18b | 0.78612 | -51.9978 | 2025-11-08 04:55:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db232d96-95af-338f-ab0c-5eb4a63f45d2 | -3.10778 | -49.46816 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c21c1e04-b6ab-35db-bdb1-95d27d239362 | -2.8956 | -53.13243 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a385f308-e4a2-3f5e-aa59-d73aa4b08aa5 | -3.14657 | -50.30131 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f19fa2e3-ed0e-31e9-b03a-567f1ed7cad6 | -3.6521 | -50.27055 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e5164a0f-f320-36be-8603-318d44025954 | -3.05897 | -48.72298 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f77b752-9947-3f1a-9cb8-04efd18ebed8 | -4.28738 | -45.88884 | 2025-11-08 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72f49fb8-ccf3-375a-b046-e61eefa2b4ae | -3.09373 | -49.25777 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fa64f1a-251b-3b30-bd75-712e2491ec74 | -3.45382 | -48.84203 | 2025-11-08 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 80cc4b57-1871-33d6-bd2d-aa7143df876a | -3.28976 | -52.09055 | 2025-11-08 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f584b6e-f28f-3212-879a-51ec2a485e79 | -4.7236 | -42.935 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5a431a3-c8b4-3a21-bf83-fa1163ea2459 | -3.4462 | -43.1501 | 2025-11-08 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6343d05e-a2b8-3180-aa48-97bb6177de9a | -2.61434 | -49.22971 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0d132bd-0723-3c57-85a2-6085bbda1996 | -4.73235 | -42.93427 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80e5e788-b4c7-3774-b59d-e81125b5d640 | -2.5229 | -49.44482 | 2025-11-08 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d006f57-4c25-3684-8259-7f9d7af44388 | -3.25638 | -52.84673 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d84cd8a-f581-3a7e-8a0b-afb9e55ee322 | -2.66738 | -49.46056 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7467db26-c256-3a70-bd71-bc074e21ef8a | -4.41043 | -45.61395 | 2025-11-08 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15fd2ae1-2497-312c-8ad4-ca96e28ae94a | -4.68475 | -46.40952 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 79dff12f-f5f1-3e40-b182-24cd49846ffb | -4.71824 | -42.9298 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2954382-95ca-3dc7-a09e-6d3bfb0fd3de | -3.4481 | -52.81611 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bd4afd2-8b79-3eb0-b94d-3e117b658fbe | -3.84028 | -49.82138 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e418950a-6067-3034-a617-e05d9a498263 | -3.5321 | -47.54593 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 79425070-d342-3c88-832a-280da19c720b | -5.72244 | -43.52826 | 2025-11-08 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76f7ad77-a3ef-3fc2-9bf5-ca10c50cdd7e | -3.44249 | -43.17437 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 594906e7-9ce0-33f3-98c8-7605626e0578 | 0.69081 | -51.4606 | 2025-11-08 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 890acce9-7c2a-33d2-9a47-89b3d545f508 | -5.41052 | -44.82626 | 2025-11-08 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05e83f41-f500-3c11-82cf-6c8cb9c45cbe | -3.65659 | -50.26975 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4f029ac-0ef1-3301-8d96-1e6634c8314f | -3.03292 | -50.31014 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eaa42e5-fbe5-3f5e-b0fc-8973eb45a307 | -3.52415 | -47.54053 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84c442df-8004-3e91-8ec8-7defb3c7fd58 | -3.33804 | -50.19599 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1dff255-6051-38e1-a94f-746f6351bf34 | -4.30008 | -49.39318 | 2025-11-08 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d3c76516-57fa-33b0-a60c-7ed35382a815 | -3.39787 | -45.4321 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f897948-c680-3697-bed6-4f54d57a2286 | -5.76962 | -40.80389 | 2025-11-08 04:55:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d53b5f53-c5c6-3371-9804-60152f6619e1 | -3.73241 | -49.68508 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50971631-2e64-3c24-bc7d-8c894bfb3bf4 | -3.51231 | -49.93963 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e10f083e-a8b0-3069-ad51-2340cfd725b3 | -3.6676 | -51.95673 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9326b48c-253d-3ba6-b873-f9d41b8bf8fc | 1.34368 | -50.71258 | 2025-11-08 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31284018-c7cc-3e5e-a831-5459e084fec1 | -3.10849 | -49.46363 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 382b411e-dc2d-3c2a-aa63-0079f5052ff1 | -3.34652 | -53.2244 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 980444d5-a0fc-36c0-889d-0351e2b61362 | -4.73022 | -42.9315 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4af01912-a2b1-3851-9980-12ab3d4e797f | -3.01938 | -49.43789 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83b98f9d-2229-38bf-a502-547c66df09bb | -4.20582 | -46.40013 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db0964a6-d458-338b-b114-d883ebbb6136 | -3.5857 | -51.24747 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dafd7c4c-776b-3687-b1aa-34d2b34b4677 | -4.73297 | -42.92979 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45f86d77-16c5-309d-a47d-e3c46897fe48 | -3.01936 | -49.44071 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24492a44-9145-37ad-99b6-d6d786f5cfcb | -3.95168 | -49.02339 | 2025-11-08 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 184ef352-f18a-36df-ae64-3658c16ed7ce | -3.35098 | -50.21411 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8db27362-2399-3d87-9ce6-d22ddc15618b | -3.0977 | -50.33184 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6c7c513-2f31-39b7-95ff-a19d7ef217e6 | -4.49617 | -45.13781 | 2025-11-08 04:55:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b844541-514f-3867-b53c-4a78d45fa5a5 | -4.69094 | -46.4002 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f59365ce-0925-30e5-83f1-58fbb7192116 | -3.25311 | -53.27684 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38f25361-35e1-3442-ba4d-12a48fbfdedc | -5.47304 | -44.6004 | 2025-11-08 04:55:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a090bc9b-09bf-357b-894f-7b5a27925ae1 | -4.33681 | -45.72702 | 2025-11-08 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1eea33a-88a2-3e7f-bba5-6ae1ec10b3f3 | -3.65639 | -50.26691 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 180050ea-9f47-3b55-b81d-18fea591dbc1 | -3.73169 | -49.68969 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64bbd0a4-4884-3a81-9f69-e7febeba9053 | -1.69965 | -54.67415 | 2025-11-08 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d28ae9d4-c1a5-3fe4-b56a-7a7c78e90770 | -3.52843 | -47.54124 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b84ca698-037b-321f-b88e-4803a10b060d | -3.04842 | -50.2574 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9111f214-6a47-339e-9541-a7829c310dfe | -3.31156 | -50.12725 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 565225a9-2a4f-3438-ab85-508bed58fda5 | -3.95159 | -49.02494 | 2025-11-08 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95d9d5ec-e8f6-3ff8-b937-d8b8438f4773 | -3.65232 | -50.2734 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 105e3ff2-3fe0-333e-9067-d91af44ac5bc | -3.33376 | -50.10449 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebbf5242-2c4e-3c56-9f8a-ce7dfff5e30c | -4.96777 | -48.01947 | 2025-11-08 04:55:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7aaa31eb-5c36-3124-bc3c-e2a9b42b2a72 | -2.52595 | -49.44988 | 2025-11-08 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b100e040-2e4d-3d30-817e-55a18ba6e18a | -3.77303 | -49.99834 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe3555b6-f981-3be0-87d8-eb648bd31b9c | -3.0149 | -49.4447 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 438d70a7-adb9-3b50-80b8-26019cae1583 | -3.31713 | -49.13649 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b198163-2728-374b-af13-6b2bb191feca | -3.32172 | -49.13224 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1495d8d6-37e0-3f35-aaef-a60e537028c0 | -4.46711 | -45.3344 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fc7dfa1-e3e8-3448-a451-0266b22bf273 | -3.39701 | -45.43774 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fa6a529-0f54-3fa9-ae2f-07b7a513681e | -5.05859 | -43.31886 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 162d8fc6-79c2-3b98-847d-8f05bfad9eb6 | -3.69766 | -53.75539 | 2025-11-08 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a7860bf-8188-3bea-946b-9e93797a0365 | -5.77023 | -40.79987 | 2025-11-08 04:55:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 756d0485-d843-3e6f-a09b-40fcc66f2bfa | -5.37975 | -44.73645 | 2025-11-08 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89163681-2952-3b83-aea4-4f6a43c8cb9a | -3.98268 | -49.87279 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 211b5d0f-3dee-302d-bb4d-c12a19d36d0c | -3.71536 | -42.72229 | 2025-11-08 04:55:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20f498fb-0c41-39ff-8692-31cd3200028b | -2.66668 | -49.46507 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9cd4501c-20f7-36cc-b3d1-2205349e14b0 | -2.44131 | -49.34649 | 2025-11-08 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08d2fbb5-c56a-3e2a-b87e-ac82d32f81fe | -3.64933 | -50.26862 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8df9f784-7b9f-3fc0-91e9-77cb9beffa81 | -4.81451 | -45.57896 | 2025-11-08 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb6c9b04-6ac2-3c78-82ca-db95692d6c27 | -1.90925 | -46.5134 | 2025-11-08 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3c7fc46-db9d-30f4-beea-81de915cf2f8 | -2.56483 | -50.64644 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f70b8a1-913d-3c02-b738-bd9ce259e6b9 | -4.6855 | -46.40437 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ccdca04d-2734-3a05-b1ff-bd8ea1436b65 | -1.70022 | -54.67054 | 2025-11-08 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a8d7629-df11-3bc8-bcd8-c7cb92d52d6f | -3.01112 | -49.44129 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45a08654-d471-36e7-9ad7-cc8849b7395a | -3.4373 | -43.16961 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README31.md)
