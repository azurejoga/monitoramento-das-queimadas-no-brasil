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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a747915-de64-3623-bf29-c5115aa516e2 | -8.35055 | -62.83814 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 201bd5a7-6b8c-3356-934a-1de986cddffa | -10.65657 | -63.5216 | 2026-10-04 05:18:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a66974c-0124-3bc1-9a5a-a945205b566a | -9.92118 | -65.03935 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46cc5178-1a65-38a8-83d3-50cb277fbfbf | -8.89415 | -66.73123 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcf92f3c-04a4-31f9-8240-5cb0917f40de | -6.07455 | -57.80875 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d9a5475-32eb-3107-9cb0-375baaaf4426 | -5.99263 | -55.68614 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4137d812-c287-3454-ad31-2d66c59af476 | -10.22209 | -59.0955 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a4edb0f-da4f-3e8b-9181-70b993161852 | -8.6083 | -66.96961 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bc9b6fe-ee47-30a4-bec8-b0634789f5e9 | -9.16546 | -61.40776 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f654e019-b441-3f8f-abff-310441b9f36e | -9.54496 | -64.81702 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 397882d0-3a40-3d6f-8e31-b3df3d052647 | -9.15512 | -65.3987 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e648d2-46b5-339d-b699-90a09ef9fed2 | -9.92724 | -65.0312 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88e74fbf-d7a5-3970-b915-113d94684811 | -9.12725 | -65.94917 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0307c4ae-fa23-3d91-a309-4f47b19ceb00 | -8.51124 | -67.11465 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40e81c9c-74f7-38fb-b17d-e86be9980a34 | -9.91387 | -65.0287 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b828432-0697-3403-9932-316080506ccf | -9.25123 | -60.333 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f41df95a-f4ff-33b3-8643-6f0f8940398b | -9.54321 | -68.5266 | 2026-10-04 05:18:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8405517-f10b-3c69-b511-fc4af419d83e | -6.44541 | -55.45381 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a342c890-9617-32e9-9449-937278d65f06 | -9.92037 | -65.04388 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2caf1e4-9b62-3154-ad23-14fe877dc7a3 | -6.07786 | -57.80928 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f6c98e0-8ac6-3bb4-8775-44526e17ac78 | -5.79137 | -57.81656 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11b73b6a-394b-3686-a93b-83446f169d41 | -10.22265 | -59.09198 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd1d02fe-0136-3431-83e4-5ff2b46ec742 | -8.89659 | -67.45451 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d61b8d3-0789-3876-ba42-f9b3608f0c76 | -9.13379 | -68.25247 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 860d15c2-6743-3e04-9456-25191fc95a3e | -6.19139 | -55.35012 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bde408b4-09e5-3535-b364-760b9d4b6380 | -6.12109 | -57.70961 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54abc79a-9eba-3eca-90fe-58e0cfd4daba | -8.51792 | -67.11246 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d655a691-f32e-3e4b-a512-2012919de4c5 | -9.90656 | -65.01807 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21ab4508-2911-37f5-9e47-28d76f227693 | -8.88195 | -66.76969 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db72c277-e96b-3913-94a3-069c8e274118 | -8.89723 | -67.45112 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 478d8ef1-f3db-3a0b-b87c-4794ebe662e6 | -9.88005 | -65.13948 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 21c2fa41-2dbf-3f53-a1ae-8e81365513f8 | -9.91467 | -65.02421 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24e93200-ccfa-31a2-b37a-76bbdc5776ed | -9.3639 | -60.30827 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16a979d1-1d4b-32d2-982b-a05d5c07866c | -9.91225 | -65.03771 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8207a2a-6e88-3b54-a6e2-1edd026d0679 | -8.66768 | -67.11846 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5cf1342-ed5b-3557-a1e5-65a4fc35371a | -9.07955 | -61.15924 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 975a9ae1-8b9e-37ba-a489-03dd9e67b945 | -9.1364 | -67.93263 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41e174c7-1f8d-33fa-9bb2-8c328878e1cd | -8.70922 | -61.40147 | 2026-10-04 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 12d2d197-8149-367d-ade7-fec33424033b | -8.59283 | -66.82016 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab9530dc-b8d1-3792-951e-c08981eea083 | -6.02153 | -57.69407 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2fb6420-4028-31bd-a4bb-aa6a0932d7be | -8.55822 | -67.06633 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e920aff-5c5a-30f2-b9fb-8779539b1882 | -8.71285 | -61.4021 | 2026-10-04 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 649cd3b1-9413-39ed-8f85-65b41a8a2a3d | -10.99193 | -59.1457 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee96bf56-1066-3b26-92c5-04fdcff263bd | -9.15664 | -68.27164 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f05d428-2726-30d2-9b50-fbbf5cdc8c41 | -9.10321 | -49.78463 | 2026-10-04 05:18:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b446cb7-26d6-3f4d-b34c-dd8f5ee2f3ec | -10.99362 | -59.13515 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1cbac93-fad4-3b30-b431-98c3331bdaa6 | -9.88872 | -65.0148 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4a0b07b-a5b8-3965-9a28-3615c944c2f9 | -9.40126 | -65.90225 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08676a0b-9e01-32c7-8507-fa7e89c81802 | -10.80435 | -55.58416 | 2026-10-04 05:18:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1d7ea2a-51da-3bf1-a0d5-af0bd046a5a5 | -8.88853 | -66.73317 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f90ebece-f825-3c56-8ac4-7b9aa40d2148 | -8.51588 | -67.11893 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d034164a-41cc-39a9-a330-e78c2547d3b9 | -9.28329 | -65.49235 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06edc8f8-d215-337c-8118-486ec09c0f0f | -8.88656 | -66.89186 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d725e771-f2f8-3f46-a5ae-1153137d3739 | -8.56488 | -67.00087 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b9a251-51f6-356c-a497-36abfacae571 | -8.51266 | -67.11146 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaadc64b-f33b-329f-bcde-65cdb6dde4b8 | -9.47624 | -64.69359 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8160255c-977e-3a89-a0c6-fc6a3e1a4023 | -9.54574 | -64.8126 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdc9fe84-e405-3ab2-aa18-1798e86093fe | -9.7005 | -57.45396 | 2026-10-04 05:18:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d412a96-10c6-352b-8f09-21b0acadf179 | -8.89917 | -67.45515 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f86bce3-7cf5-369a-ade2-18cc0f249947 | -9.62193 | -64.17826 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23c7b6b4-68a4-369c-b049-d264f4c95013 | -9.60717 | -64.04104 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02ce42ce-9bb5-3c0f-8ee4-4be11e217656 | -9.12823 | -65.47004 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e3a8ba7-1b11-3c49-95ea-edac5f752a76 | -8.34439 | -62.82646 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33b6ebe9-2768-3ad1-8601-3975f3307629 | -8.57549 | -66.81963 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6901b3ef-c578-39d9-b9d4-2ca20b70a268 | -10.99087 | -59.13109 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d5199cd-4c08-3e6f-b1cc-8a8790ca8a09 | -8.34659 | -62.83745 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bcb5b38c-0f25-394e-8bab-837d93023d30 | -6.446 | -55.45003 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25445ce8-3951-317f-b2ef-e540e5f12a2d | -8.56346 | -67.06731 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 206d7ef9-7eab-3863-8b4c-c864829f65a7 | -6.50339 | -58.53151 | 2026-10-04 05:18:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d91bfd39-7e88-3db7-b71e-ced24d094531 | -8.51649 | -67.11565 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b47dafd0-fd9c-3d1d-afbd-51fbc0807e55 | -6.05406 | -57.70276 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95fbf307-564b-3e18-9483-8756eb68409c | -8.71064 | -61.39296 | 2026-10-04 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 07b46131-0d5a-370a-a015-50ddfc6607ac | -9.13289 | -65.4709 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 974bf7b0-78bf-3c91-9660-d2f35c045851 | -6.33345 | -55.31713 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 940392f9-13d7-3f1d-9719-b71ec0587d6e | -9.15048 | -65.39785 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a167b6e-f2b9-3b65-aad0-15b8c9cb89ee | -10.98918 | -59.14163 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fea4b944-1488-384e-8e38-c9a2dd7251a5 | -8.65858 | -66.93433 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8795e0d-0097-35a8-ae95-68dd21457357 | -8.35143 | -62.83299 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a6c4e4a-7c21-31af-bfdc-2632ae443806 | -8.50933 | -62.6379 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5118948-1c47-398c-881e-b7f88b875d33 | -10.83215 | -57.20563 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c3d7ec0-2513-365f-8e2f-c70e2161ba9a | -8.58827 | -66.81599 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c82473b-487e-36a6-aba4-47ab3d3fed3c | -5.89295 | -57.67008 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f31e0e4e-f3df-383b-b4bc-80dcd7ec5680 | -9.10217 | -49.78232 | 2026-10-04 05:18:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d6a4f1a-9a71-3221-a685-be73fb40c367 | -9.78801 | -60.13806 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b1766e4-bbea-3c64-9c35-912e6cd4bf60 | -10.9925 | -59.14219 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8731502a-2e56-3b1c-8468-648c3f5cb564 | -9.01928 | -65.69966 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46c0a966-e437-3d8c-b596-a5c1502daa96 | -8.57682 | -66.82027 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d8b663d-c135-3a15-9990-3f291b9cb16b | -9.09027 | -61.16107 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c76f78b1-e763-3f68-ae56-51007e1af8e9 | -8.57624 | -66.82343 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 43cc9581-2c25-391b-8784-e93ce8fecc95 | -8.35452 | -62.83883 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecdc77f1-d169-3882-a282-707c89848f4e | -6.16376 | -55.36907 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f22ac6c6-aec6-3bfb-a920-68761804ee2e | -9.01072 | -65.69286 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e9f949b-c78c-365b-8e58-6547ba58f987 | -9.64994 | -61.93697 | 2026-10-04 05:18:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ef54370-b77c-339e-988b-559e41313763 | -8.34571 | -62.84261 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e545999-fc37-38b4-86b1-d4780e5f5d9e | -6.4552 | -55.45437 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52c309b5-350e-33f0-9bb2-17053a6344e3 | -8.88907 | -66.73018 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99b771df-26b3-32ce-a105-1067fe1db7a2 | -8.3435 | -62.83161 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a2d3fb1-551f-3bac-b46b-4a77f9cbd47d | -8.54387 | -67.02685 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adec8469-6c67-3723-bd1b-130a7e32fc8c | -9.1597 | -68.26929 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 109a32dd-0aec-322f-b73f-073e4fecac16 | -10.17706 | -57.96558 | 2026-10-04 05:18:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README66.md)
