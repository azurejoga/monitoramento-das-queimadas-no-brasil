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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c502ee9a-dab0-32b7-9ae8-80b8b22f6708 | -8.90443 | -49.67154 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fe5949a-117c-3f1b-ac53-e6bbcfdef3e1 | -8.89115 | -49.64804 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98e21a4f-ea52-3171-9ba9-cff4d67ddfbe | -8.88893 | -49.64056 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7413b453-8c4f-3243-a1e9-0495c4c6b9f5 | -8.88839 | -49.64405 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89c2157a-1495-35c3-a79b-0efa3c44e509 | -8.88784 | -49.64752 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e53792a-7313-38dc-b6e1-cf1f244610b9 | -8.88354 | -49.69675 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1872f5a1-a7bb-3a81-93c0-f2de46a38194 | -8.87969 | -49.69971 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 152b22f4-0f35-39d3-be51-a6b8a5d0a961 | -8.87797 | -49.66735 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 297704dc-59c6-31ac-a83f-b9a3e8dc9000 | -8.87515 | -49.64195 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4d277d9-0f34-350b-ad21-d0d98c43c3a0 | -8.85845 | -49.66034 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7591f020-0f17-3432-8188-fe3f12cb7b32 | -8.66258 | -49.50127 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8d57b0c-1e6b-38af-862a-9c28ecbaaca7 | -8.65927 | -49.50074 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfddeccf-7edb-3d11-8cc7-7ca1136d614d | -8.6533 | -49.10224 | 2024-10-05 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6e6a535-e74f-3f72-a572-747d8e1ed205 | -8.65276 | -49.10575 | 2024-10-05 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bec25684-b02c-3e79-9f31-1c646afa0c1b | -8.54039 | -49.65305 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39a1de82-58fd-3eed-a55b-89cd483b7fd5 | -8.47819 | -49.02797 | 2024-10-05 04:38:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e52778c-f936-3b0b-a522-a0ab802848df | -8.47541 | -49.02394 | 2024-10-05 04:38:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da0ea231-91c5-3e01-ba54-43c8accfdedb | -8.47486 | -49.02745 | 2024-10-05 04:38:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3533e43-fff6-386f-90a8-d62524237881 | -8.32433 | -49.55815 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16154b26-f1cb-32c7-867b-884d5000835e | -8.79892 | -49.975 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61e84ff6-d84d-38ee-9840-b3d5d82a2350 | -8.79561 | -49.97448 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ece87ebf-74bb-330a-8cf5-5ad6ab2c1d56 | -8.79558 | -49.95311 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9f17dc08-5a78-3b15-969b-bbee04ddd202 | -8.79503 | -49.95658 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 62077944-3101-3782-b6c6-01140eec6780 | -8.78845 | -49.9769 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ad81da6-51e0-381b-8d9e-d76c5bc37c95 | -8.78678 | -49.96595 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3fdb19c-709c-3f72-b81b-2beafc8c067e | -8.78514 | -49.97638 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26675dee-9428-3471-b820-4ca8064c85c3 | -8.78348 | -49.96543 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09d55c49-90bf-33b1-b875-7a108ead4642 | -8.78293 | -49.9689 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e4b7058-1e82-3562-b4df-4ac2fea15378 | -8.7829 | -49.94753 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7efb8109-d09a-39f4-a69c-7aada2e6c216 | -8.78126 | -49.95795 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c51bb31-42ce-3848-b328-60494d185f7d | -8.78014 | -49.94353 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03586ddc-24a6-381a-9693-e28d29953f71 | -8.77959 | -49.94701 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b866dcf-7f1d-3677-b5f6-68b989ac560b | -8.77905 | -49.95048 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2d1cabf-e8c0-3f03-9683-561683e28cff | -8.7785 | -49.95395 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33e29306-99d5-3613-831d-51678f7d7219 | -8.77796 | -49.95743 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d14c9a8c-436a-3a35-96b7-0902ed1de883 | -8.77741 | -49.9609 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee65b137-830f-35d9-87fd-88796e6510b0 | -8.77686 | -49.96437 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a77ab936-994f-3d67-8afb-581a955538be | -8.77629 | -49.94648 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0e718dc-7d5e-3294-ba92-734cb3e0741d | -8.77574 | -49.94995 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 030f9337-6289-3c57-a37d-39150d3d03ed | -8.77407 | -49.93901 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 685e6491-e84f-3451-8786-000224db588c | -8.77298 | -49.94596 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0fc97d9-30eb-3afa-ab7e-e5731d634d48 | -8.77134 | -49.95638 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e386c2f-cd44-3906-8521-a8e234a79f78 | -8.77079 | -49.95985 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1620b35b-e395-39f6-a7eb-7fac483ce3d8 | -8.76967 | -49.94543 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d673ab9-b4f8-3542-94b6-233ffb29626c | -8.76803 | -49.95585 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37bc4f1b-a083-32e0-81de-6e2959b4d4d1 | -8.63245 | -50.04105 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c14d59ae-5a93-3f9c-a62d-c8c0668ade71 | -8.32918 | -50.06746 | 2024-10-05 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a88ec3c1-337c-3f6c-8fed-7b221395fd28 | -10.32669 | -50.54153 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aad4280-540f-3499-a0da-7e3f36e3f2c3 | -10.32614 | -50.54502 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12a726d6-f31a-3b87-be90-45ddd01bde40 | -10.32559 | -50.52702 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4daef732-0988-315a-a05a-eb3ef9f54c00 | -10.32558 | -50.54852 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9032f189-c091-329e-b910-b21ff7f48b9b | -10.32504 | -50.53051 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 899bf96b-143d-3b5f-984d-177904143669 | -10.32448 | -50.53401 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0358a1e-79ed-3946-a622-e62661a9b36f | -10.32338 | -50.5195 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5e8f923-0be4-3443-b725-5e3a57603b6c | -10.32283 | -50.52299 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38bf665c-8093-34fb-8430-68e52086c625 | -10.32228 | -50.52648 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40db774e-cf04-34fe-8699-043785436fd8 | -10.32173 | -50.52998 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78b0229d-2fb5-3a8b-b66a-4e70e5a9ffc6 | -10.32173 | -50.50848 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1037165-632d-3d2f-a280-4e0448d5d10a | -10.32118 | -50.51197 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e54e854-f9f9-323d-aca8-66237d3bfc30 | -10.32007 | -50.51896 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dec4c601-1b5f-3abc-9e88-e133b18ab915 | -10.31897 | -50.50446 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2ab3666d-caa1-39d5-82aa-4cc363990638 | -10.31842 | -50.50795 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 111be1de-a670-31b9-aa41-9b3d14653e62 | -10.31787 | -50.51144 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4524e2f-4649-39d2-bab5-e10ac7b99b18 | -10.31566 | -50.50392 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b0f2d931-5d2f-35d4-ab36-8fec0e6e5290 | -10.31511 | -50.50742 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 87fac3d1-4c62-3826-8790-43a3b6691604 | -10.31456 | -50.51091 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 368d8cad-c0b6-3926-970e-f354b5913d0f | -10.31345 | -50.51789 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bfeed5e-131b-3034-a874-7a95c99f0be2 | -10.3129 | -50.56441 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7a9a71b-c81f-312b-ba9c-6d7bb6b1317f | -10.31235 | -50.52488 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b33b1841-81c3-349e-bee3-d95dd48cbbf1 | -10.3118 | -50.50688 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 138d38cf-f4ba-39f7-9134-08096378b154 | -10.31125 | -50.51037 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0e04c370-4fd4-3e47-8a65-a9956973fe4e | -10.3107 | -50.51387 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b5ee7c7-5e30-3e96-b0fc-da9e255c41df | -10.31015 | -50.51736 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c06613c-2f18-3192-9920-eefa329fc578 | -10.30794 | -50.50984 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| abb2bd90-bfcc-3c26-8e62-d10468dd1f14 | -10.30684 | -50.51683 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fdfa894-a59d-345a-9139-7b53f304b37d | -10.30077 | -50.51227 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30a02b7d-4d5b-3d82-a0c4-565f7a2518a5 | -10.30022 | -50.51577 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e9705e1-b290-36eb-9ef0-ad7fdf0f0d46 | -10.29967 | -50.51926 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0817b84-58fb-3df8-b505-7f3cd5b97007 | -10.29912 | -50.52275 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7d55ffc7-032c-3bb7-8c90-d92393b5c8bc | -10.29856 | -50.52625 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4ec42758-33fd-35ed-afc4-e5dbb42e79ba | -10.29801 | -50.52974 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41ac2004-7fdc-3306-8ae0-3642f431707c | -10.29746 | -50.53324 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06482c76-8f6c-39f8-8893-2df90dcdbd11 | -9.99047 | -49.47744 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9c9509c-30b5-3096-be6c-4fd2de68fd23 | -9.98715 | -49.47691 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 024171bf-25d0-3ea3-aea4-ad6f1ea14b2a | -9.9846 | -49.47264 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a88b8ebe-7df9-37b5-83c2-013e94a68c68 | -9.87907 | -50.14755 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6848b3ba-366e-305c-bd02-b06b6030e8b0 | -9.79247 | -50.07299 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ae297b6-0401-3cf3-aaa7-32ec0119982d | -9.78971 | -50.06897 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5e1ba8ac-d8c7-31bc-856e-182b1b8d7815 | -9.77309 | -50.08774 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 119d1782-2a3b-3f82-bd50-b4a4727f1d23 | -9.761 | -50.12152 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd81f7ce-797c-3088-b0c3-4cd9d7e706e6 | -9.76046 | -50.12501 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0458e957-053a-3fab-ac25-40229eca296b | -9.7329 | -50.12775 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9148b896-7a09-3c3f-829e-a8060bb4a557 | -9.72353 | -50.12269 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 795fbc1f-8b3e-3258-a6e5-c3c6752377b2 | -9.72022 | -50.12216 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0933c6c-bc6d-3ee2-a2d7-f6ccae4f803b | -9.6009 | -50.16764 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1993ea3-a061-34ea-afc3-90297809e40f | -9.59759 | -50.16711 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7f00e72-87fb-397b-9718-3d2e46ad451f | -9.59255 | -50.09135 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7ab015b-2a16-308e-83f2-46fdf2f9fa62 | -9.592 | -50.09483 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a508d43e-f6f4-33ba-b408-0f9adadff080 | -9.58924 | -50.09083 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b51a074-f2c3-3103-8bb3-d003d244d3f5 | -9.58603 | -50.17597 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README103.md)
