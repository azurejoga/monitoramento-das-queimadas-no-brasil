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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d535a1bf-e501-34c1-911f-1ecfd30e9de0 | -9.43755 | -60.54324 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a11e9fe6-bc4c-32bf-972d-2632478ce903 | -9.45071 | -62.35892 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 737ef4dd-81db-38f3-bd67-ee1b56a5f090 | -9.11225 | -61.20218 | 2025-08-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daafd0ca-d1ac-3c58-bcaa-a04a26e72a53 | -9.06417 | -71.25475 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afeaed87-4aa8-3505-bfee-ee85d819c9be | -13.02719 | -56.90213 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01f4984a-0421-3a7f-ae53-767453766da7 | -8.66691 | -62.82924 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e7d4f8ab-8ec5-3cc3-a66b-74a1825be9df | -11.32938 | -63.27172 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 160f3016-347e-30f5-980d-deb65674e7af | -8.6597 | -62.82816 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 30a50c44-7257-3150-801a-ba5ad7e6cd76 | -8.86184 | -63.02547 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df57eaad-095a-341c-a116-44076204f18e | -7.90894 | -63.00668 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d52b19c-25ec-391f-a391-218185344cee | -7.95214 | -63.32792 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be6fbe27-55ea-371e-8c02-71ca694daf34 | -9.44222 | -60.5714 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bccba7eb-42bf-3d82-9759-c4f1e42b9d4a | -11.41851 | -63.24585 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1b2043f-2492-3458-8472-ef3b321ac9e3 | -11.32237 | -63.26377 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16520417-2ef8-36c0-b5e1-1acffbf1517d | -14.80481 | -59.71895 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 80d47960-f4d9-39aa-8039-6532592f7935 | -7.91129 | -63.01528 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d06400d-7bab-3d10-b26f-66bd3fada853 | -9.44118 | -60.57903 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 907a6398-d101-32f3-b313-f08d0f8d5747 | -9.45267 | -62.34537 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 071ade69-59bd-3779-afc2-03e428306bdd | -11.31748 | -63.27176 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bcfb8366-7b08-371d-b2c2-f4f1a7048232 | -9.44391 | -62.35326 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e366a287-936e-35b3-b3be-06d1320e19d8 | -11.41187 | -63.24043 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33f9adec-658b-3b20-8689-44cd23f3a959 | -10.31355 | -59.20176 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7edd19c0-0418-3e51-ab70-a3b171d650c5 | -7.46415 | -70.12636 | 2025-08-31 05:44:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ff74222-5626-31cf-b870-ec4556e8fbeb | -13.02333 | -56.88589 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d68ac3b-44c6-3bff-85f5-6a82b58f526e | -8.743 | -64.08711 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edb55bd1-086f-3520-b646-6404be5317dc | -8.9184 | -62.42182 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c99ee54-1136-3d6d-9dc8-596e527f461c | -8.66503 | -62.84175 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3aea807-59f1-3487-935a-7bd16f49bf75 | -9.44503 | -62.37183 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e56cc84d-9421-3e46-9097-c99248bfb992 | -7.91542 | -63.0118 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e26994c-9556-361b-9bbd-0ef7f489eec5 | -8.59616 | -61.95605 | 2025-08-31 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d256c312-d2d1-3a6c-a23f-573013ca8866 | -12.91812 | -56.97586 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a233031d-e76c-3ca5-aafc-0ecaa730ea15 | -8.84874 | -64.15237 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 934e4fd8-4545-342b-bc43-c43f1f4345ae | -13.02111 | -56.90546 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d779a7c9-4bda-3882-a912-5bad19a07c1f | -8.66366 | -70.04311 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e92ada8-19c7-3ca6-a2a4-696edcbbbf5d | -12.22629 | -64.22026 | 2025-08-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b6b80a0-ba4d-3c58-83c6-b2ce08637412 | -9.27673 | -67.64548 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b53e2494-9ca1-3d9f-af2a-c82e48b45329 | -7.91188 | -63.01126 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a578e5d-511c-3822-9b1c-997878a6362d | -8.65017 | -62.43879 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3663de5-fdea-3939-8acd-c730bdf8f34b | -14.80499 | -59.72095 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f309a6be-0e79-39aa-ac58-69a9dfe88c9a | -7.60418 | -70.20176 | 2025-08-31 05:44:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4f034ee-df5a-3f7b-95cd-f964bfe5c6af | -8.74399 | -62.38345 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8321674c-7c4d-31b2-af12-d9a011f5d47c | -9.45214 | -60.56116 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ef85a86-fea0-321d-95e2-43827ae6b609 | -13.02067 | -56.90937 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f54bd17a-16f1-324d-86f4-b215695d01c0 | -9.45397 | -62.33641 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c10318f0-a2ce-3730-97d2-1d8abd65f4b3 | -8.64766 | -62.83484 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d8a70ea-7c58-3465-b393-7556823ce882 | -9.43753 | -60.57463 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aeff3d91-aba5-3f90-baf6-f3d886efe93a | -12.61129 | -57.01265 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0d8bf64-de68-3610-8ce4-c07892fbb64a | -9.46014 | -62.34648 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3ad13e83-e52a-3b45-b797-ada20f6e26c3 | -13.02945 | -56.90053 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89266f87-984d-3a8a-88b9-3642e2d8ccbd | -9.27335 | -67.64494 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97ba59c1-efdf-3634-a28d-53ef81e7471a | -9.45136 | -62.35442 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a968310-8c99-36fe-831b-a7dc1b9ddebd | -8.74704 | -62.38843 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b76604c5-b76a-3450-b735-73256e62ae1f | -8.38818 | -70.76247 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60cf1e0d-57ed-3cec-ba0b-8ecf340059f2 | -11.32272 | -63.26633 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86c1dc4e-6f60-3694-b21e-43b703a9886f | -8.4451 | -70.14112 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb3e017d-4ba2-3f64-834a-c04bb21cd427 | -11.31811 | -63.26749 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9de1a759-e4ad-312d-b8d7-e58864d69f5c | -9.0646 | -65.40981 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba83f6c7-70aa-36ae-a07f-a6c4ad76c654 | -9.46254 | -62.35612 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d8fe63fc-d79c-3372-9aac-987a8defc397 | -10.30414 | -68.26574 | 2025-08-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 755ede97-21d5-3974-a1bd-d20781c004b5 | -13.0177 | -56.88516 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf3998c5-5db3-36c8-a91f-8d0c9e9e465f | -7.90185 | -63.00559 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a7a083e-f64a-3da3-b68a-20880e811de7 | -12.43876 | -63.92817 | 2025-08-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f54684d8-fa5f-3c17-ae28-099f5e272c95 | -7.81302 | -63.18859 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 577b89e4-5ae7-3e7a-a349-1f74a9fa52ee | -9.44829 | -62.34933 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1de10d45-f860-3233-b521-04a7952fa117 | -13.01592 | -56.90093 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3708e8bb-9c5e-3bda-9c7d-72e8b62e2c50 | -14.31004 | -60.35051 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aae02f38-8a1a-39b8-a87e-8036eca8f833 | -8.55929 | -63.01128 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96848366-1713-333a-9f2a-7cafeed95fde | -13.02897 | -56.88651 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3daa448-6a63-3ed3-b572-cfdf41cdce9f | -9.06575 | -65.42435 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbfb496d-2457-37c3-bb82-b8afdecc48bc | -11.32696 | -63.26261 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fac71f77-5fa3-3c92-8bf2-f502e091b109 | -9.26998 | -67.64439 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0a7617a-c968-33da-a2cf-366f760da16f | -8.5581 | -63.01944 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 474dbd9b-c01a-3163-9930-797fbf800460 | -9.45882 | -62.35556 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b417f83a-245f-3971-a0c4-7339aa924169 | -11.32635 | -63.26689 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37e9c02a-043b-3f30-9de4-dee0dc08be60 | -8.6417 | -62.82542 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79bfc27e-19ac-39e2-a7a1-15a1f4487379 | -7.66788 | -73.29628 | 2025-08-31 05:44:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43062189-41ea-3393-bdc2-ce15d9ee7bcf | -9.43515 | -62.36115 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ef0c955-7136-3d45-83ae-a023411d520c | -9.44894 | -62.34482 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b2cc631-8967-3cb9-aae4-c1b24f97cdc6 | -8.69458 | -62.87849 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14496a5f-92c5-3e07-8d42-bc47bdddcfae | -9.46079 | -62.34198 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 43048641-ba45-3f04-bb31-3395ccfa7ff1 | -9.46387 | -62.34704 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a88b8281-b701-3fe3-a1de-bac8ff3f18c6 | -14.59294 | -54.55584 | 2025-08-31 05:44:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 561614ac-f328-3e13-af95-30cad821c168 | -11.326 | -63.26432 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 168aad46-a123-3150-8164-546a5d00363c | -13.02523 | -56.88826 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c39d5535-463b-3f2e-a1a1-6668e49aa649 | -9.43909 | -60.56319 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1abef9da-95fd-333e-9d12-3dbf5544f106 | -9.33238 | -68.21305 | 2025-08-31 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fd4172e-6888-384b-ab45-ee1819418eb9 | -7.56527 | -63.41478 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4426102e-6f09-3d35-a6bf-d679e60bfa2f | -8.73966 | -62.3873 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14109591-2986-3f23-8bf8-dcc44bc3f165 | -8.42901 | -62.29475 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b469063-7c03-3034-bf29-8474aab308f6 | -11.32174 | -63.26804 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8be1c32c-93b5-377c-8d90-1bf0eecfc35d | -14.59897 | -54.56248 | 2025-08-31 05:44:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1087cd58-e17f-3b9a-b198-5231ab4cd366 | -13.01161 | -56.90653 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faf30cb9-da95-306c-a730-a6e5b2da3fbc | -14.79875 | -59.72865 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 859abf5f-1c17-35f2-8536-a580e3d66952 | -6.91935 | -71.75044 | 2025-08-31 05:44:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87017bfe-ccec-364b-ba9d-28435e5fafe5 | -9.46189 | -62.3606 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51a8c1fe-6524-3ddd-b611-0ecf00bc9951 | -15.22427 | -56.07574 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d41efc64-c11a-3c9b-b36a-bdf16c286589 | -14.79392 | -59.72853 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ff41dc18-9f5c-3cdd-a98f-4bcc31041c62 | -8.75261 | -61.86258 | 2025-08-31 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94f7e6e5-6a26-37d5-b594-108e06df3d93 | -8.74831 | -62.37959 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3fa91d9-e711-32d7-80de-d6a4751485c5 | -8.88598 | -62.38538 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README74.md)
