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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5ec50d6-3f91-3892-89e0-7d4dab7b6836 | -8.2128 | -61.393 | 2025-08-25 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 339.6 |
| 7c889898-8f13-32bd-88c4-89274b791669 | -9.6553 | -59.6302 | 2025-08-25 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 99ed7cbe-a074-339d-a37c-3b25f1f47cd7 | -8.2129 | -61.3739 | 2025-08-25 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 216.1 |
| 615c22a7-f39d-389f-9e26-69b058aa86f7 | -8.9689 | -65.4198 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e2409d15-2e9f-3c4c-9d3d-1604750fa1fc | -6.8745 | -45.6528 | 2025-08-25 02:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a4eadc2b-8acc-3cdf-a4c8-93b288ae7e2c | -6.8413 | -58.9552 | 2025-08-25 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| f73dfef7-3528-35e2-9a30-ce868cb01287 | -8.8919 | -62.4487 | 2025-08-25 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 8a12f563-932c-3440-93fd-d14eb427ab23 | -11.4595 | -55.4633 | 2025-08-25 02:50:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 98406ee2-b1e9-391d-9476-48fffe992fef | -8.1942 | -61.3938 | 2025-08-25 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e7020c78-31d8-3b50-a7ae-efb58824de2d | -8.2314 | -61.3732 | 2025-08-25 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 84187e0b-4164-3f37-b978-cf87b8bc1111 | -11.4593 | -55.4836 | 2025-08-25 02:50:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 022eb746-b7e3-3f8f-9377-908a398a1997 | -5.1181 | -43.1964 | 2025-08-25 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| aec4f49d-5d59-3b3b-aa78-33cf580e84c6 | -9.0061 | -65.3813 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 08c37eab-2c7f-38e5-8c96-15186ea606ac | -9.0601 | -65.7157 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 22f9ebbc-b224-39a0-994a-18c5516bea29 | -6.823 | -58.9367 | 2025-08-25 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 6de3c2d3-3dd0-3eb6-9578-346e67c026e8 | -8.9875 | -65.4006 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b19aa5ad-65e9-385e-9125-ae8cc771dd5a | -9.006 | -65.4 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a1cc3f4a-0198-3039-8aff-99cde4fbe872 | -9.0415 | -65.7349 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 965df541-a6ef-370d-9540-e7a43c9f8197 | -7.6326 | -62.7243 | 2025-08-25 02:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9b2cdff9-c0f1-369f-9710-89173bf01fae | -5.118 | -43.2198 | 2025-08-25 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| e3fdc55d-9817-362e-9c58-ed60112b1594 | -5.0992 | -43.2211 | 2025-08-25 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 9540fbfe-54c0-34a1-bd63-8c6d6932f80f | -7.9262 | -63.0724 | 2025-08-25 02:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 74ae937d-412f-3caa-9696-aa884baceece | -8.2126 | -61.4121 | 2025-08-25 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e4b3b043-b167-348f-b33d-e2678f006178 | -9.0972 | -65.7145 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| f532741c-29a3-3728-850a-4a20ba298ba2 | -5.0992 | -43.2211 | 2025-08-25 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| c3a9f7d4-21d6-3aff-9d81-328e39e34065 | -8.9874 | -65.4192 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 156.4 |
| c74fda78-c41e-3621-afca-ef58d27b945d | -8.2313 | -61.3922 | 2025-08-25 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7dffa483-1ea0-3678-9f01-19c3cdfb8e8a | -9.0061 | -65.3813 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e489964a-5ca0-3499-964b-3cc1b84ea53e | -8.8734 | -62.4495 | 2025-08-25 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 6cc924ce-72d2-365c-a838-05ab24d96b1d | -11.4595 | -55.4633 | 2025-08-25 03:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 5de07af2-5c0d-3312-b43f-828e424df47a | -9.06 | -65.7344 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 43d75e22-897e-3c2f-aa51-bf86d26ba084 | -6.8413 | -58.9552 | 2025-08-25 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.2 |
| e6e5fe35-b76f-324c-a2b6-8a822f88c5d9 | -5.0994 | -43.1977 | 2025-08-25 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| c0e9ebf9-e70d-3d1d-a459-26e8d0246e3b | -9.1722 | -59.4629 | 2025-08-25 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 82d80dbe-4383-3f76-a8da-869f504e1885 | -8.9875 | -65.4006 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 0f92ed8e-44a6-3f90-9557-b1563be2d204 | -8.2129 | -61.3739 | 2025-08-25 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 3a979592-2122-3d21-acb9-f34cdaf82669 | -8.9689 | -65.4198 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 1fab0da5-0f53-3e9e-8d68-6d962cdab2b6 | -8.2314 | -61.3732 | 2025-08-25 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1933a218-9d59-3841-ab2f-8601602232e6 | -8.8918 | -62.4677 | 2025-08-25 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f1c97da3-422a-380c-8730-b3e32f1c501b | -9.0415 | -65.7349 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 7d6a826a-30d6-3317-8076-945adec94365 | -8.8919 | -62.4487 | 2025-08-25 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7396db52-2f83-3ead-98ca-3194a3e3141f | -8.5136 | -63.8799 | 2025-08-25 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 57b5373f-7fb2-3ee3-87ab-ab58408f3863 | -6.8229 | -58.956 | 2025-08-25 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.0 |
| f375baf9-c06b-33b0-a6bd-74e4fea45a82 | -8.8733 | -62.4685 | 2025-08-25 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 3773cb3d-10ed-3273-9721-3f5b3adcd528 | -6.8412 | -58.9746 | 2025-08-25 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 226fef5a-bb34-3b6d-b5d1-7c200251502c | -7.6326 | -62.7243 | 2025-08-25 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| bd45ae73-b5f2-303f-ae7e-7925227ca202 | -9.0971 | -65.7332 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| f85817bb-53c3-3a88-8ac9-e57f47a8c885 | -6.8228 | -58.9753 | 2025-08-25 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 204e171f-c47a-3757-a628-5b216c929e47 | -8.969 | -65.4012 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 006592cd-caf0-3b81-940c-cc19961cee1c | -8.2128 | -61.393 | 2025-08-25 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 292fc07b-2aa4-3f2c-b228-73e8528463ba | -9.0416 | -65.7163 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 336c0d15-d2be-32bf-bc2f-aa13e662eaa7 | -9.006 | -65.4 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b43e5b9d-3590-3a15-83b2-53d90b664a20 | -5.1181 | -43.1964 | 2025-08-25 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c5ac8a5a-6203-33d5-b12f-ae787562e16e | -9.0601 | -65.7157 | 2025-08-25 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 5139d22e-87f4-3c98-94c2-048e03139fec | -5.118 | -43.2198 | 2025-08-25 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 47a67821-d7a0-325d-a6a2-2b7a438e11ae | -19.57327 | -41.61055 | 2025-08-25 03:04:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a9290719-3660-3a25-81c7-21d9dba9124a | -19.56637 | -41.60842 | 2025-08-25 03:04:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 58fd2ae2-8d1b-3fdf-8f4f-9d8dc47a1751 | -8.2128 | -61.393 | 2025-08-25 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c082634a-cb24-39bb-9541-bf50717bc476 | -8.8919 | -62.4487 | 2025-08-25 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 937cc7d3-d59f-327a-ae71-1d2d575ee639 | -6.8745 | -45.6528 | 2025-08-25 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 1d387e7f-12fa-3533-959e-b15b02489195 | -5.118 | -43.2198 | 2025-08-25 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 901b1a26-37e0-3e59-a6c6-4134619cf523 | -9.0061 | -65.3813 | 2025-08-25 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 92b4c0e1-c1ae-3295-a512-1fec2efe901e | -10.5937 | -44.331 | 2025-08-25 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 0a639935-2483-3bc8-a669-1469454fe44d | -8.9874 | -65.4192 | 2025-08-25 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.4 |
| eb55adf9-991e-3fb6-a78d-a0bd5e2949f4 | -8.8734 | -62.4495 | 2025-08-25 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 6f493ad6-9338-3c29-98ca-e9cadbfab372 | -9.06 | -65.7344 | 2025-08-25 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 651ded93-90ed-3c68-8575-865b559eebf4 | -8.9689 | -65.4198 | 2025-08-25 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| df180f82-d3bd-3302-bc9c-437f75f04316 | -9.0971 | -65.7332 | 2025-08-25 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 2fef66ef-0e7c-3f4c-bfd3-0ff733545d74 | -8.8733 | -62.4685 | 2025-08-25 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 122.1 |
| f2c9394f-2efc-3711-8d82-383d405b4d82 | -6.8229 | -58.956 | 2025-08-25 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| b43334da-854f-3fe4-8122-cba41facf4ea | -9.006 | -65.4 | 2025-08-25 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 80faafa7-d48f-377e-8a8e-07fd40009cfe | -8.5136 | -63.8799 | 2025-08-25 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 572b6d0f-1d9a-3737-9620-4492905e4a20 | -5.0994 | -43.1977 | 2025-08-25 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 057b6469-0964-398f-a403-d072462703cb | -8.9875 | -65.4006 | 2025-08-25 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 8101db1d-7f55-333a-85f7-07fe2bb20815 | -9.0415 | -65.7349 | 2025-08-25 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 9788cd64-0b95-3d71-9aaa-a3b23762515b | -5.1181 | -43.1964 | 2025-08-25 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| b07be07a-9966-3524-a7cb-c338c4d0fbe0 | -6.8413 | -58.9552 | 2025-08-25 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 1374d06d-f5b3-383d-a19d-9c97b21f3ce0 | -8.8918 | -62.4677 | 2025-08-25 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ab2939e9-a609-3957-8692-ce09cc5da271 | -9.1722 | -59.4629 | 2025-08-25 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3645b736-eb9d-336c-babd-9f9e10c4c990 | -9.006 | -65.4 | 2025-08-25 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 66434795-fc07-3cc7-89db-d903c1a89874 | -9.0416 | -65.7163 | 2025-08-25 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 6bd39c5d-c17b-3978-9726-f7e09dd6e090 | -9.0415 | -65.7349 | 2025-08-25 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| a5f5406c-1d9e-395e-b64e-c6b530eed7ee | -8.9689 | -65.4198 | 2025-08-25 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ea85f358-efdb-398c-8b7a-7458fe9e9d1e | -5.1181 | -43.1964 | 2025-08-25 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 68e9ff2e-16e4-3e70-8cff-0fef7edd9340 | -6.8413 | -58.9552 | 2025-08-25 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| f495d31d-2885-3485-8250-0021388fa3fe | -6.8229 | -58.956 | 2025-08-25 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| df0291e3-baf1-352a-9f4a-b02ab0492baf | -8.9874 | -65.4192 | 2025-08-25 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.1 |
| a68e673d-a4bf-3555-a507-ff94e5bfdc6b | -8.8919 | -62.4487 | 2025-08-25 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 1e38dd64-bad9-3e71-8705-558f3d090fcf | -9.1722 | -59.4629 | 2025-08-25 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 454c5742-6fc5-350b-8538-715f0b3f2a72 | -8.8918 | -62.4677 | 2025-08-25 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ca0285dd-96bb-3f17-ba4b-881f519ed192 | -8.8733 | -62.4685 | 2025-08-25 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 148.4 |
| d163f63e-47ac-3d01-87f7-e14f201e9583 | -8.8734 | -62.4495 | 2025-08-25 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 1f1648b4-88bd-3476-a46b-a7cc1c07756e | -9.0061 | -65.3813 | 2025-08-25 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 98fc8502-e7ee-3f38-98a7-8ddad7956c18 | -9.0786 | -65.7338 | 2025-08-25 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 6a7fd652-51ba-30ea-ae35-067ff8af5efb | -5.118 | -43.2198 | 2025-08-25 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| ac487a7a-67c6-380a-b455-932e7a51d89d | -8.9875 | -65.4006 | 2025-08-25 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| f71df4d1-9250-3577-88a9-96f3c866fb95 | -9.06 | -65.7344 | 2025-08-25 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 53e4b4a2-1601-38ec-b712-113ee724ea31 | -7.14159 | -44.16164 | 2025-08-25 03:21:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e14d44bf-f3d4-3fc3-a940-0fefe5d8c890 | -4.17281 | -40.72366 | 2025-08-25 03:21:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c727bc34-39b1-3988-88df-6b85481e97eb | -6.6755 | -44.43137 | 2025-08-25 03:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README18.md)
