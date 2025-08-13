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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78ee6df1-ff14-32fc-ade0-893a74d9dfca | -7.2569 | -59.99962 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aedd1306-e21b-314c-b7ed-98ff4565d385 | -11.63714 | -61.63964 | 2025-08-13 05:29:00 | NOAA-20 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac65ab15-e197-3adf-8bfa-424b6f2cb838 | -10.30054 | -57.12525 | 2025-08-13 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e6a360d-d0d9-3ced-a2b0-b6fb3da4e893 | -9.82819 | -60.76 | 2025-08-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40913fec-3d8d-391c-894c-f5b3ccf25be6 | -10.00872 | -59.21407 | 2025-08-13 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6e48b39-5ecb-3cb9-864e-d6c21726902f | -7.254 | -59.99523 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dcf5e6d-1df2-3723-9181-2c3c1c35b1ca | -9.17015 | -59.67184 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ced5174a-096d-3e6b-ae8b-71b96e5c787f | -11.90012 | -52.53893 | 2025-08-13 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a62de756-eb1e-3b8c-a1e6-3be4e4ce9dc9 | -8.92983 | -60.72906 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c53af264-862b-3744-93a0-48ec2ee7283f | -9.37783 | -61.53296 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1ec61b3-e400-3d35-a8e7-ccd23d061620 | -9.18944 | -59.66624 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1694181-6119-3cea-8dce-44e8ebfaa303 | -8.91726 | -60.76574 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7498400f-bfaf-34d7-9f01-f67ffc03257f | -7.24236 | -60.00135 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c9971a3-31de-32cd-9192-78f70fd84358 | -8.10925 | -55.57262 | 2025-08-13 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e32cdbc-a801-3f02-8810-ca16bed65b0f | -7.27205 | -60.6271 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41c975a5-1fe1-3476-8317-17e8e33057d0 | -9.05788 | -60.64672 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e2dac2e-3219-3bca-a41d-2c63d0a1e422 | -9.38567 | -61.52679 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdf156f3-4c27-3720-837f-537ab4e2cce1 | -8.57846 | -54.71783 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07484854-a2ee-3be0-bda8-f2f4316d87a8 | -9.37557 | -61.52521 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a0459f0-454b-3d16-adec-61b73481dd6a | -10.04088 | -64.89687 | 2025-08-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e99411d-fdce-3c54-bfc3-bf79710e2c85 | -7.44933 | -67.73333 | 2025-08-13 05:29:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da69cae6-8c85-3fc9-a6a7-c7a4cf50bf96 | -8.9044 | -60.57805 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55750efe-eb92-3a90-afb5-e51513912602 | -9.18521 | -59.6699 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50644607-991b-31ab-b5aa-7f67ca46ab38 | -8.57694 | -54.71576 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68980546-3b91-37c6-ad07-c6f2965524eb | -9.05615 | -60.65815 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 868f9e63-7b55-368f-b091-5376ca5eb507 | -10.34121 | -50.81548 | 2025-08-13 05:29:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ee3c5d7-7ca2-3ddc-b24b-b281c6dd20d5 | -9.37727 | -61.53658 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b4490a5-1f90-368e-a4b1-360384f700f7 | -9.06364 | -60.6554 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ce86642-caf4-3af0-8b6a-7ff301e0a890 | -9.0573 | -60.65053 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3daa056f-a786-3b7d-9ee7-f1cd3f49ed66 | -7.45993 | -60.63586 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 244c8ca1-b554-3769-9cf2-e03578908895 | -8.92872 | -60.75974 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e56be38f-2c0e-332c-826a-f6c767c25ffc | -9.05673 | -60.65434 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d83349a0-cf9b-39d4-a28c-4eb8e6d8949b | -9.27465 | -60.76455 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b760ef10-9f5e-330f-81f4-d9e1ce4d358a | -7.25979 | -60.00401 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71bb0610-310d-3b20-bb03-f6df8dbc17ee | -7.45857 | -59.88912 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1801c02-80b6-316b-9f6e-044f134c0ab8 | -10.34125 | -50.81591 | 2025-08-13 05:29:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3a6df2a-7d3a-3f5c-8408-5cc5b781bccb | -9.27809 | -60.76508 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9715fffd-9a3b-316f-847c-ece160a04bea | -10.00498 | -59.21351 | 2025-08-13 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4948e441-39e1-3d13-974d-09e142d77aa3 | -9.19368 | -59.66256 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| feb0d1eb-31b4-38b1-842b-08bc016354d8 | -11.7181 | -51.60891 | 2025-08-13 05:29:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 022938f7-f99a-38f7-bef1-f8e328dd5068 | -8.10993 | -55.56787 | 2025-08-13 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38aabdbb-2961-3e30-adda-4e74faa4ab07 | -10.28998 | -67.27456 | 2025-08-13 05:29:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1de22805-60f3-33f7-835b-af357aa251e1 | -9.50882 | -62.3747 | 2025-08-13 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be328d94-0d3a-3df2-bc03-0b9c88de8b5b | -8.57615 | -54.72139 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f4b5efa-48de-3c77-b4fd-6b192cf3d858 | -9.17076 | -59.66765 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d142a74-72af-3014-83dd-79b1c9a1c52a | -10.0196 | -58.4352 | 2025-08-13 05:29:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4389235f-f571-3224-a4b6-bcfdf9846def | -7.46618 | -59.88631 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef55a1fd-f9a6-37a4-8c31-07c210b30228 | -10.34057 | -50.82146 | 2025-08-13 05:29:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dee89c10-ab4d-33bb-8bd5-4a4307e0c766 | -7.45708 | -60.63165 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87112819-6c9c-3f7e-9210-457c3b7de31c | -10.29625 | -57.12465 | 2025-08-13 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc98ff9b-a8cf-3808-bc62-c75bf89ca4dc | -8.12123 | -55.5547 | 2025-08-13 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c680a788-a144-387d-a763-2fc5aaafcaf0 | -7.2675 | -60.63391 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e10ba15-a982-3b5b-a888-89343ba999c7 | -11.7175 | -51.61393 | 2025-08-13 05:29:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a38a13c8-7c51-3ca4-92c1-133c06ac086b | -9.7754 | -63.5696 | 2025-08-13 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3c75001-a305-3145-a623-d5992d437f3d | -8.56707 | -54.71444 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b60ff05-b334-3a22-9053-78c5e1cfa2a7 | -9.06306 | -60.6592 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2bd3e18f-8a74-3b62-a92d-087f250021d7 | -7.40984 | -60.02176 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b488dca-54e5-327a-a315-6eea7d103ece | -9.38456 | -61.53401 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02a22fa5-dedd-3f8a-b31e-6bd3b0398e83 | -7.25282 | -60.00294 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0afb94c-e7d1-375c-97b6-af1cb3393013 | -7.45367 | -60.63112 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d867f9-0df4-34fa-880b-b31619574f17 | -7.26864 | -60.62658 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8a3f8d3-3d32-38b6-80e1-a699acd38fe2 | -9.1973 | -59.66307 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f9e61d2-ff5d-370c-9a7a-bdbac4590533 | -7.45797 | -59.89305 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5b569f4-0ac9-3319-a446-469a3907cafc | -9.71781 | -49.47854 | 2025-08-13 05:29:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ff27582-ea4f-3cf6-8cb8-66842d4dd055 | -10.75376 | -69.08782 | 2025-08-13 05:29:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e407f443-1962-3d53-8ae0-5b9f6ea233e2 | -9.71005 | -49.48415 | 2025-08-13 05:29:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff1db4dd-5697-3514-ad03-9afb62d501f2 | -7.45652 | -60.63533 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99a75bd5-c4ad-3449-ae70-02a912290f6e | -9.38793 | -61.53454 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e34dac4-bd1b-30b6-a47d-8eae72113efd | -7.45936 | -60.63953 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fc6cf0b-8be7-32a4-a229-4104988c9eaa | -7.45595 | -60.63901 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 534f7e0f-2404-3acc-8049-da646f359a8c | -9.27752 | -60.76887 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67f5194c-7bfa-3aaa-96dc-ae65f4232ff4 | -10.34775 | -50.81684 | 2025-08-13 05:29:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 941c5997-4d09-3f12-8823-c37e5b3c0639 | -9.47458 | -63.51777 | 2025-08-13 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e521f72b-5a25-3c27-9f2e-d404e7bc8129 | -9.37838 | -61.52935 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 529617a4-fd4d-312d-ba20-b8b335bd15aa | -9.21426 | -59.64836 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 43093a74-e2df-31b3-9800-840cd14a91fb | -7.26069 | -60.63288 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b6f0ec68-d354-3907-b48f-0076290ef44a | -9.05961 | -60.65868 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7935281c-6d0e-35ea-90ac-b163a42faa3b | -10.96569 | -49.57958 | 2025-08-13 05:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2967fbfd-f187-304e-9c09-f6f59ce0b9f3 | -9.50937 | -62.3712 | 2025-08-13 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f83074bc-a2ed-30f0-99b6-7c24009d3b67 | -9.47403 | -63.52127 | 2025-08-13 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43ab4acb-e66b-38d4-b2d7-03693de6f91c | -7.81802 | -61.32981 | 2025-08-13 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f076b41-b2bf-3bbc-8a1d-1f93c2f71aec | -10.34805 | -57.59786 | 2025-08-13 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 514c9569-75b0-31ba-9b28-b0f7e21eec8c | -7.44525 | -67.73263 | 2025-08-13 05:29:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c62441ba-1e00-3388-8f31-84b8c5cc7a66 | -8.93729 | -60.72632 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcacf815-7914-3c9b-a815-9bc417b86ed5 | -7.31912 | -60.61913 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab76da77-2f94-31f9-b8b5-b97b5e1e0193 | -8.57122 | -54.72075 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0cb6d5a-1023-3a4b-ae08-babcccd16a9c | -10.34181 | -64.468 | 2025-08-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08414a82-93f9-3f9b-a641-1462cc5f8f53 | -10.96645 | -49.57289 | 2025-08-13 05:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45233ec5-519b-346a-b004-f35b72b378d6 | -9.16923 | -59.66926 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2d61ec9-3343-38bd-8bf1-30d926d44a05 | -7.46558 | -59.89023 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e153c795-f0d9-371d-8fcc-490ac4142c8f | -16.3153 | -52.9201 | 2025-08-13 05:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| df44aca3-0ecd-326d-9068-b85d4e8c7310 | -2.9108 | -48.254 | 2025-08-13 05:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 55eb79e5-890d-3de6-aee3-340ae155ba77 | -16.28861 | -52.91275 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4254ac66-b642-3503-a3e8-880f8959fc0a | -15.09104 | -51.36264 | 2025-08-13 05:31:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25fb25bc-c84e-3f25-b578-04e59a1d4fba | -16.2939 | -52.92186 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dbaae18-1606-3629-89bd-8e382ffc0a86 | -16.29432 | -52.9177 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f41a96a4-26d8-3b46-a34c-65f82bb46c47 | -16.3645 | -50.60663 | 2025-08-13 05:31:00 | NOAA-20 | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fc2c3fc9-4951-35eb-9c70-99d6ac29c54c | -16.30704 | -52.91499 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e30bab57-ebb4-30fa-9b81-e96ae6c8137f | -16.40152 | -50.89573 | 2025-08-13 05:31:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6e27ebeb-c5af-3283-924a-3b0b4bf6c489 | -16.30661 | -52.91918 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README34.md)
