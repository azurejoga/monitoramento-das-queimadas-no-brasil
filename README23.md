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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d855dd63-4622-346a-8571-7f79ca275812 | -14.19631 | -57.40379 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc32cf80-2224-37e8-a004-56b975e56f0e | -10.9355 | -56.8322 | 2025-06-13 06:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| bdcb9f21-6229-346e-b72c-cc6d8ae515a5 | -8.68273 | -64.87247 | 2025-06-13 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30cd4e71-57a1-37da-9519-f4a8bc9fa163 | -8.68315 | -64.86928 | 2025-06-13 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dc7bd9a-7b3f-3c0e-949f-99f7e8e8345d | -12.51538 | -57.23021 | 2025-06-13 06:14:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4c0ce59b-31aa-317d-8d7c-f0766d41a284 | -14.19127 | -57.39864 | 2025-06-13 06:14:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a9f134f3-209c-3dce-8832-49ec2ae9d690 | -14.67515 | -53.36303 | 2025-06-13 06:14:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c03f37f3-b0cb-3974-a62a-7af285badeb9 | -13.89476 | -54.62315 | 2025-06-13 06:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 4416a6d4-5b4d-3157-b9cb-8b2791aad87f | -10.63891 | -49.43402 | 2025-06-13 06:14:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 974a2bb9-9141-3aab-bc34-543e9b3055cd | -13.8961 | -54.61401 | 2025-06-13 06:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| c571d98d-8330-33ef-8c93-988261879dfb | -9.40048 | -48.42506 | 2025-06-13 06:14:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0272042e-6457-3be8-83b2-7d2be00684e3 | -10.93309 | -56.83207 | 2025-06-13 06:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| fa5929ab-f1c8-31d6-b14f-cc0b509872fc | -11.56541 | -54.57017 | 2025-06-13 06:14:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 7ea53c23-6150-3b80-b8c3-9cb5d82f03dd | -10.91443 | -56.82907 | 2025-06-13 06:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| c65d8ca0-5ca4-3014-b092-8fb20de76095 | -11.91279 | -57.46803 | 2025-06-13 06:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| cb968404-815a-3eda-8535-9153c7053945 | -14.67373 | -53.37308 | 2025-06-13 06:14:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a2db6398-9d95-3d2b-975f-3992d9e77164 | -9.40195 | -57.55067 | 2025-06-13 06:14:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7a3e560e-2bda-321c-89c7-cc0eb31e8ff0 | -13.8857 | -54.61532 | 2025-06-13 06:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3bb9f01d-af2c-3dac-8e79-cfef50be4fb1 | -11.12149 | -53.9524 | 2025-06-13 06:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 70dcb992-bbce-36cf-96b7-42354b2a0681 | -11.80884 | -54.49701 | 2025-06-13 06:14:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5738c1f1-5217-30df-a169-573ffc3facb6 | -10.68814 | -49.49362 | 2025-06-13 06:14:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6281a00c-01b7-373c-8763-2a705948f7f6 | -13.89342 | -54.63229 | 2025-06-13 06:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| a697311d-3c37-3737-b15c-0cb791e0b206 | -10.92376 | -56.83056 | 2025-06-13 06:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 60af9f6c-a645-3603-92c9-00902919bebe | -10.64106 | -49.41814 | 2025-06-13 06:14:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 837d61dc-7377-352a-8fb0-f95b0d9d94e2 | -11.5566 | -54.56884 | 2025-06-13 06:14:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7708caa7-afdf-3a1f-9049-7beb26de7f62 | -14.20729 | -57.39783 | 2025-06-13 06:14:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 5dc55a1e-80a9-3103-bac7-c695b967690a | -10.93151 | -56.84216 | 2025-06-13 06:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c3e9416d-29e3-3153-9212-90013176bd96 | -13.89209 | -54.6414 | 2025-06-13 06:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a707b060-5584-3936-aef5-18040d17bd2b | -14.20051 | -57.4002 | 2025-06-13 06:14:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| adf25b38-d96e-35fa-81fd-5d5196709394 | -11.12284 | -53.94335 | 2025-06-13 06:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d6cea2b4-8df1-3f4a-8010-fc54924b157a | -10.22784 | -52.23596 | 2025-06-13 06:14:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1465bf9d-4c2f-3498-9cf0-2903b6dbfa21 | -11.56675 | -54.56123 | 2025-06-13 06:14:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c716b6e9-d66f-3290-86e4-5ac82cc1349f | -10.91283 | -56.83921 | 2025-06-13 06:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1386e08a-ab78-348a-bef5-a7d72b5e0027 | -10.92217 | -56.84068 | 2025-06-13 06:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b3593ad1-128c-3995-902a-6d5faa60e3a1 | -14.1897 | -57.40859 | 2025-06-13 06:14:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 816a4b19-dd57-3d10-a19e-e9a64deb635f | -10.6996 | -49.49516 | 2025-06-13 06:14:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e58d2961-9ddd-34a1-a9fa-7ae3bd3ce03c | -12.47028 | -58.46435 | 2025-06-13 06:14:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 30fe665b-f6ac-35ed-b135-94e441356534 | -9.21717 | -62.47544 | 2025-06-13 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c2c514d-f317-3cce-adf0-9a3d8a60245e | -9.22392 | -62.47161 | 2025-06-13 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9804c776-2604-36e8-8826-c22d2468380e | -9.21776 | -62.47074 | 2025-06-13 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74c630f8-1854-3b04-a3cc-74dccb450b10 | -10.04679 | -64.98281 | 2025-06-13 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3858666e-c768-3fee-8b86-2dc1b0c75e8c | -9.22333 | -62.47628 | 2025-06-13 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dde6a51c-4d0a-3920-b571-5d69033fe146 | -10.04637 | -64.98608 | 2025-06-13 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76dda416-6eb6-3529-8a6e-1fd281e40ed8 | -9.96237 | -64.97514 | 2025-06-13 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47f5568a-22a2-3908-9558-c0b70e36f26f | -9.96195 | -64.97842 | 2025-06-13 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09ae2ff0-bac3-3f7d-b679-9180efdc3e6e | -13.9059 | -54.6291 | 2025-06-13 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 0a642610-1a41-3042-978c-5042769be6a2 | -10.9355 | -56.8322 | 2025-06-13 06:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 64a0ae63-2782-3ee9-93cd-db0067e810d0 | -13.9059 | -54.6291 | 2025-06-13 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| fe82c65e-602b-3a43-8b4b-127901216812 | -13.9059 | -54.6291 | 2025-06-13 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| e010aa8a-075c-304c-8945-075111534699 | -13.9059 | -54.6291 | 2025-06-13 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 1429983e-f266-3d2e-bf3f-51b7d2179366 | -13.9059 | -54.6291 | 2025-06-13 07:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 74c05435-fc24-3969-bb93-1fdca3b31679 | -13.9059 | -54.6291 | 2025-06-13 07:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 82feee37-6717-3167-a7a6-b1f93609899b | -10.6483 | -44.4861 | 2025-06-13 07:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 037759db-f652-336b-b2f2-019c3270fbff | -4.67478 | -37.76566 | 2025-06-13 11:45:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a04ed83e-f21a-3b14-9519-29bc8e5bfd48 | -4.89371 | -37.52693 | 2025-06-13 11:45:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| bd9d14e2-a0c2-3a1a-bc0c-409ed636eaac | -10.65013 | -44.47436 | 2025-06-13 11:47:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 4f0518f3-fce2-3902-856b-c7bf9ae3893b | -12.0082 | -45.13309 | 2025-06-13 11:47:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 4d45b138-cbd3-3514-a517-c99866866063 | -10.64631 | -44.48073 | 2025-06-13 11:47:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| c9396fee-2f39-377c-8cf3-04a89aaa22a6 | -8.79246 | -45.07848 | 2025-06-13 11:47:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| b392ad79-425e-391d-8f27-2bf7743e9a49 | -12.00112 | -45.12488 | 2025-06-13 11:47:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 2f38383d-cee2-3839-a2cd-d6cfc9fed260 | -13.72816 | -45.25556 | 2025-06-13 11:47:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| dd435a53-dbc4-3eef-ad5d-f53f6173600a | -10.6595 | -44.48285 | 2025-06-13 11:47:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| a9a0a421-a646-3dda-8dc9-e68ab02f27a7 | -10.6467 | -44.49554 | 2025-06-13 11:47:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 38.1 |
| c2e6bb8f-1f8b-36ab-a5c2-acdfe3bc6010 | -12.1718 | -44.33631 | 2025-06-13 11:47:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| bfbfa590-c35a-35cc-920b-671f33337c33 | -8.79517 | -45.08478 | 2025-06-13 11:47:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c43a8956-d76a-3e5c-ab52-16b86ea33c4b | -18.65351 | -40.43956 | 2025-06-13 11:49:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 33420d10-ec8a-349d-a12d-0bf64509aac3 | -13.9663 | -54.4364 | 2025-06-13 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1305f19c-1f68-388e-a5fe-5a192d04730c | -13.9667 | -54.4157 | 2025-06-13 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ccc47078-f976-398f-8617-0fc139aecb79 | -8.7996 | -45.0815 | 2025-06-13 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8acdde54-4270-370d-8d64-da9d581dd414 | -13.9663 | -54.4364 | 2025-06-13 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e1f73f21-82e4-3d96-86b1-fcdc3e72e295 | -10.9355 | -56.8322 | 2025-06-13 12:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 74c325b0-7e9f-32e4-86be-dd45cb5ae02e | -14.0783 | -53.4042 | 2025-06-13 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 9fc96367-b46d-34f7-982d-d4bcf2609f28 | -11.5779 | -44.8413 | 2025-06-13 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 29142b8f-66f9-37bd-83cf-5d592ef34141 | -10.9167 | -56.8336 | 2025-06-13 12:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 9d493a66-e68f-396a-b3ae-33c37231396f | -10.9355 | -56.8322 | 2025-06-13 12:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| f2f4c08f-5758-38d0-aea8-903bf8d7ce41 | -8.7996 | -45.0815 | 2025-06-13 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ce3d5499-c0da-3531-b2f0-f90f8d8957ff | -11.1729 | -47.392 | 2025-06-13 12:50:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e382f0f6-8bfe-3ab7-9665-41b20fdcd6f0 | -11.5779 | -44.8413 | 2025-06-13 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| dfdeba9b-ed50-3536-b658-efadb2329c30 | -10.9355 | -56.8322 | 2025-06-13 12:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 153.3 |
| ee9facf8-91d4-3cbe-958e-c04f369b66ba | -14.0783 | -53.4042 | 2025-06-13 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| b9b61dbe-3c2b-3414-9365-9b7581e9f3fc | -10.9167 | -56.8336 | 2025-06-13 12:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| c217f547-0338-3284-9e46-6299ec2107df | -10.9353 | -56.8522 | 2025-06-13 12:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 735f464c-61a4-38bf-a087-8a1f009b6ea6 | -10.9355 | -56.8322 | 2025-06-13 13:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 194.5 |
| fb420aed-3153-3414-ae60-ff6215538699 | -10.9353 | -56.8522 | 2025-06-13 13:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 48352fcc-26f6-34a3-96c8-64280efbfba7 | -14.0783 | -53.4042 | 2025-06-13 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a1b60dac-585c-36af-ab8f-a83cfd9cc4b9 | -11.5779 | -44.8413 | 2025-06-13 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| dcd323c8-a41f-3a59-9a40-19a64ab2b7ab | -8.7996 | -45.0815 | 2025-06-13 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0ff1627c-5134-3da8-9232-353e2d278f44 | -10.9167 | -56.8336 | 2025-06-13 13:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| c0fcfb7d-74dc-32db-93e7-d7b3cd7a3dc0 | -11.5779 | -44.8413 | 2025-06-13 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| ad6976c3-e66b-397d-bc30-f90678deaa04 | -11.1919 | -47.3896 | 2025-06-13 13:10:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 101b8031-5ddb-310e-8a24-53bd72b0ee8d | -10.9167 | -56.8336 | 2025-06-13 13:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 6fe248d3-0e3d-3c21-a301-408ae8f7c879 | -12.518 | -57.183 | 2025-06-13 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 1d25bd94-4bb2-399c-9892-59d3f8b7edd3 | -10.9355 | -56.8322 | 2025-06-13 13:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 86eaea1a-15e9-3fc0-830b-93bb8b724676 | -14.0783 | -53.4042 | 2025-06-13 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 9dcb0976-a43d-3503-a93e-b4ea19a61315 | -11.8963 | -47.4537 | 2025-06-13 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 111566d4-daa3-3dfc-8f39-6f603384d4ba | -12.5177 | -57.2031 | 2025-06-13 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 73e837a9-3bb5-3018-9756-2517f22b5800 | -10.9353 | -56.8522 | 2025-06-13 13:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 7265fa60-a2b7-360f-9958-34d4e0ff749b | -8.7996 | -45.0815 | 2025-06-13 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 79e01c2b-34a5-3a9d-b255-3e7ca970de3e | -12.5177 | -57.2031 | 2025-06-13 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 0ba0ba35-1697-31d0-8fe6-9775c16efbe6 | -10.9355 | -56.8322 | 2025-06-13 13:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 238.2 |


[Clique aqui para ver as próximas entradas](README24.md)
