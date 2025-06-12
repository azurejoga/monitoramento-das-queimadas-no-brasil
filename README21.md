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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 150d5849-61d1-3541-abe5-fee8209912ca | -11.83883 | -60.9254 | 2025-06-12 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7d4b5bb-ef13-3302-996e-91a051455703 | -9.25376 | -57.54021 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6902195c-d943-3aeb-9750-7bef0e6e2ec2 | -12.52365 | -57.23488 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a047f4f4-9da7-3971-98a3-bd2addede6f8 | -8.67376 | -64.88426 | 2025-06-12 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39d02233-241f-3cef-89fb-c301e84a0e32 | -13.29368 | -57.07811 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d4c9c05-291f-3442-9691-735eec97be22 | -11.99341 | -57.20905 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cd32686b-519b-3296-9c29-5228c9e02f49 | -12.71202 | -58.03256 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82097dc6-7373-3338-a779-74cc4bc5c3dd | -13.89043 | -54.65285 | 2025-06-12 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| efcbdba2-3fe5-3382-a31f-8fc6306bcc36 | -9.25285 | -57.53406 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bbb958fb-f538-336f-adda-5e9fc3b3af2d | -12.71092 | -58.02517 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b21df8d-bc73-3fef-b9eb-37780863223f | -12.70931 | -58.03799 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5de585d-2ea7-367d-9553-0b93f1f5f8fc | -13.65503 | -53.9442 | 2025-06-12 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43e51d81-4fc9-35a5-96d8-8bbb4a4768fb | -13.29753 | -57.09349 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 269fe7b3-50f6-3b4a-9988-679c8649c66b | -14.03258 | -55.12583 | 2025-06-12 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5ee1b27-02e7-3647-a2c9-82b3c98d4281 | -11.77574 | -54.37956 | 2025-06-12 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa0b2009-54e4-3fb8-93f7-a86bb1e245a0 | -11.77063 | -54.37333 | 2025-06-12 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17fa9aa1-caa7-35ad-a3c9-23d4c123cc0f | -11.77123 | -54.36784 | 2025-06-12 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1e78d02-6d45-3a6d-9b06-9c28ec31d8cb | -10.87806 | -54.74781 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6d381f9a-cd2d-3006-81f2-699b2a8e90e4 | -10.80977 | -55.87337 | 2025-06-12 05:44:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc3ccd29-686c-380e-a277-aaf2ce713755 | -13.71491 | -58.67939 | 2025-06-12 05:44:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5633be21-33e4-302b-983d-558d6f03d773 | -10.36687 | -57.23378 | 2025-06-12 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b12dac0a-0d32-34eb-8cad-3309804fbbec | -11.76992 | -54.37336 | 2025-06-12 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a10e1a6-8dda-3a7d-bef9-91aef6b3fd21 | -12.52407 | -57.23131 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b12a3de7-9fa5-35fe-95a3-345204d50941 | -11.99382 | -57.20557 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b4ab714a-c180-320b-bd16-3867f8c8a4c5 | -11.99838 | -57.21337 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e5471b7-31a8-3785-bd5c-57dccb067372 | -11.85934 | -62.7664 | 2025-06-12 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34ac33b6-211a-35f3-875f-282767041237 | -10.88256 | -54.7472 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cfe40129-45c8-37fd-b1f5-ddc1a6686add | -12.71163 | -58.03582 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21c4647c-8fe4-3416-a018-11bd420fd018 | -13.89159 | -54.64172 | 2025-06-12 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 47c37f3e-2dd7-379a-b2dc-f53b46366357 | -8.67321 | -64.88779 | 2025-06-12 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9012001e-21a5-3d82-a9cc-864ecc4e9e3b | -9.87758 | -61.4024 | 2025-06-12 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a5111db-c066-38ff-a5dc-b62a30a63af0 | -13.90338 | -54.65503 | 2025-06-12 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a74a3f96-3d4b-368e-9e86-83a22d0f2c3f | -13.89869 | -54.63693 | 2025-06-12 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 88c743d3-3af7-370e-bba1-4053b0a4e98c | -11.37653 | -55.11248 | 2025-06-12 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cafd8a2f-b314-38c2-90c8-a32975762809 | -11.83517 | -60.92088 | 2025-06-12 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed4838f3-5c9f-3834-aa92-524ed2618590 | -13.28942 | -57.06618 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 454bbac6-1cee-332d-9cdf-24ab2a0006a7 | -9.39235 | -57.52575 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34f983c6-2ef4-3ac1-8700-d95efdeb575b | -13.89217 | -54.63619 | 2025-06-12 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 499f434b-8c0b-3e08-9130-5a4506040fc7 | -10.94751 | -55.31417 | 2025-06-12 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f15c4469-28d8-3b74-9d13-b426bcd0fa9f | -9.87832 | -61.39725 | 2025-06-12 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b9eba1e-2161-3a9c-920d-7a1e330727e7 | -10.87747 | -54.75266 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 00f15141-93b5-35ef-99e9-ea709d60cccb | -12.51739 | -57.24118 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bab34171-bdb3-361d-90a3-8048c1a4a86a | -13.29282 | -57.08554 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fc54a9e6-f729-3b30-af68-5e2d23fd401b | -12.52323 | -57.23843 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81e14215-95d0-3d62-89e1-a257312eb74e | -12.5178 | -57.23769 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e286da7-71f6-3aea-ba8c-4fb55da19bb6 | -11.13932 | -53.94502 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4dd805f-ae82-35a2-b668-fe3a9e9f6155 | -10.36646 | -57.23279 | 2025-06-12 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06baf244-e61f-3702-82a0-561f0dabcc1d | -10.36687 | -57.22947 | 2025-06-12 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ca831f7-2752-3f56-af05-b2f3246ced61 | -13.47088 | -56.85951 | 2025-06-12 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcd44e10-04f0-37b1-b06c-973deb9362a8 | -9.24739 | -57.53623 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3605f11-4093-3942-9d23-13d0c0ccf81f | -10.8831 | -54.75848 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3e6f2562-4052-3a3a-ab6d-72152563ffd8 | -13.89809 | -54.64262 | 2025-06-12 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6bc86213-941c-302b-942e-6ba9dcbebabf | -12.71054 | -58.02826 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| af17f9fd-7e79-3efa-b4a9-6fd3052a4aa9 | -8.67043 | -64.88374 | 2025-06-12 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40f471bd-1fb3-343a-8af3-16ecc760f08d | -9.25459 | -57.53413 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e30dc70-2070-3412-8ff3-c69154559d4e | -13.29325 | -57.08184 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 25a51a9d-f499-362d-b0e5-367b56958af3 | -10.88429 | -54.74872 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 234fde48-ee50-3379-aed8-a90f13f09f9d | -12.36533 | -64.23112 | 2025-06-12 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ef7987f-1445-315a-acb5-a7b7c1b51f18 | -13.28854 | -57.07379 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f141468-478a-3c6e-98c0-554519954e23 | -11.83465 | -60.92478 | 2025-06-12 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a9bbfa7-0caa-3551-9bf1-4c0627dfeae6 | -12.70538 | -58.02748 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ffdbd621-86eb-3957-9057-91178f542240 | -9.18043 | -61.86414 | 2025-06-12 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4177772a-391c-3fbf-822e-f66405fbe87a | -10.8837 | -54.75358 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3c42dea3-d122-3ca2-959e-c403b8a8b241 | -13.6618 | -53.94502 | 2025-06-12 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee6d9f9c-2675-3e20-9b0f-42a2fcb9b714 | -10.36731 | -57.23047 | 2025-06-12 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c69ebef2-a2a3-3b2c-9197-61d7fa55722a | -11.85868 | -62.77098 | 2025-06-12 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b57a643-67ec-3ea5-a0df-f2ec0d58505b | -9.25207 | -57.54015 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a523b9bd-b738-3b0a-9d46-a30d5c1ad8fc | -13.29197 | -57.09292 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9779c515-d1bd-38c6-8440-ff163cf0c03f | -10.30341 | -57.14149 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac878b2e-19c7-3c7d-9c52-8dc418314d0f | -9.39274 | -57.52275 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f78ff85-e35f-3755-80a8-6a23e94c36e2 | -9.24777 | -57.53327 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c58b041-2805-3619-962a-fa181596bc21 | -10.09662 | -64.96198 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bac2e70e-a073-3762-8600-0ca17ce4de22 | -10.80398 | -55.87245 | 2025-06-12 05:44:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a036e9a9-0371-3886-a054-f0137c2ee08a | -14.04416 | -55.13773 | 2025-06-12 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71bcc764-0ccc-3fa8-82ff-883e560e7634 | -11.77056 | -54.36788 | 2025-06-12 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8027a75-f235-3c87-b5fc-d48c49b25636 | -12.47106 | -58.47216 | 2025-06-12 05:44:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e335eac9-8092-372f-9285-f808105e9a31 | -12.13945 | -54.66634 | 2025-06-12 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57a7a8bb-9d3c-3b4b-b7c2-ab876d0ed912 | -9.24911 | -57.5363 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9d54ab9e-a758-35b4-be97-4c723fb2e750 | -12.71013 | -58.03147 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67ba98b4-e6db-3eec-a02e-6b9022426c1b | -10.87577 | -54.75113 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 079338d0-7791-37c8-baaf-0d810f292c50 | -10.882 | -54.75206 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a11ffdb5-6456-3b21-b2da-15467d9350f6 | -10.88933 | -54.75932 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abc1f8d3-8567-38a2-9d74-2b9d567deea1 | -9.87437 | -61.39662 | 2025-06-12 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22116007-bb7f-3878-8b2f-03956cfd6001 | -13.29239 | -57.08923 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a87bc8b4-7ca1-3485-b68f-38a20d3bc160 | -12.71125 | -58.03907 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a0d4ed6-c710-3d75-9e41-087292be5362 | -13.89102 | -54.64725 | 2025-06-12 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5d88f68d-af2d-3d4d-972d-8f8996da9f80 | -11.76928 | -54.37886 | 2025-06-12 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2db116a3-d37e-3d5b-b1ae-82e4688bca52 | -12.70498 | -58.0307 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bca8c797-dafd-32cb-880a-f99e27119e5d | -12.43328 | -54.87065 | 2025-06-12 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21241aaf-9687-3256-b252-3be4f8c50df9 | -14.67889 | -53.36245 | 2025-06-12 05:44:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b373e279-d11b-39e5-ba44-307b42dc2a68 | -14.0378 | -55.13729 | 2025-06-12 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ec61bf9-2f91-3849-a80d-89cc84e08e0f | -14.67825 | -53.36895 | 2025-06-12 05:44:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 373cf415-15da-33ee-9231-21e5b7556d4e | -13.29795 | -57.08983 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f32d7f8-71f7-3021-a40d-883e5b911b64 | -13.29411 | -57.07433 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cba03e9b-fd6b-3709-a7c7-582e3c98f41d | -9.25418 | -57.53716 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ecf138e7-cbce-3e8d-8003-c4965668f56b | -10.94696 | -55.31885 | 2025-06-12 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5ced5c7-aa5f-3d66-ad00-f4365bb39b4c | -13.8969 | -54.65402 | 2025-06-12 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 46eac194-bafd-39fc-bb8d-884db3e97b91 | -12.14007 | -54.6609 | 2025-06-12 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b16f6db-0546-3935-806d-52f1cf84f70b | -10.95244 | -55.32423 | 2025-06-12 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddfe324b-edb0-3bc9-bdbe-f0b84127ad79 | -11.83936 | -60.9215 | 2025-06-12 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README22.md)
