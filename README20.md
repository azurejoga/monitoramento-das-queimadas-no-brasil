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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 200083e6-278b-399e-8a38-1cea425829e7 | -12.75405 | -44.48961 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 16bc996b-e630-393f-b7e2-776470a11fa0 | -9.19398 | -58.05259 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd11caba-1ac6-3bc4-959f-4a5f7b93c6ba | -7.78983 | -48.43576 | 2026-07-02 04:38:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdbcdf43-9a19-3a74-9d74-ef231f14d677 | -12.85582 | -44.34444 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e812d479-45b5-30ea-bd16-31e4c39dcc0a | -12.85431 | -44.35518 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 796c397c-877f-3725-aaa3-da36c9f5c789 | -12.87143 | -44.35027 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 3e468eea-654c-3961-b987-77f31df5b149 | -12.76202 | -44.49077 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 29f1a0e6-4e02-3cef-b647-59359c3a0dde | -12.85632 | -44.34086 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| d2bcb934-d63c-3ab2-96b8-55e0373618ae | -12.75407 | -44.4746 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 0c47db5f-1248-3163-8b47-f28020fcc60c | -12.79173 | -44.51104 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0b72e22-e9b5-3248-a307-22ff89af6534 | -8.31805 | -45.37851 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b648386f-d4dd-3046-872f-ac5cfdc6ec02 | -12.85481 | -44.3516 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2bdc625f-2124-315a-9d7b-64c4657421d8 | -12.75465 | -44.48524 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 11989600-bfcd-364f-8fc9-6f7ac474e9bf | -9.21496 | -45.32439 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d24de4f4-b9ff-30b8-b427-df91bfce1e8d | -12.86893 | -44.33887 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1fe41ba0-a1d2-3119-8689-d0be03e56200 | -11.80252 | -57.00079 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 02f327a6-8a1e-3a67-919a-c1849a5b8007 | -11.79402 | -56.9977 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 9ff4c479-2acb-38cb-9441-6e9ecb47ee40 | -9.81777 | -46.43821 | 2026-07-02 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c8b65ef-0fe1-327c-b161-7e4636854228 | -9.17464 | -58.06681 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c06cbe4-c49c-3ece-bff3-5c5f0d2569bf | -12.41828 | -58.39379 | 2026-07-02 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57ab3cb9-36a3-3f14-b4fc-4df3e87ad264 | -10.78537 | -53.54464 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 265bced7-85b5-3e75-8e08-fbc2821b8089 | -10.94488 | -43.05357 | 2026-07-02 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ab6be248-43c4-3284-a2ab-d455dc76416d | -8.79813 | -47.31253 | 2026-07-02 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 614deb60-bfc3-3911-91d9-64757f487989 | -11.91542 | -43.38958 | 2026-07-02 04:38:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afbb71ce-8ab5-3722-a990-b239e0be58bf | -9.25593 | -46.4256 | 2026-07-02 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 211971f8-dacc-3305-90f2-befe56812888 | -11.30181 | -46.42542 | 2026-07-02 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e427c15d-fdac-331c-b6ca-278285adab0f | -10.77726 | -54.10892 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c85835d3-3fe4-3cbf-b478-74071158d962 | -10.37569 | -46.68504 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5f394b83-6e7f-3bf8-81fe-13c940980b5f | -12.75066 | -44.48465 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 3e5b078e-6636-3a2e-b05d-309b713728b4 | -12.84928 | -44.36174 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 715cc712-9098-34e1-b047-ed473d57141e | -10.38593 | -49.92777 | 2026-07-02 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8866dd8a-f7b3-32f9-b2d3-53333b47019a | -12.8557 | -44.3154 | 2026-07-02 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 4f938086-06ba-3e01-bd51-1b2cbdbb7c37 | -12.8741 | -44.3593 | 2026-07-02 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| fe313c90-52fe-3d78-9f7c-fe0ed3fb8f80 | -12.8548 | -44.3625 | 2026-07-02 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 183.5 |
| c5bf5bda-63e2-3c05-981b-6704250a8ea3 | -21.7823 | -56.2976 | 2026-07-02 04:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 32032d9f-ec7a-3081-a4f3-2c21d034dd7d | -12.8746 | -44.3357 | 2026-07-02 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 293.7 |
| 9ec569d3-ec96-33a3-99c7-f8e10c570b55 | -10.9397 | -43.0593 | 2026-07-02 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| b0a395aa-35e4-3268-beb4-b8c5cc8b78f4 | -21.7827 | -56.2762 | 2026-07-02 04:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a0b0f457-62f9-317e-9992-042c996e5d57 | -12.8552 | -44.3389 | 2026-07-02 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 384.9 |
| 088cff73-eb1a-3036-9578-4bf02d7fec41 | -10.9401 | -43.0355 | 2026-07-02 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8bfacfc6-f189-32e8-b50c-5e084a9e9856 | -18.48018 | -54.1016 | 2026-07-02 04:40:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5f9b76a-2f52-30b5-b8f7-ad6820fe859d | -19.50553 | -52.73486 | 2026-07-02 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 190147ad-e799-3f07-af7a-31722cfaa905 | -19.50215 | -52.73422 | 2026-07-02 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 795aef80-ff35-331c-a73d-e834145d813e | -21.49301 | -48.53813 | 2026-07-02 04:40:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 70a33b25-256a-36e3-92e6-57ee8c94602a | -20.48566 | -50.52542 | 2026-07-02 04:40:00 | NOAA-20 | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 03bb0472-0fcf-3a97-aaf8-0c4b6a3e20d6 | -20.70355 | -50.52052 | 2026-07-02 04:40:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8922bb84-1253-3dd4-8878-2968ec7203e2 | -18.89125 | -53.02385 | 2026-07-02 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb2efd7e-1a05-3169-9945-47ab750bf824 | -17.71657 | -46.79518 | 2026-07-02 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bc40fb5-abde-36dd-9126-5974440d3ed1 | -15.33849 | -52.78127 | 2026-07-02 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ada57c9-1198-3e8e-a1e6-d3c96cb559ed | -14.81473 | -49.00922 | 2026-07-02 04:40:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27b204f8-12ce-38b6-b8b9-e00b2d4f0ac5 | -14.17624 | -52.86561 | 2026-07-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bb5e9c1-4ce6-3ec1-b2f5-9a87b2be3056 | -19.50004 | -52.7259 | 2026-07-02 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bad6ed02-7e4a-33d7-b9cc-10fdebe4bd92 | -17.71555 | -46.78772 | 2026-07-02 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9930984-caaf-3d05-af5b-3eba8c1ef7fb | -20.70298 | -50.52425 | 2026-07-02 04:40:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bd720077-c3e7-3555-a5bc-d2e62e691d87 | -18.41068 | -53.28739 | 2026-07-02 04:40:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f781ec3-9685-3d54-8705-c60cf12f4b2c | -19.50343 | -52.72655 | 2026-07-02 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0516ab0-1980-3ff6-a352-5d35d7b99ba0 | -20.47568 | -50.52369 | 2026-07-02 04:40:00 | NOAA-20 | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ac6e8392-d29b-35a0-8a45-e012bd83191d | -18.12809 | -43.97319 | 2026-07-02 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f198b8fa-379d-3c2f-970e-a03cd102106c | -14.15697 | -52.88079 | 2026-07-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8067dad-0fc3-3a4e-b24d-da8c9b630b6e | -19.50828 | -52.73935 | 2026-07-02 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48263477-22a2-3a22-b921-5dedde763b5e | -18.64032 | -51.83258 | 2026-07-02 04:40:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e0a034f-c9ce-3ea6-82c7-68c6288d7ee6 | -17.25401 | -48.28312 | 2026-07-02 04:40:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a85fb1a0-1ab2-3354-a073-1ff4d0932ce3 | -18.13254 | -43.97373 | 2026-07-02 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0305f93b-3cb6-3f10-a126-300ea9aa306d | -15.7505 | -48.28086 | 2026-07-02 04:40:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be4ded04-df55-3039-9922-48ed60c9b977 | -19.4994 | -52.72974 | 2026-07-02 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae3dcb98-7e80-37df-8aaf-6bc2524a0723 | -16.70348 | -48.71766 | 2026-07-02 04:40:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3840031-6fd9-3c96-a05c-7edeb0dd9ae3 | -14.15409 | -52.87596 | 2026-07-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fe8ec01f-5610-3e92-b1e5-00cee4f81ec4 | -17.71491 | -46.79226 | 2026-07-02 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8e20c46-9cb8-3585-8e76-5ea9ceac64c4 | -18.66918 | -48.21139 | 2026-07-02 04:40:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad819bce-07ac-3a5d-8291-3103de97902d | -16.45023 | -44.76676 | 2026-07-02 04:40:00 | NOAA-20 | CAMPO AZUL | MINAS GERAIS | Brasil | 3111150 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42caf425-9ef9-39bc-a63f-38bee5cdcf06 | -16.39511 | -47.41758 | 2026-07-02 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5929fbe-092f-3c3c-a250-e7ae1211a929 | -15.34201 | -52.78188 | 2026-07-02 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 858813e6-0188-307e-8bad-1b931b5b11da | -19.50278 | -52.73039 | 2026-07-02 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d72af9d7-f978-31e7-bbd2-da685d083020 | -19.17471 | -47.35394 | 2026-07-02 04:40:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6d7817bc-d199-3545-b22b-64c0ae03ec68 | -17.69072 | -48.63968 | 2026-07-02 04:40:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e914f134-8e9d-3d33-96da-922122b4bd08 | -20.61392 | -51.11934 | 2026-07-02 04:40:00 | NOAA-20 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a3635e1b-3d94-34f7-89fa-5026779c844f | -16.67705 | -49.21183 | 2026-07-02 04:40:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59ae4b85-230b-3c11-9093-b33de6fb4f98 | -20.47901 | -50.52426 | 2026-07-02 04:40:00 | NOAA-20 | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 58dfd95d-3745-38f9-849e-0bac74e34c04 | -19.50617 | -52.73103 | 2026-07-02 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e45521f-2d6d-3222-a134-bf1fd6cd8d91 | -21.4523 | -51.35995 | 2026-07-02 04:40:00 | NOAA-20 | IRAPURU | SÃO PAULO | Brasil | 3521606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b2bea2db-b260-3bd1-bda0-7cc4eb6d70fd | -19.8441 | -49.06717 | 2026-07-02 04:40:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a65dfc45-3396-34a0-a138-1351dbcf4d6e | -14.17403 | -52.87837 | 2026-07-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b29716b-483d-39b5-89e8-df21c99e4ce6 | -20.08016 | -44.78369 | 2026-07-02 04:40:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e995aea9-7f9d-31f4-9f27-4802d58f607b | -17.7178 | -46.78606 | 2026-07-02 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b387a001-5b0e-3809-b2c4-9b16c6f86879 | -19.81985 | -54.64785 | 2026-07-02 04:40:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93e9a805-11e5-36d5-b083-02c2e9b7348a | -20.97455 | -49.09747 | 2026-07-02 04:40:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5d862de2-ee5e-33d1-a4fc-b948715fe375 | -18.41346 | -53.29213 | 2026-07-02 04:40:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e984e991-c1f0-3515-bf56-efc70e135da0 | -14.67667 | -52.40045 | 2026-07-02 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d90732c-f8fc-37cc-9139-3daeb19fa779 | -21.45172 | -51.36366 | 2026-07-02 04:40:00 | NOAA-20 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1059e688-8724-36c5-96e2-1c66de9374de | -17.54349 | -49.42648 | 2026-07-02 04:40:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a7ea84d-3776-3e0c-9bfb-9f8a14ba85ea | -19.17103 | -47.35344 | 2026-07-02 04:40:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6a682c4-80ec-335a-b9dd-4e7604aa5716 | -17.71719 | -46.79063 | 2026-07-02 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3a296b0-8e93-3fad-b32d-edbcc67af362 | -20.70688 | -50.52109 | 2026-07-02 04:40:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d5fb7288-b108-3738-9817-1dfe8b984548 | -18.93197 | -51.39743 | 2026-07-02 04:40:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6857157d-9e62-3a92-917c-34f1b83699ba | -14.16055 | -52.88144 | 2026-07-02 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71042751-270c-3e43-8ca4-23c99bef3774 | -21.80087 | -52.72129 | 2026-07-02 04:42:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0464397a-d687-3f0f-b8ca-d6ddb5368b79 | -23.43747 | -51.42804 | 2026-07-02 04:42:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d2bb8171-0315-3b59-a768-0d9948d12d25 | -21.77677 | -56.29247 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a04d567a-4171-3033-8e47-963e5ea5884b | -21.77579 | -56.29767 | 2026-07-02 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88032506-807b-31da-ba7c-85a8a5a097b8 | -21.80297 | -52.72947 | 2026-07-02 04:42:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)
