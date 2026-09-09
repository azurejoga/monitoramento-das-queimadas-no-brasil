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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a672b427-ebb3-3490-84aa-26f806499315 | -3.68383 | -58.5237 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7967711a-5f69-34eb-9bbf-b867d4d0060a | -3.36644 | -59.42597 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9be00410-9ce0-32f7-b87c-ad2d25a6e26a | -7.09126 | -59.81819 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ad2589-4b84-316f-bf59-4f309dd6c559 | -5.1843 | -59.75976 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaa328b3-d16e-326a-8c38-f48aeaa05ead | -3.95925 | -59.35791 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72f66c1d-f5a4-39ba-aa42-00201c620ec8 | -3.37737 | -59.42379 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e430a4b-7b35-37af-a8f2-c48ef3c85ff9 | -3.38516 | -61.31055 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9d44509-d1c5-39bb-9386-56415594056e | -5.47622 | -60.23573 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fcf3f0c-f33a-3129-a0c2-3fea7913efbc | -3.68142 | -58.52862 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1d843b1-d34f-3061-9c96-8dd7ea9a1d85 | -4.29045 | -59.96375 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d1ddd40-f3be-37ef-80b1-34f5bf1194cb | -5.2882 | -60.1129 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e194bd77-23f6-383d-add9-cb4f62f57ffa | -3.89716 | -59.60105 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aac45890-dfd3-34b6-98cd-64c48799debc | -7.08774 | -59.81763 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf340c14-3b38-3d22-864a-0338872da11a | -6.8657 | -56.5741 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 312bd0b5-d2b6-3666-93bc-a63a1781c95b | -7.09067 | -59.82213 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5af91692-818e-3147-9375-63a706089907 | -3.95556 | -58.95689 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0325133-9071-3326-a3a8-ee948134a3fa | -3.96502 | -59.36666 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e64d94cf-4fe8-31d9-a263-a1d845dced17 | -4.66745 | -55.62754 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35f2d8fa-6831-3bea-80ca-dfa84bb463fe | -5.29105 | -60.11713 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10b4997f-c258-3ea9-a766-d6a67d55eaa4 | -3.38078 | -61.31692 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9c78112-18b5-31c0-8e8c-535669dcaced | -3.38248 | -61.32775 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20123f10-2606-3e30-9756-e9c989f5e31e | -3.15041 | -60.65356 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ade29868-49e8-3847-b4ad-02907e5891c4 | -3.43078 | -59.26072 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1745b9c-4bb2-312b-aa03-ba63f89cd890 | -3.38462 | -61.314 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1075c0dc-95a8-3b51-88d3-348bb96703fe | -4.20805 | -59.99675 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2032c41-38cc-3d23-94a2-22f3875a0e50 | -5.29127 | -60.11666 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbddc526-c412-3ac9-9880-607ad406d36f | -4.51076 | -55.71323 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15a1ad38-37cd-3798-b078-ae0952918d37 | -6.76488 | -58.96061 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b249eb5d-e2fb-393e-a0ce-4a346df79ad7 | -4.19385 | -59.95322 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d60fb79b-c632-3c06-81be-1eb5b04b763f | -3.31391 | -61.35228 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3783142-9a89-351e-a414-f4dc42720370 | -3.41214 | -61.31119 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad4661cb-65ab-36b6-87e8-52e61cf889cc | -3.43485 | -59.25742 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ac13aea-a1f9-377a-aeb8-42e249813bae | -7.06017 | -59.78186 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76f07273-c23b-3ddc-a02e-5797d88abd26 | -5.36765 | -56.02005 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 891c186b-b5e4-3afc-98fb-cf2952004957 | -4.20691 | -60.00408 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d233ea8c-e87a-37dd-91b1-809d2b3665d2 | -5.28763 | -60.11662 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6db16ff4-25c6-3e84-86ef-c0de80422562 | -3.05671 | -59.27199 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fc8541d-46c9-3db2-a138-08f0e5dd6d5a | -3.68566 | -58.52502 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7fbfa02-c41f-3231-9914-72acc0fe1ff3 | -5.44669 | -60.24628 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06b73a43-611a-3605-9005-e71c50b2c6e6 | -3.45779 | -59.99149 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1613f377-e2f4-369b-96db-5729a9e1c58d | -6.76886 | -58.95935 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d734246-af75-3bec-97bd-387622f96a88 | -3.15844 | -58.65075 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a76eefcd-fe9a-3590-8176-6240a38015c5 | -3.68743 | -58.52424 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f41273a-662e-3554-b25b-222ed2f8de61 | -3.36183 | -59.43299 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36fc67de-cdef-3f2d-80d6-34eec80651c7 | -8.98506 | -65.38766 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bfbe949-72cb-3245-b99a-0e17b9922487 | -9.21053 | -60.924 | 2026-09-09 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdca475e-1bdc-3070-8a77-0e6fa266a471 | -9.24636 | -65.67671 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2d86658-3ee3-3cb9-9fa3-3d6894eb1696 | -9.01558 | -65.42085 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 196df281-73f5-3f20-80ed-760caf2e8eb8 | -9.52035 | -68.64159 | 2026-09-09 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a63134de-e8f3-3163-875c-bb8f60533759 | -9.64974 | -59.60933 | 2026-09-09 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15044898-f0c6-31b6-acb3-1e6bb4e3aea4 | -13.23521 | -61.67431 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78bfe167-6300-348e-a384-18d169a5b75f | -9.48779 | -68.34557 | 2026-09-09 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 729a51a8-b5de-336f-b25b-c23f5bee39d7 | -13.28931 | -61.78487 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dd6839e8-9f28-3df8-aeca-5813cd780f7e | -9.00858 | -65.41972 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd4d4b3d-47c3-38ff-8a18-60d50df2b7e6 | -8.96219 | -60.49806 | 2026-09-09 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7607f233-249c-3c55-9190-092828109227 | -8.9848 | -60.58442 | 2026-09-09 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46654817-d1f2-387a-b966-0eaa12458330 | -9.07929 | -65.49928 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b160b49-4cf7-3bd7-9e42-1c643ae3acad | -9.23733 | -65.75375 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6663ecac-f2d1-3946-9efc-4d97352de4ad | -9.84936 | -66.45867 | 2026-09-09 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ddbce7-a7d5-3e8b-b1bc-3897938170fa | -9.03882 | -68.5043 | 2026-09-09 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6896e869-7de7-35f9-a5b2-8790d9e2c9b6 | -9.86652 | -62.97393 | 2026-09-09 05:31:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9fc3d7e-f46a-3f40-b488-9d5531de0f72 | -9.00795 | -65.42366 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6af21e8-985e-3f89-925e-5272bab32986 | -8.98792 | -65.39217 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| beb4d75a-9c22-396e-98fe-f1114c9d7f3d | -13.21614 | -61.82825 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62133fb1-28c8-3ace-9448-03eb2196ad3b | -8.98759 | -65.41629 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f59db4a5-9782-3294-b584-889cad33db43 | -8.99109 | -65.41686 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d2252fd-d991-3b00-8f43-6a4c404afe76 | -9.24284 | -65.67611 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d7f705c-ed4a-3742-ac33-a3f044dd8a3a | -9.01622 | -65.41693 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 173cb047-2a45-3b12-8358-5b256df203d2 | -11.57134 | -61.65228 | 2026-09-09 05:31:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c68cb2e8-68d3-3588-a593-e83c771249c6 | -9.23379 | -65.75315 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dc8f33a-c541-3991-9bd1-ea1be6875ae8 | -9.32319 | -68.20691 | 2026-09-09 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c3e3134-516b-355a-a325-c52f78e91389 | -8.51641 | -69.79672 | 2026-09-09 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86d24e68-9021-3ad2-b3a3-d302d1e92995 | -8.98443 | -65.39159 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4682b570-de4b-34da-bdd8-9f8b784e7f90 | -13.26512 | -61.68682 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b56f4fe4-2a39-3d9d-adcc-8bae53fb5fc5 | -13.28988 | -61.78104 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 39a0f07a-7778-3ec0-babc-560b8bd078d3 | -13.23352 | -61.68588 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f1c23e9-e2f2-3c98-b1cd-c0a9d5269e31 | -13.28473 | -61.79198 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51a1e08f-5c40-3878-b105-c0c9e76c68b1 | -13.2853 | -61.78817 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dde705cc-8daa-3f06-8e31-0f0fecaaeb01 | -10.62266 | -67.92647 | 2026-09-09 05:31:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d77f5e2e-fb95-3fd2-bd73-1b340bfd2bed | -8.99173 | -65.41293 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2c4f4bf-32bf-3ade-859d-e8e306c259f1 | -9.2435 | -65.67208 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc2cd8d3-bd4e-368d-9eb0-db5dc273693c | -9.02332 | -65.44563 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00ca828f-f764-3e35-86c8-98b145a962c1 | -8.98827 | -60.58496 | 2026-09-09 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f57f634c-bb15-3779-a70e-10ecc3d43e59 | -8.74877 | -72.76669 | 2026-09-09 05:31:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70255124-3c15-3c4e-aa1f-a3a12a1d88f0 | -9.02228 | -65.44619 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2809c7ac-e01e-316c-b3ae-987cc54af0d6 | -10.66005 | -58.76842 | 2026-09-09 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 689aa677-cbb2-3811-92bb-ff2c38f45dea | -13.28129 | -61.79145 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b96111b3-1dc2-347e-a14c-eb7f1a185f70 | -13.28874 | -61.7887 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 69a0f0ba-7cf3-3c26-b81e-055a844aba2c | -9.61194 | -63.46941 | 2026-09-09 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc588cde-ac24-3ef9-8916-95587659e4e0 | -9.3391 | -68.23586 | 2026-09-09 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ce98b8a-a8ef-3214-876d-8f6b48d68db4 | -9.32316 | -68.20708 | 2026-09-09 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54dfbc82-4d3d-3b30-a23d-450695321cab | -9.01208 | -65.42028 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9b194a2-43e1-32f0-b3bb-2b488300f239 | -13.26569 | -61.68297 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9b033a16-f15d-3e11-a444-1c846062e003 | -8.98349 | -64.44347 | 2026-09-09 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebd5d563-c563-32f8-b277-3e0a0c16d345 | -9.01748 | -65.40907 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3518d3eb-2ba5-3dcd-91aa-8c0f7f019e4d | -13.21271 | -61.82771 | 2026-09-09 05:31:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f34242e9-cf7c-3914-8e3b-f32374eb61c3 | -9.2071 | -60.92348 | 2026-09-09 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccd13a04-d083-35dd-9d40-b58e5da07bbf | -8.98422 | -60.58826 | 2026-09-09 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04f3565d-247e-3b61-ae79-9da4f89b83d7 | -9.01272 | -65.41636 | 2026-09-09 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c21dd9b-dfaf-3155-bc78-202e6b7da80c | -10.65615 | -58.76794 | 2026-09-09 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README27.md)
