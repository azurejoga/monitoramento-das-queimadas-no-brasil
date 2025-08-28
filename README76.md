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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc226bb3-33dd-35cf-b058-1ec2fbf863e0 | -9.17734 | -59.45037 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bf0f181-53b0-3392-b28b-8d1304fa3a3c | -10.83615 | -60.81252 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4fbca7a-a76d-3cf3-b467-8973ecb802ce | -9.46726 | -60.30672 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 044895ca-f2f9-3859-815b-7fb7ac1b366d | -8.94814 | -65.95333 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60369f3b-9c00-3e67-8686-75476589956e | -8.3477 | -62.9319 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e7ffc27-abfc-357d-add5-6e29cdf26168 | -9.00816 | -65.72374 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0559f0a3-6cc6-31e2-ad56-f2d66e36ab20 | -9.10337 | -60.31901 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44d9229f-ffde-3aa9-8bec-77dfdcda7f9e | -6.9039 | -62.93558 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46371610-f26c-35ed-86fc-019e1b282f26 | -8.8764 | -60.75759 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 769a0a32-6a7f-3d1b-9e9a-4c944b8b90ab | -12.78713 | -48.17451 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da1f1f36-9cef-3ec5-bd8e-af36af126e26 | -6.91726 | -62.94176 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70169627-e7ae-39c8-a61c-32d6891c7d97 | -7.54389 | -63.84323 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af6ed1f7-0c15-3671-85e1-8cb57177ef22 | -8.92351 | -65.92429 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de01488f-c7dc-3bec-acd1-0892904aecce | -9.17913 | -60.80933 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e71d310-d19a-3f0a-9b18-94ed378699a2 | -5.91588 | -61.30763 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 890794e9-2fb3-3d18-a34d-52b59eb47c67 | -8.25336 | -61.46749 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2618f8f6-65f4-3860-8567-c1385b32858e | -9.1294 | -65.76794 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 547e8c3a-ef4e-373f-a346-50f5d0d7d670 | -9.66694 | -48.31118 | 2025-08-28 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16e884f9-f8a5-35f9-bf19-0ab4af64253b | -9.40932 | -60.56886 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 178a4836-1c12-3e3b-b086-c0a97662da68 | -10.98469 | -62.54293 | 2025-08-28 05:25:00 | NPP-375D | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b8cf78a-3b54-3a8f-8fa1-12db9e745a83 | -12.68277 | -48.17935 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6232c07e-ee42-34f0-bafa-0ec9a93c55fb | -8.90911 | -62.48095 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 603a8682-c488-3ec1-91ca-c5ba96b98258 | -7.47277 | -61.39652 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3167a1d-d712-3112-a219-4e55b40aac5a | -9.02125 | -65.69469 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1617ebf-376b-3549-89b6-c56abbccf255 | -10.7872 | -60.79743 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ece8bf5-06e2-37d0-aad6-d5a764e96ea0 | -8.95955 | -65.95897 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36f7191e-9aff-3819-97ab-883ae0bbc85a | -10.32255 | -62.62028 | 2025-08-28 05:25:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f48f635e-60d2-31ef-8a6b-ee8516bdb28a | -6.23675 | -60.0091 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2a7744d-817a-3bc0-9ac7-92509c3e1fa6 | -8.34181 | -62.94649 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dee797b6-c0a9-3b19-8294-c40ddbeee517 | -9.48044 | -62.38347 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ecc5199-fb97-3675-beb2-2e20481b2ac2 | -9.07105 | -66.0616 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39c0d192-0f06-30d9-8dcc-f0a42650c6ed | -8.88199 | -62.47651 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44053f29-342b-351a-ad52-5a1d33b29adf | -7.41245 | -60.62542 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b3cec6a-d785-35c5-a471-eb53810aacde | -7.54026 | -63.84263 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 689f84d6-a4a4-33d6-8b02-d37eca3d05fb | -8.95494 | -65.96178 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b65152f-817f-365f-8680-45f4e732d322 | -10.80162 | -60.77071 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 83df26ee-2f1c-3802-a8e7-3d9572adc253 | -8.95154 | -65.95755 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cd5b1b3-e9eb-369e-8546-e743d1d3d8e0 | -8.60709 | -64.07488 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18ae47e4-b268-31e6-9336-7ee97673c26d | -8.94631 | -65.96389 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 194286e9-570e-3f8c-94a5-b1972ddbacc3 | -9.26015 | -65.89854 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ea49803-0489-3461-b0cf-607a9f5a5468 | -9.12594 | -65.78827 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4f1601e5-c261-34d0-bb5b-a2c35f58d2bf | -9.12766 | -65.77817 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a98fc42c-4be6-3462-8273-af2deab8d303 | -8.57135 | -63.92957 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cc82f23-2179-3885-91a7-fa5ff8b5335b | -9.41544 | -60.57343 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e24739ce-a460-3a5d-ae71-4bb386b98dc4 | -9.40814 | -60.5326 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5b6b294-15ab-3190-8b69-190e7e11d085 | -9.139 | -65.28089 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11bad871-30d3-3ed2-8545-76784ce15aa6 | -9.54142 | -62.39663 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14b3501b-b401-3748-b263-28a7f06ec213 | -9.41481 | -60.53366 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 483b4894-a7ea-30ff-b462-9b1719d6d997 | -8.98655 | -61.7009 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b80fe715-b60f-3efb-8b9d-a5563f866f65 | -8.87749 | -60.7506 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a184774b-a238-375a-981f-f529d801ad9f | -9.40481 | -60.53207 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d48c4ed2-e912-318c-98ee-c80d2534c669 | -9.16709 | -65.79795 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67973e96-aa56-3bdc-a79f-19840c7e1b54 | -9.23347 | -60.9147 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 640d1fcf-5b9b-3681-91ab-1dc78ada628b | -9.63834 | -59.62988 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18ff99ee-d634-39f8-9f7d-b62d480cbbd7 | -12.78067 | -48.16796 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84db61b3-756d-3828-993a-a947ffc705a2 | -9.17397 | -59.49499 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5c1d92e-323f-30d5-b2d7-ff680c208a9c | -8.92751 | -65.92498 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 412c7ab6-1103-32d4-92c8-50ef29c5f6cb | -7.54116 | -63.86 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05bae2c5-8133-33f9-8ac7-9abacdaea2ec | -9.39147 | -62.49916 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e55c932-192a-3bd8-b2d4-852c159a6cdd | -8.34709 | -62.9357 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8143952-c5ee-34a2-b4f5-3a1a83b436e1 | -8.89275 | -62.47453 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0f3ae81-19da-3b4f-8480-c7d0263c7aab | -9.05289 | -54.94377 | 2025-08-28 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 94fbb375-65f9-3e4e-b83d-bef684d32bca | -7.44514 | -63.1605 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9ebadc1-41b1-37b3-a302-14713ec26f20 | -11.36193 | -63.27575 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d44d45c6-fbcf-3285-9e77-53784885b38d | -9.41701 | -60.51957 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 246c0bcc-e2fe-3c4b-97d0-3ba1b93f71af | -10.7955 | -60.7661 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9b4cdf9-e8c3-39e9-b2d1-7a00b4e5e674 | -8.94753 | -65.95685 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 983d10a2-42d7-393a-9ab9-208b7fac0e0d | -8.34486 | -62.92754 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 944a27c3-6780-3b08-a203-124b7fe79fd2 | -7.66196 | -62.54513 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ffc805c-5633-35cd-9f42-a42ecf649180 | -10.56479 | -69.81071 | 2025-08-28 05:25:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 504c3566-4e1c-365a-84ab-0d1b90b24fd4 | -10.06539 | -58.36329 | 2025-08-28 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2634599b-ed63-3c62-84c6-36283bf6df46 | -8.34952 | -62.93144 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96377f5e-61f1-33a5-ab16-d94dda2c0cb2 | -13.00408 | -56.90797 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd9ad130-5d52-3be4-b13f-9634bd0c5321 | -8.92292 | -65.9278 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b66ca949-bdf9-3b49-9d00-30ed7ca182b7 | -9.08638 | -65.73431 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b8a0e48b-5272-3780-9476-f8bea3e0d36d | -11.22459 | -55.06599 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97202e13-0344-39da-9d44-a1e93afdb4ee | -10.24963 | -59.66613 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eec481e-d724-3751-ada3-9003995d7340 | -9.59711 | -55.38322 | 2025-08-28 05:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f62d7f00-e3ac-3a99-a0ce-460cce6765c7 | -7.5518 | -63.84026 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25cbf4a5-24f3-3cd8-bbd5-2eab47d7421e | -7.37397 | -64.3696 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bd3965e8-a9bc-302f-b866-d95a53c2e5e5 | -9.40371 | -60.53912 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 237fc57d-a00a-3419-a1c1-35db0e22b402 | -8.95032 | -65.96458 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 163beba1-ff45-39c4-b624-0ff87f212cdc | -9.16313 | -65.79726 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52ac093a-fad1-3c1b-b38d-7ab3628893da | -9.12073 | -60.7322 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cd8ae85-1985-34ee-8cef-7bf7d1fdb52c | -13.00811 | -56.90858 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0676abe2-5344-35d4-88ec-6fe3e2dd4f79 | -8.10485 | -71.25148 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e450869f-5c71-3472-b1c9-da0a920b854f | -8.8753 | -60.76458 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b720e399-8d82-31c0-af85-623218733f78 | -9.19778 | -59.5437 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b8cbcf9-d1ff-327e-b7a7-0990f3bfeb8f | -9.79303 | -64.2433 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc4b330d-7155-3164-9e6b-e9000b3d16a1 | -10.79384 | -60.77673 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b8907572-ff30-3135-a3a8-fb120680b071 | -8.10656 | -71.24207 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30fa03fe-9835-34b4-9a75-739c9e9bbac7 | -6.92551 | -62.93513 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9db409e9-2de6-3dc6-a016-d227eef487b4 | -10.81942 | -60.76627 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c843e99-1b80-3a8b-8f10-c90b6511af1e | -9.19626 | -59.64835 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6acc092b-0bdd-36bf-9634-08c3bbb0f65a | -8.06444 | -61.54559 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19369990-058d-3566-9ab9-27d99aa87e9d | -8.96197 | -65.94494 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bc0baec-4d40-30ec-a2c5-7937c860934c | -11.22581 | -55.05713 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 265b2aa7-3864-36b5-af5f-bb9f4e6d1e14 | -8.92917 | -65.9397 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a2cc7ed-a419-347b-b7d1-0dfe77787891 | -8.5143 | -69.79861 | 2025-08-28 05:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4a07ac7-d2ad-3993-a4a0-f1e3f641c288 | -9.16775 | -59.5128 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README77.md)
