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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4e39907-2156-3cc5-b1d8-bc04c51892d6 | -3.10449 | -53.73877 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7049198c-b300-3658-8446-f646e1566a1f | -6.91419 | -43.67612 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83a66bdd-0864-3c8a-a6a0-7e13765d98df | -3.22391 | -53.87241 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e01026f-cdcd-316a-952d-3e0398a78df4 | -4.59882 | -49.62855 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b38a410d-f932-36a4-99bc-39e05e1b6775 | -3.4676 | -54.58741 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1b1285b3-d9ca-34f9-ab31-73efcb190832 | -3.04747 | -54.21389 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eadfcd79-17bb-33bb-9704-c9f1d7d7fa08 | -2.91296 | -54.12109 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd6141cb-c867-30d4-a10e-97592e26cdfc | -3.05569 | -54.16685 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3515053-0130-3ed9-9f09-3d181d30ea9e | -6.9019 | -43.66734 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f387d8ee-27f0-3222-83a2-f2691acfa6af | -1.46573 | -53.59795 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9049f060-3323-381b-a502-c88867d0504d | -3.30618 | -53.84959 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffa14d4f-c436-3965-98f6-42125e6469da | -2.80106 | -54.11844 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c80a2aa4-60b7-3c84-a97d-514422754a3d | -3.09895 | -53.74086 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| beda3c25-ce9d-3d58-ad8a-4e343059e5de | -3.12361 | -53.73644 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f0b1e3e-d659-3a0c-ac9a-7a7640827050 | -1.1697 | -49.2501 | 2026-10-05 04:38:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e961440-fda4-3b0b-9444-66e239ab27d8 | -3.11848 | -53.70561 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc67f5bc-d4fb-3cb7-a7d3-25c7ac989bbe | -3.31635 | -53.85132 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d9e709f-5425-3ad2-9031-26e9dcaf08d0 | -3.31175 | -53.8475 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4c8effc-edbe-309f-bd73-19ac9883f141 | -6.89529 | -43.68664 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7e370421-b599-3117-80c7-976d40871be4 | -3.37712 | -54.10122 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ada95e5-c8a9-36eb-88e5-5bfe7e13e729 | -4.04771 | -51.07757 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e83234ad-d1fc-3e6c-b682-e5fd7cdbf221 | -7.18187 | -42.00263 | 2026-10-05 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 39520107-47ea-3c27-8a01-186a0370f5ca | -3.70142 | -50.65894 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 226bd5e8-384d-3d7a-a685-74089ae3a4e4 | -3.94704 | -40.93326 | 2026-10-05 04:38:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| be9f278b-35af-3c45-bd1e-80259c36ff63 | -3.10641 | -53.72708 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 65e74074-88a3-3434-b7b1-f3e0fdb6daa4 | -3.20788 | -50.75332 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34b9ca1b-d8c5-3ecf-ab02-489bcf32c096 | -8.31224 | -45.47397 | 2026-10-05 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a55f9459-6da5-3a60-8767-58169034eb20 | -3.06018 | -54.17081 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1c077d4f-6310-3d7e-ad36-fa19d2e90790 | -3.07269 | -54.16027 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 30ac3cd0-453d-3fe1-92ac-45f1a4e2f40b | -6.8959 | -43.68269 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02fb600d-fd70-3cd6-a424-37366cfb9ae4 | -2.78332 | -54.0962 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9e6ba66-aff2-3669-8bf2-965dc4349dfa | -3.1246 | -53.7306 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c939b94f-0bc3-3760-a04f-abe92e8437a4 | -4.45978 | -54.96099 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ab4f7f9-0f33-3cec-ad36-3ab9188a4758 | -3.04492 | -54.23302 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ded31d63-be10-3cc0-bb86-50067c7ddec7 | -3.84406 | -55.84094 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de61b624-6678-3f8c-a332-da4b1e6f28f0 | -6.91834 | -43.67263 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d865c83-fd0f-361b-baae-ec6105db94dc | -3.50641 | -54.61768 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c961f274-223b-388a-9841-9c23ac4c2853 | -3.00956 | -53.86928 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e68c82f1-ff9f-3db5-a46b-483d1070bbcd | -3.06592 | -54.16858 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 56ac3064-80f2-3504-ab01-a488dc3450be | -2.97242 | -54.08861 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b49c82f-cd4d-3148-bc98-29cbd8593952 | -6.4189 | -51.95865 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2262e853-d974-373b-bff5-be3b76cfbab0 | -3.12081 | -53.70249 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e21c9204-0461-3f4c-9e00-f6d9e7a2d270 | -1.09947 | -54.10939 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a822106f-a33f-3b3c-8d1b-4bbe04910e81 | -3.51363 | -54.62571 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd918bfc-9423-339c-8686-dbc30e1281be | -6.12743 | -53.05062 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64a69165-9d7c-3bfa-86c8-71407a5e2cc9 | -4.86474 | -43.46793 | 2026-10-05 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e31dc130-db05-3955-a2b2-b9f20bb91d89 | -5.58367 | -49.74514 | 2026-10-05 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4d7006aa-9fea-3ea9-ac35-a2ba6d0721cb | -4.28908 | -50.26869 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0521c3f-6797-3ed1-b893-2c8220df4d42 | -3.47212 | -50.103 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6bde858-8b97-3a24-9c4e-452823b17e35 | -5.98933 | -53.63389 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c88de8c9-c7f5-3cb6-b923-cc831eaf6168 | -2.69034 | -49.03571 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1dc4ef13-0d7e-31b8-a79b-f7ff6bd9702f | -6.61652 | -41.56325 | 2026-10-05 04:38:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 23ae6a1a-27e6-374a-b83e-422e9e33a5b7 | -4.11151 | -49.0704 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 100e5eda-63b1-3818-89be-8fe68c8f14fd | -3.80682 | -50.85744 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc9bfaf4-d501-3905-bb35-959771c3673a | -1.62931 | -55.13453 | 2026-10-05 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d34776d8-69aa-3c30-9ddd-2e101a51d2b6 | -5.98842 | -53.63918 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b569ca2-04a2-383e-a5bb-81d8f6893119 | -2.96351 | -54.10962 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 447f695b-e96b-3f63-8351-63e98f4d4ee1 | -2.78906 | -54.0939 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da785620-84a0-3ac8-9297-17b04ab333f1 | -2.57818 | -51.86467 | 2026-10-05 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd477cad-692d-32a4-aab5-7a7082afc994 | -3.64801 | -55.32149 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a535d6de-ae99-3e97-af95-0fcc95ac6783 | -3.11795 | -53.71999 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a974172-339a-3d0d-8d5d-5f9cba9a3dbc | -2.98123 | -54.09966 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e58a627-2537-3b23-87ef-71339e29401d | -3.00908 | -53.87212 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d4c05b7-c513-316e-bf2f-2d91c00f0760 | -3.61343 | -54.60438 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfd37a0b-2a2b-3d67-90f5-c9c13cefbd0a | -3.30667 | -53.84664 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c062389-584d-3b1f-b40b-7c27acf53f70 | -4.30807 | -50.78292 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e023e1ae-54ce-34d8-b182-bfdeb5dc13ef | -3.31223 | -53.84455 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5439bdd-98cf-3ad1-9cd7-e4248041612a | -3.11705 | -53.74438 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d251d690-7a5f-3a85-b51c-022bc5d47950 | -5.99409 | -53.63484 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6ab5e5d-fc47-36c4-8e32-90694be70537 | -3.84298 | -55.84676 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe088d7c-3388-397e-9173-08d0c7c3b298 | -2.57627 | -51.86691 | 2026-10-05 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 018eedd1-7c15-3fd3-a31b-8818ec9d945e | -3.61095 | -54.6012 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48c7a258-d7f7-3ebe-b72a-235b3d186c67 | -3.27961 | -54.17474 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5045f98-772d-34f3-8199-d3597fa21f1e | -4.03417 | -43.38498 | 2026-10-05 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ad90990-a360-34db-9053-479eb73525e9 | -3.12395 | -53.715 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 00cf27d3-7267-3fba-902b-ed545acde776 | -3.11529 | -53.70454 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5df76ad1-1381-364f-9545-ecd375ee99ed | -5.58293 | -49.74961 | 2026-10-05 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f7d21e70-d903-30a5-9702-3fd83dfe0207 | -7.09441 | -41.75586 | 2026-10-05 04:38:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c0d92110-e231-3dd8-8e44-b988a5e479ff | -3.79514 | -50.79954 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a296b945-283c-39d7-b8fc-297dd530158b | -6.08874 | -53.48563 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea962040-a072-385e-9eac-07c8fac5953a | -3.46586 | -50.09179 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa9e6300-0b7f-3f5d-8fd7-89785b34896d | -3.37663 | -54.1042 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a3958a1-52c2-393c-a104-0fcdbecf1842 | -3.15665 | -50.43631 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c2f71f0-0a44-3d3b-a21f-d543a865810e | -6.26178 | -52.86672 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 386d9526-095f-36ec-a856-b39a49686518 | -3.79105 | -50.7988 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f92d7808-5a62-316b-995f-5cd611e457fe | -4.4646 | -54.9651 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3a1dd96-50f8-3aca-bc74-10e8de66562e | -3.11898 | -53.70274 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 59df9940-c134-331d-bc76-5752030fda01 | -2.89629 | -54.12476 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b36a0638-9bb2-3263-bf01-5e914275aa75 | -3.10231 | -53.72038 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b91c1cf0-ab46-3d2e-b2e8-61f4e4fdad49 | -3.06124 | -54.16455 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 12d82d6c-d90b-3a92-aa05-4f0fa768068b | -3.37869 | -54.10035 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a13d8954-9f49-3d59-80c2-2e144a4a2646 | -3.09943 | -53.73791 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64b14c26-7077-3152-872c-26dec0213fee | -2.79218 | -54.10732 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed810516-a03f-31ec-bdab-e4af1a59620d | -3.11938 | -53.71123 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 649caf03-bd90-31fe-9310-e8efac903459 | -3.0734 | -54.147 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 06df353f-6355-31ab-a985-57a1168d1fa5 | -3.4577 | -54.5977 | 2026-10-05 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b807ae79-5097-3320-8d6f-e14b14f2c5ae | -2.9817 | -54.1091 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ae419064-bd38-3bcd-b34e-d345d3e30363 | -3.055 | -54.1675 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 3936656c-ddc2-3865-8d3e-0fc0f7c3e382 | -3.0734 | -54.167 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 235.5 |
| f2ab2fe6-389d-3a9e-bf4a-c871fce9a3a1 | -7.4442 | -63.5589 | 2026-10-05 04:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |


[Clique aqui para ver as próximas entradas](README28.md)
