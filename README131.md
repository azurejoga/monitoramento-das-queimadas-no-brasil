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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37a40c36-bfdc-3259-9318-fc725df7679d | -9.73186 | -48.41354 | 2024-10-25 16:50:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b0423bfb-2c05-30dc-8a18-a57629b2f808 | -9.63883 | -48.5359 | 2024-10-25 16:50:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1ecf5815-9561-3702-9e2d-443f3eed126b | -9.63826 | -48.53232 | 2024-10-25 16:50:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ed72675f-239c-380c-9c25-7aa63bfb5946 | -9.6821 | -47.90332 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a99a8ae5-12fe-3983-a9be-c63b335974ee | -9.68208 | -47.72663 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79e0fcf1-a363-3fdd-a471-f6faca930bdf | -9.62494 | -47.61154 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c4e881ad-8287-3916-86b7-1e9feaa47138 | -9.62433 | -47.60774 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 30dfa155-4c7e-3ded-ab1e-eee472d65d07 | -9.62372 | -47.60394 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fdcf99d1-7e42-3b68-b9d9-1681084d5e0d | -9.62311 | -47.60014 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 121b61c5-b6dd-3885-9619-34eed9a73e64 | -9.62189 | -47.59258 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6848080c-29b8-3316-b9ed-f68c21cd9f11 | -9.62149 | -47.61211 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 16cd324c-72c5-347b-90cb-caa815de357d | -9.62027 | -47.60451 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eaf97e49-c6b0-3813-911a-90187c19855d | -9.61966 | -47.60071 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 50b98b09-6831-3a59-bffd-a77aafd9f336 | -9.6195 | -47.64366 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e7ee6137-b5a8-3ae5-84b7-9d7dbbbe6f78 | -9.61905 | -47.59692 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5c2c5b9d-3585-3652-92a5-3322663d2ec9 | -9.61805 | -47.61267 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 48cc7a8b-d8b1-38e6-a43d-29522ac633b0 | -9.61622 | -47.60128 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a186181d-047e-3014-8d65-32e3587833d9 | -9.61561 | -47.59748 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dae16ce8-ed57-32a6-aca0-f76cc10fdb7c | -9.6075 | -47.59105 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9af12b9a-1828-3fa3-9713-f18324856b33 | -9.60466 | -47.59541 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de446c4d-0bde-3e7b-a548-a93f6ab14cac | -9.60405 | -47.59161 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f617d433-ca91-3444-9d95-07f3d3ebc371 | -9.59191 | -47.73383 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5331680b-a124-398f-9628-4fae49db7bef | -9.58848 | -47.73438 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3d10ab43-85ac-32e8-b62c-5c2edf9c43f2 | -9.58788 | -47.73059 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c633467-6931-3f85-bb6a-8c7fc0e4012c | -9.55581 | -47.72807 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05198286-f112-306c-a0ee-52551728a559 | -10.54295 | -47.77514 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ed138fa2-0582-3ba8-851a-4e10ad67d510 | -10.53246 | -47.73113 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bc566970-d316-37c3-a377-7a22963cdbaf | -10.45157 | -47.70929 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 28383452-a962-3242-bd0f-c4de1a2e55c4 | -10.45038 | -47.70172 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 70c2bf17-7ebd-3774-a9e5-426f1d5aee44 | -10.39386 | -47.61086 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7235c2f-ca35-3fcf-9f53-c46fb740ef7d | -10.35215 | -47.67972 | 2024-10-25 16:50:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f245ebdd-e4e0-3492-9385-d7798f44ec37 | -10.34038 | -47.80421 | 2024-10-25 16:50:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55407e78-c65e-361f-aa10-a921e59bfaca | -10.29494 | -47.80381 | 2024-10-25 16:50:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1388ee54-e342-37d7-b5f3-cfc692f26c1a | -10.19478 | -47.70543 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05c33147-b126-3381-8623-750eee5949ac | -10.19246 | -47.62495 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 368d44b3-ca1f-36c9-b040-0b62d3cee3c6 | -10.19196 | -47.70975 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 403f3395-058f-3890-ab73-3daf6d2cb1e9 | -10.19137 | -47.70602 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65cda412-2d7c-30ee-af0d-b1cf5ae14994 | -10.18904 | -47.62551 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6a330b55-635d-3268-b1aa-c5387af0f97a | -10.1594 | -47.76875 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5e9c70b5-80c3-34ff-8f6f-23826db264af | -10.159 | -47.76823 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 76944470-2632-3a68-b2dc-b2ef3e3d7e0a | -10.15559 | -47.76883 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 85267a84-9a8a-3a32-86ad-c866cf100b8f | -10.15501 | -47.76515 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ad7e795c-489c-3c0a-839c-54072bdcb7d5 | -10.1497 | -47.73141 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da92ad59-eccb-3974-85e4-ea26bfe749dd | -10.10175 | -47.80426 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61ca21ba-b3d4-32b2-b9c1-b25bbc2e2173 | -10.09834 | -47.80482 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6322bf6-2de6-3265-b431-2304f308dcd8 | -10.09821 | -47.78206 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 50bcdce6-4c96-362d-9bcd-3c2ed4b85a98 | -10.09762 | -47.77836 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 88946026-9a91-39fa-acc6-79957e616967 | -10.09421 | -47.77891 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a194f974-f661-3cca-8b97-f263c80a4761 | -10.09093 | -47.80224 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 302a8312-8541-31ec-ad6e-cac22da5a60c | -10.0734 | -47.73637 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d8d1197-23ce-3317-a8f8-d45301af83fe | -10.0728 | -47.73264 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fbc6941e-0d52-3884-b394-41e9ee215099 | -10.0722 | -47.72889 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a5663db8-d915-3108-bf17-0d7763f09c2d | -10.0716 | -47.72514 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56663d98-8feb-3e8b-b9d1-2e82c76f7117 | -10.07099 | -47.72138 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 50e036e3-f57f-318b-9df7-6ae380686793 | -10.06938 | -47.73319 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c155c5d-f358-3dce-b4e5-9886e4404075 | -10.06818 | -47.72567 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a055a62-1e3d-3cf8-9cb3-cc37d21ac30c | -10.04088 | -47.4459 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8f3fd1af-3263-3331-9271-122dd9d2a7e9 | -10.03627 | -47.61471 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 53c387b5-ef5b-3804-be0d-d0ffb96145ea | -10.03284 | -47.61529 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e9a5371d-1b63-3a7f-99b9-ac7407057fc1 | -10.02795 | -47.47559 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 785deeee-2801-3f8f-9713-c02d6679cd71 | -10.01981 | -47.46902 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 58fc5244-6a0b-35f8-a008-ecb553a58029 | -10.01547 | -47.44216 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 18a637b7-3783-311f-8400-1e8ec88d6b48 | -9.99979 | -47.76007 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5fcb627b-72b6-396b-af99-46aa2b25355c | -9.99919 | -47.75635 | 2024-10-25 16:50:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b94412df-bf72-3bf0-9e1f-e29a4c67b1b4 | -9.94871 | -47.59433 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 100cdc42-39ef-3f16-b6c1-cd51e78d8070 | -9.85271 | -47.84919 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31d80ac2-b83e-3f3a-bcc4-0ab95b2c5324 | -9.8493 | -47.84972 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9951a6d-bd0a-3511-b104-36d2ca529877 | -9.84589 | -47.85026 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d09b640-8e7e-3f96-a990-726fd90ba591 | -9.84569 | -47.56435 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 91d16798-f620-38df-8659-d4bef8a21254 | -9.84347 | -47.57254 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 106b976b-6538-36ed-a23c-6abce289304b | -9.84286 | -47.56873 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d30590bf-7604-3159-abfe-b8b8ee18b329 | -9.84196 | -47.85043 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7aa42654-4860-38ae-a89e-4022fd5ea0b9 | -9.84064 | -47.5769 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6281512-a027-3224-87e0-dc0ff923cad9 | -9.83781 | -47.58129 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32270033-ff6c-36d3-a5e0-d97ec2cbb142 | -9.8372 | -47.57748 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39ab3edc-5ef5-3956-b144-b3ab4a4da413 | -9.83679 | -47.83985 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 12153225-9420-30a7-a270-8b57bb0cc106 | -9.83572 | -47.85527 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b374bf2-64d2-3ee6-b55b-7f1e7ba0ee99 | -9.8329 | -47.85951 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c9e64010-41ba-3dad-b5e2-e38943acb31f | -9.83007 | -47.86378 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8fafdf3a-3b8c-304a-999e-e14899d67966 | -9.82315 | -47.84208 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46fa83fc-d1b3-3638-9e6a-216cb33bf61b | -9.82245 | -47.59553 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6ba5aa85-f8a5-3459-81f2-d23f3c633084 | -9.82184 | -47.59174 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 39f8a220-6732-3c14-9d31-848d0cb28036 | -9.81985 | -47.86551 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a73f7a8a-521e-3549-9614-df3763a77125 | -9.81974 | -47.84263 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1551da4-c114-3b38-b89c-f634de0b39b4 | -9.81915 | -47.8389 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 70432c5c-fd43-3286-8e7b-068728c3bb12 | -9.81632 | -47.84317 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9ae613cd-5a3c-34bf-bf35-9a68ff02530b | -9.81573 | -47.83944 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aee7e680-9efc-3830-b078-44786994ed66 | -9.81419 | -47.67405 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5829ad55-0605-397b-a08e-9a9947fb9c7d | -9.81291 | -47.84372 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b60789a5-3d02-3dea-a759-0d9c2a304a28 | -9.81232 | -47.83999 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82071c53-e88f-3a46-9b0b-36c8582f3562 | -9.80211 | -47.66441 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad39c6a7-1252-3376-864f-ed004a3270fb | -9.78474 | -47.79858 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d6bae82c-2472-3844-826f-54e5a0eded34 | -9.78072 | -47.79535 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da0aeb92-cf9d-37cb-8105-cd194251f762 | -9.77436 | -47.86533 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6f8d83dd-896f-32bf-befa-94b1977a6754 | -9.77377 | -47.86163 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f8f7f037-adaf-30a5-88b5-a8589fbc0acd | -9.77096 | -47.8659 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2cb8af3b-09ca-3307-ba3f-934f6e9863a6 | -10.90231 | -47.7849 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c0b65d8-85cf-3bb9-b50f-05516bce1a73 | -10.89553 | -47.78603 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 97a5793c-b74c-3ceb-8405-bc921d2871aa | -10.87415 | -47.80474 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f33c8833-cce4-3498-946c-9df6f4a45793 | -10.87135 | -47.80899 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README132.md)
