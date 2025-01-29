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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce00c3f3-2921-30cc-a9b5-f72265660636 | -6.94136 | -43.54029 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9720d9d7-19e0-38fd-8292-82cc63068bd3 | -7.95143 | -49.76583 | 2025-01-29 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34d94f73-bd53-3e82-bcb4-390cceb66ce2 | -7.95229 | -49.7558 | 2025-01-29 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd44843f-73f8-3901-beaf-3ef9c005f124 | -6.51024 | -47.59656 | 2025-01-29 05:01:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1ce9d49-ba02-3ae5-be34-9baa999b201f | -6.9436 | -43.52351 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 751b8506-3882-3ba2-93cd-a5b81f7caff3 | -3.88269 | -54.21879 | 2025-01-29 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 374af59c-aa33-388c-94d6-e69abd757a03 | -3.70408 | -53.92712 | 2025-01-29 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 90c69a9b-b853-34e9-a6be-1bbcf0703018 | -6.94212 | -43.53463 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d586ddd8-0061-3c8a-b940-fdae85b68a6d | -3.48356 | -54.29305 | 2025-01-29 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7556a5ef-619e-3d3c-85f3-5e5f13767e43 | -3.02372 | -54.02118 | 2025-01-29 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| edcbc5c3-a7c9-3814-b91a-e959504768fc | -3.31039 | -53.86313 | 2025-01-29 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08119a16-d921-3f53-a219-69d6bbd17b5b | -6.93476 | -43.53951 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7a78cfce-122d-314d-9c6c-8133c3485722 | -5.4692 | -42.9244 | 2025-01-29 05:01:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 30561d1d-4b1e-35c8-89cb-bb0305d425a0 | -7.95108 | -49.76455 | 2025-01-29 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b1c3ece-808e-3435-8981-708d1b05ee90 | -2.3867 | -51.90128 | 2025-01-29 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7fcdacf-faf6-3987-b439-1425d47e2c7a | -5.47291 | -42.92271 | 2025-01-29 05:01:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99f87463-e73f-3887-819b-76b8771e2670 | -6.50982 | -47.59951 | 2025-01-29 05:01:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 864c9dc5-ce77-3d38-a83e-ffe414ea7b28 | -3.09282 | -54.5985 | 2025-01-29 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68e9ae6f-4f6b-3cd8-b0ce-707611b9c8c6 | -3.31867 | -54.91332 | 2025-01-29 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7801e214-f712-3c8c-9eb3-42d8e773eaec | -3.30703 | -53.86261 | 2025-01-29 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f864c67-482a-33b7-9546-0a5c2fe65bc2 | -3.09228 | -54.60195 | 2025-01-29 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c744c043-1f0e-3da2-84bc-934c09a7e6f2 | -7.95168 | -49.7602 | 2025-01-29 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5a61087-4fc4-304d-941a-3ec657e05148 | -6.51066 | -47.59364 | 2025-01-29 05:01:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34bedc01-3345-3a1d-8975-abb056f1b059 | -2.91002 | -54.16168 | 2025-01-29 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 537d17d0-e3d0-38af-8a2f-6f471c07bf88 | -6.94869 | -43.5356 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bba20f95-8091-3d05-bb26-af38e3274cfc | -6.94285 | -43.52909 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0546d92b-f0c8-34d0-bab2-8612599534b7 | -7.9527 | -49.75712 | 2025-01-29 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f65b6ae8-a996-3b44-a3b9-bb139184a8df | -6.50007 | -47.48695 | 2025-01-29 05:01:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 749e100a-591c-31db-b501-a94c66162e0f | -3.45468 | -54.60892 | 2025-01-29 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5e2901c7-9ff0-30ff-97f1-88f93f00500e | -5.4587 | -42.92649 | 2025-01-29 05:01:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 56da383e-df12-3cc0-88cf-675da13868f7 | -5.4625 | -42.92333 | 2025-01-29 05:01:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2e1ade36-fca2-3a3c-ae2e-d2f36d47a323 | -2.90699 | -54.28958 | 2025-01-29 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d044b879-2d45-3c5d-a8f6-2f1d1bc2fc68 | -6.93552 | -43.53375 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dbeb8fe9-f818-38d6-9a40-904e6d7fb05d | -7.94764 | -49.76081 | 2025-01-29 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ab06183-cc82-31c9-9efd-2a569e41ca6f | -5.46619 | -42.92184 | 2025-01-29 05:01:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0bae5c5e-0690-3ce4-a3e5-b7b96011603d | -2.79832 | -54.3332 | 2025-01-29 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb9ceb09-30f1-3a9d-b5ba-dcd42f32ca74 | -6.93628 | -43.52806 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48e7ffd1-94d1-366d-a193-514d76a44565 | -3.5394 | -53.87654 | 2025-01-29 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2341e67a-733b-315e-9d08-338a02ca8a0a | -7.79661 | -55.02856 | 2025-01-29 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e831478b-0345-3a57-b933-446a2ba8bd69 | -6.51482 | -47.60041 | 2025-01-29 05:01:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdd3bebe-1bfa-3da3-a375-831030bdc035 | -7.94726 | -49.7595 | 2025-01-29 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 238bbda3-8f18-353f-95e4-97ab192117ad | -6.94795 | -43.54114 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8be9f86e-f977-3dbd-bd9a-d32ee998d4e4 | -3.31921 | -54.90988 | 2025-01-29 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46f6accd-9500-36da-bef3-bdf3b63c2e9f | -17.81391 | -40.14704 | 2025-01-29 05:03:00 | AQUA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 60ef1a5b-41b8-3d77-bcfc-9fa4a76e4f6b | -9.16974 | -62.38824 | 2025-01-29 05:03:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69657eba-fab0-37a8-8fda-0aac63af9183 | -10.21485 | -52.85659 | 2025-01-29 05:03:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebbbf99e-caa9-3d98-93ee-92db3f16e404 | -12.0822 | -54.58616 | 2025-01-29 05:03:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7b2e83c-e840-3d79-a614-d7469095f1a0 | -9.20087 | -49.47618 | 2025-01-29 05:03:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4cdf370-6c47-3139-8fe8-873a7c2ddcee | -14.32278 | -57.61125 | 2025-01-29 05:03:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e27ef285-adc7-3d0e-b476-0dbd4cd83093 | -10.84917 | -56.09229 | 2025-01-29 05:03:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3f2b798-d018-3a85-81b9-1abaad1435f7 | -12.89842 | -45.06926 | 2025-01-29 05:03:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc022ff0-0df4-3d36-9547-78cf8d2d21d8 | -9.23662 | -60.33547 | 2025-01-29 05:03:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7163402-c6a6-36c2-a601-c05b2070595d | -14.52732 | -59.97014 | 2025-01-29 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6155cc2-3062-30f2-b74f-a09790d1b235 | -11.61096 | -58.21223 | 2025-01-29 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a9ff9d5-657f-3e93-9be5-05686f2311e0 | -11.36189 | -53.93383 | 2025-01-29 05:03:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a6aa773-e9a3-30a4-8c5f-ba9b5d9028bf | -11.36548 | -53.93436 | 2025-01-29 05:03:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af772461-a43c-3a3a-9e45-dcb012306a1b | -11.25743 | -60.7917 | 2025-01-29 05:03:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff5c541e-afed-3acc-8ca0-8ccb371d9843 | -9.82676 | -63.56268 | 2025-01-29 05:03:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fa105f3-e669-31a9-b365-839ad793c096 | -10.21501 | -59.41042 | 2025-01-29 05:03:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ed16a9e-c394-3a63-8250-653521dd7d72 | -9.26047 | -60.31412 | 2025-01-29 05:03:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d1f74d6-d6b2-3c04-94ea-aca6f4fb6041 | -11.86482 | -46.94749 | 2025-01-29 05:03:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2996f5e-86ce-3647-ad6f-b0288d60ec43 | -9.16539 | -49.49804 | 2025-01-29 05:03:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22e66463-6d66-3906-b796-280728aaeb73 | -12.9045 | -45.06881 | 2025-01-29 05:03:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fbe9a7c-1aec-3dd6-9e66-0e5020c5f2e2 | -11.45661 | -52.92075 | 2025-01-29 05:03:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f260b2de-fed5-3aec-8a3e-cca2700c47db | -9.2597 | -60.31863 | 2025-01-29 05:03:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f93abe49-33cf-33a7-99df-cb263c02b98b | -10.10073 | -62.07882 | 2025-01-29 05:03:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bdb259e-05f0-3d61-94c6-e5e8b45b2ac2 | -12.89804 | -45.06805 | 2025-01-29 05:03:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a57d7a5-8336-342c-a087-bf137b1a635b | -11.13215 | -54.22234 | 2025-01-29 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3267591a-9529-369a-ad80-38f8eb7bdda9 | -9.17399 | -62.38902 | 2025-01-29 05:03:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca1c46dd-fa4e-3990-8c2c-92e269390102 | -9.19628 | -49.47547 | 2025-01-29 05:03:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c11384d-4a3c-31c1-a731-d77654e5ca54 | -10.18548 | -59.50066 | 2025-01-29 05:03:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e36fc8af-9e63-3ba6-a923-592f7c2bd9c4 | -11.80056 | -49.32344 | 2025-01-29 05:03:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd186d53-d90d-3d81-be97-e202b5ae7d32 | -10.09599 | -62.08182 | 2025-01-29 05:03:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bbfa970-0ab7-3572-91b6-d4afe533f53a | -12.90388 | -45.07423 | 2025-01-29 05:03:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f43c27d-cb5d-3b2f-8b82-3ed4980ae5c0 | -10.21568 | -59.40633 | 2025-01-29 05:03:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8246873-27ca-38da-8a4c-3c84ba91e698 | -10.2111 | -52.85603 | 2025-01-29 05:03:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43d3aa93-07b6-3080-8bd4-71d2c1989bac | -11.2537 | -60.79109 | 2025-01-29 05:03:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e473f8b-2412-3542-88ba-afe8f16625b7 | -12.39064 | -57.52299 | 2025-01-29 05:03:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1ad8e14-4aa5-39d6-9720-dff5ee7ac687 | -12.57126 | -57.73332 | 2025-01-29 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f623a430-78df-3399-8ddc-b7364c44d074 | -11.13921 | -54.22339 | 2025-01-29 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98625c39-3122-3905-affb-db07516c1000 | -11.45282 | -52.92018 | 2025-01-29 05:03:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bb3e317-6e60-3aaf-be6a-6374b5dd681a | -11.39205 | -52.93983 | 2025-01-29 05:03:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eba052c3-559e-3d3d-9357-913b0f723955 | -20.90741 | -56.54031 | 2025-01-29 05:05:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d8fb03c-30df-3d02-a83a-bff5420d69ba | -20.54777 | -55.84114 | 2025-01-29 05:05:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4d86e55-37fe-3e56-b50d-b9ce809ab18b | -19.80102 | -53.79576 | 2025-01-29 05:05:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c8bfa52-5302-31d7-8cb9-d4d1cf4021ba | -19.11325 | -56.22207 | 2025-01-29 05:05:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fe16ce8f-832c-3fa9-a0d2-d70fd2071fb1 | -20.90801 | -56.53611 | 2025-01-29 05:05:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c579a955-76cc-3a69-bb10-5a5084b94604 | -20.54716 | -55.84554 | 2025-01-29 05:05:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdaaf1fb-4fc0-383e-ba68-d236d7192879 | -19.80148 | -53.79208 | 2025-01-29 05:05:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c41abf9d-e1a3-364b-91c8-5e740feeab3b | -19.11384 | -56.21798 | 2025-01-29 05:05:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f44b2248-c8a8-35b5-9468-696ce051df95 | -16.2197 | -58.60892 | 2025-01-29 05:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 6c135315-7ec0-3138-9113-9e0378d4a9d3 | -15.64551 | -59.63679 | 2025-01-29 05:05:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5948dd40-5637-3653-a373-59bf287ece33 | -16.22027 | -58.60532 | 2025-01-29 05:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 74b87f7d-0078-342a-9a67-6e3530ab8fcf | -15.75035 | -59.853 | 2025-01-29 05:05:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b7aa849-129d-3904-91c4-594bbb88dfd5 | -16.22359 | -58.60588 | 2025-01-29 05:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e6d50c40-ca16-320c-ac52-bd142281d905 | -16.28182 | -56.78923 | 2025-01-29 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| be28a7da-89c5-3ce9-a89a-cabd0e0f2a24 | -16.11591 | -58.17208 | 2025-01-29 05:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| f7b9ab88-b88d-376a-b4f3-370725a60da3 | -15.74695 | -59.85238 | 2025-01-29 05:05:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3287e7cc-ec48-3d9e-ac46-44db29af049e | -15.66803 | -56.0751 | 2025-01-29 05:05:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| ec0caa4a-3805-35e8-a892-9d4b50f7ac80 | -15.63072 | -59.64192 | 2025-01-29 05:05:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README6.md)
