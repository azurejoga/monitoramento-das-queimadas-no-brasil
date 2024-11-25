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
| 1f3d7ad2-57f2-3387-9245-6f0ce93255cf | -2.8521 | -53.975899 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b22c1691-d330-3ac9-ba18-6aec46288695 | -3.0704 | -53.2206 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a94123c-9649-32b9-b8a5-664f036e7852 | -1.778 | -52.716599 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 322f4a74-478d-39b3-a29e-8ff7e32f0f78 | -3.1856 | -49.244999 | 2024-11-25 01:01:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a94cab-653c-3b84-8504-a24c2301093a | -0.7449 | -51.948101 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5c600aa8-901f-3030-8ac2-cd7ff680fea9 | -2.7489 | -54.0205 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f378cc37-aa85-3bfc-93e0-9a66ed943d39 | -2.6253 | -53.976299 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a62e710-b3a6-3287-9e88-9939c85431ab | -2.8329 | -54.116699 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b350b17b-21dd-3c9a-a440-c294365f6cef | -4.2447 | -48.6726 | 2024-11-25 01:01:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa54e64c-cd90-3549-a8bb-c176dbbc4f7c | -1.6161 | -52.596401 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33771446-15ca-3f62-80d9-7a2c9aa11b97 | -1.2061 | -51.758301 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e75a682e-d6c9-3427-9dc5-d74a6cc6fc20 | -2.5731 | -53.973598 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d74e6b-d25e-3e3c-8800-4b28d7385177 | -2.9299 | -51.766399 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd2151e-ed4a-39d5-ad1d-3d927d23f88f | -2.8153 | -54.714401 | 2024-11-25 01:01:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7238fa4d-1325-31ce-87a0-c1247c2d923e | -2.9072 | -51.713299 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b63cf178-f519-3ec6-99f6-da3d7a30c1a0 | -4.0006 | -54.1703 | 2024-11-25 01:01:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8651faa-4edf-3953-a36d-bc16f3da66bd | -0.3743 | -51.547699 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e8e5b545-bc6d-300f-9990-2a7b5c6a0149 | -3.1758 | -49.247299 | 2024-11-25 01:01:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89aab2c9-d798-3489-b417-ae0530364674 | -3.7181 | -51.784698 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e0b0432-8154-371e-b9d5-9849400fbc4f | -3.1071 | -51.507999 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a22e487-13fc-3304-95f8-8d5e082ddd61 | -3.8237 | -52.239101 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebf0b601-cbfc-3067-a995-78daefe57e4c | -1.9932 | -53.292 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36e5d982-f887-3cdf-9cef-bfdfed552a48 | -2.5813 | -53.9645 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6e33c2d-c172-3651-a92d-1c267087e809 | -3.4231 | -53.2738 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64df9d3c-6d89-3bd1-b303-f3cf6be8b1c4 | -1.7648 | -52.703999 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf146246-91d0-385d-b6a8-137909dff273 | -3.0509 | -51.444 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f81c7815-18e7-3bbb-82f0-3719f312182b | -2.7748 | -54.043499 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e17df75-b502-336b-a910-bad31cde40e0 | -0.9793 | -51.713699 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 425dc8ac-cdd5-3af5-b7ab-6a0b2dcf0ad7 | -3.5197 | -53.782902 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dd29d28-7de5-36c9-bf67-fbb51eb105f7 | -3.0178 | -51.434502 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08f2642b-bc65-3c66-97f3-34f39d8b287c | -3.2896 | -53.0079 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88303e1-59a2-345c-8b28-85c8f8b4738d | -1.5239 | -51.617199 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57dee1a9-184b-3e94-a41d-7ff8ca27231e | -4.3259 | -45.887299 | 2024-11-25 01:01:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9125f8-9a79-3713-b944-2fb7080c04f6 | -2.5496 | -54.0508 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18e15671-bf67-33c0-86fe-c33f68744013 | -1.7371 | -52.717999 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a24165e-de87-3f4b-b1e2-33a4e388ad6c | -3.0026 | -53.7328 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a721cd6-2d2d-3b0a-9241-81d44990578e | -0.0524 | -50.821098 | 2024-11-25 01:01:00 | METOP-C | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f4a4fb6-fb55-35c2-bcbd-78ca2ecef037 | -1.3157 | -51.742199 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9cbd308-6752-3a21-bca6-9453bb7a62e4 | -3.0687 | -53.2136 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00d66da0-0cc3-3cb5-ac28-2332832d1e91 | -2.4092 | -53.8442 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e78a896c-9665-3bda-b335-1154dd6ea7e9 | -0.9676 | -51.7076 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ced38d16-237c-37a4-9671-5ca78a455404 | -0.3723 | -51.539001 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fb2eee7f-f1f9-363e-a24d-4e5f845968a1 | -3.7145 | -51.769199 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c3d4c87-229c-3350-b68c-ffb678b69f1c | 1.3764 | -55.914001 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37f2297d-9470-35cf-9a60-85d8052e25cf | -1.2351 | -51.794899 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89f0df9b-9104-3725-8a5c-7ca7b364818e | -4.0292 | -48.07 | 2024-11-25 01:01:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93bce4c7-ec8a-3b74-8a18-b8f5a05ac848 | -2.3307 | -53.861801 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d4631da-65a4-31fb-a7a0-4eb3f794a66f | -3.1657 | -51.095299 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7c64529-814e-310f-a548-53c7f9adf194 | -0.3936 | -51.4524 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fe614f84-6031-3e2c-b7d5-429caf6c35f4 | -3.3031 | -50.359501 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54769f7a-be4e-343e-acb5-722416929750 | -3.7074 | -52.405201 | 2024-11-25 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4565df44-4490-3089-92c7-7d4b0624c085 | -1.0808 | -53.3619 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9dd3565-ea3f-3222-9514-f7b7f6383041 | -3.2832 | -51.1129 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd55842-4225-3a68-b346-d49a33627139 | -1.6127 | -52.581402 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5fb1b4a-b4ae-374c-9619-4f40a381f8db | -4.0419 | -48.0802 | 2024-11-25 01:01:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d07795f-ab18-34cd-b506-98e7bffa9e8e | -4.2366 | -48.6385 | 2024-11-25 01:01:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbd7a108-ac32-3aab-bdc4-7186da0ad936 | -2.5806 | -54.051102 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70b01855-b1af-32ef-8264-b80262946af7 | -2.7384 | -54.1091 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60fbfb33-7b96-393a-91d4-c0b411045196 | -2.765 | -54.0457 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11ea394b-c4a9-3317-84d3-94712c208e49 | 1.3811 | -55.893501 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b47872c-08d5-3ce9-ad00-cbc2d175e1ce | -2.5708 | -54.053299 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57741d47-22c5-397c-ad3c-5a10d59911f2 | -2.8502 | -54.012299 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b231e3b-e3b8-3e2c-b37b-a4ed17a54810 | -2.7713 | -54.073002 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3718b900-d18d-39a1-ac5e-484eba802caa | -2.8223 | -54.0257 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec0e44c-d4a6-3592-86b6-8cf41d67825b | -0.0503 | -50.8116 | 2024-11-25 01:01:00 | METOP-C | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc3d854b-f9be-372a-b15f-0c8bc71202fd | -4.195 | -50.689301 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 210026ae-197d-3704-adc9-d73e47508c83 | -1.7175 | -52.7225 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d979aa3e-7b20-346d-95c6-94850c870cef | -0.8873 | -51.716999 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 276be85c-1108-3241-81be-2a48054d5fc5 | -1.7388 | -52.725399 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14513caa-144a-3c0d-af59-a1d6a7e65767 | -3.2826 | -53.828899 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a78a821-c893-38e5-95c0-8ca9f368a0b0 | -3.8537 | -52.146 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb630f0d-8fdc-3642-a909-ce37ed40b8c9 | -2.2522 | -53.610199 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aefa6773-343a-3077-9766-786a7e1cbccd | -0.2664 | -51.526501 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5cee966a-54d6-377a-932c-18179c1a25d0 | -2.2554 | -53.6241 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afbc9a58-e731-3d0f-b92a-367322d61f8c | -2.7583 | -54.061501 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09684c5b-d142-309b-8782-e28a458005d5 | -0.0601 | -50.809399 | 2024-11-25 01:01:00 | METOP-C | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d308493-fab7-3c29-9ca7-79d09ec1cd9a | 1.378 | -55.9072 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9d46d3-f5a8-349f-9d92-a49595663745 | -2.3143 | -53.610901 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef7deae-cbea-3eb7-abbf-cbc155425a3f | -3.2842 | -53.8358 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e05fbb2-0666-3643-b426-f4f72fb4d932 | -4.268 | -48.7267 | 2024-11-25 01:01:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 847500c8-af84-3bb1-bf47-3fa95900a211 | -3.0245 | -54.052299 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8090584-2a25-32fa-8b2c-5a83e75f19c6 | -2.6247 | -54.378101 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2555de3-63a7-3770-857f-009f243943ba | -2.8019 | -54.116402 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6587fef5-4255-3d7c-920c-82f9e17fcef1 | -2.7958 | -53.014301 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3f4f7ef-b0ca-3c7c-860c-232ace47a8df | -0.9597 | -51.718201 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d578125a-ca34-3950-b8a8-0f145d0ca795 | -0.341 | -51.536999 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 29295495-bae3-312b-85c9-d6c51def2948 | -2.8388 | -54.007599 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e3de445-6021-39e3-9a1c-481e9c061905 | -3.8187 | -51.995499 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3928709a-6e1a-3b5d-a4fc-1fabc02266a9 | -1.4938 | -52.513 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 825d2bc1-fc31-3e47-8c1e-27079f4cce78 | -1.6321 | -52.442101 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6cc151c-09a5-3ff7-bfb5-5ead094a5a7a | -1.3873 | -52.319901 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4c5366-6481-39b0-8116-a4abc6bdfaf9 | -2.7697 | -54.0662 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc361ced-cc5e-3ca0-99cc-a048451bc220 | 1.4121 | -55.893299 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4dad43-8dc0-3c08-b7ba-f67d4bb63d00 | -2.8169 | -54.091599 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 196695d1-c185-3732-b596-9c6129228c06 | -1.6127 | -52.3582 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9313d3e-d3ca-34d2-9f57-e2ece8497a20 | -2.6507 | -51.7631 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88a9add2-0396-3cb2-8e9b-0343db240e33 | -2.5692 | -54.046398 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3504a79-e060-3026-8116-8c369bc48722 | -1.7763 | -52.709202 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af9599cd-5180-34c5-89a2-852601d99af6 | -2.3241 | -53.6087 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed552630-efd7-3574-947c-886ad3360898 | -2.8568 | -53.996399 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
