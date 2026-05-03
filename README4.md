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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7243193-78b2-3ba3-b29e-e3e050d85545 | -13.21693 | -54.54052 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bcf53da0-ae67-3115-b091-66ad09d55222 | -11.95566 | -43.96655 | 2026-05-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40d21ef3-626d-38df-8108-1c0a776d5b7d | -13.21882 | -54.53122 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4a07260a-6dcd-3eee-9236-65b564d6b889 | -13.21399 | -54.55497 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6d2d4ec2-12ad-39ee-b939-fff45597cd82 | -13.20991 | -54.54388 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ab83cd9-de65-3520-b70b-cc4ab91f4dfb | -12.28115 | -44.62508 | 2026-05-03 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6ce49614-0100-39e4-995f-87fa29598d97 | -12.38127 | -50.01927 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04ff7b14-9e90-311e-be48-e899ecb0781d | -13.221 | -54.5516 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 422fa7bd-e53d-3ddc-a33f-1926a01c99b1 | -13.20672 | -54.52851 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8e3c031a-6056-3063-bf83-8b51e6e5c099 | -13.21976 | -54.52659 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 281fa51a-d8ea-3905-b5a7-6e37c1b66932 | -9.5706 | -50.67999 | 2026-05-03 04:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdbdfdbc-810e-397e-9ac7-ae80fa4e259a | -12.36565 | -50.02644 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e6db38d0-171c-3a34-8497-6bb6a16dae27 | -11.88335 | -43.80235 | 2026-05-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9763b773-08cd-39c9-9387-79f30aae61a3 | -13.21184 | -54.53444 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 62a7a770-7691-3148-84c8-870f6f70a073 | -12.3799 | -50.02139 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af824399-7b5d-38b6-bc6a-8848bc795eea | -11.88889 | -43.81065 | 2026-05-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 656771f9-546f-31b6-9efc-06efc54f640c | -13.20578 | -54.53316 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f1670e6-2875-33d6-9c47-89b03213427c | -12.35462 | -50.03454 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8704b19f-0974-3b71-9f98-cf6d43dad832 | -13.21498 | -54.55011 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24891447-6fd7-36e8-8aeb-83e504ededff | -10.64038 | -48.00589 | 2026-05-03 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 42342639-3382-3686-b211-a21466b70741 | -10.98451 | -45.09119 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 074e765f-0ec5-304e-a399-73a3a53e4d39 | -10.98385 | -45.09517 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f3a65abb-9525-30e3-9536-c213ce7afb87 | -13.20065 | -54.52728 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| edb20255-1eb2-3569-85ac-15749638956f | -13.23071 | -54.53867 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9f1f8a3-10b9-3d1e-99a4-cf00177cee82 | -10.97682 | -45.09403 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0bea757d-f453-3abe-91b3-97b02707ef4d | -10.97748 | -45.09006 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 216746d9-72ad-37fc-9002-87db5fd08382 | -11.64181 | -52.56858 | 2026-05-03 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb86ed9d-9353-3810-9440-555895ceb5cd | -10.58726 | -44.32474 | 2026-05-03 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 614a82b2-9d51-3810-ac1d-393b06bd0759 | -13.20286 | -54.54743 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3375e795-34bc-3351-ab09-b4cf48452a52 | -12.36103 | -50.02555 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4d6133e2-261b-3594-9a6b-868b731b780d | -12.38084 | -50.04179 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39872dee-8b78-3820-b255-6ef346fc6aab | -12.46357 | -44.30053 | 2026-05-03 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed199344-73aa-3504-ad96-fccfface2050 | -13.22486 | -54.53257 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da4f0096-956f-35fd-944a-a3f37915f5ee | -13.24264 | -44.46408 | 2026-05-03 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da8aedb8-acd4-3370-b786-1038de64a168 | -10.97967 | -45.09859 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b6b5032d-ecb8-3f29-9858-743fd278413a | -13.22199 | -54.54673 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| baeb4fc2-72ac-33e5-8fd4-d8266b7344a0 | -11.84326 | -43.9664 | 2026-05-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7fdabf2-3e59-3e35-ab29-0f3881fc90c4 | -13.22899 | -54.54339 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3d81690f-ead0-3da7-8795-94b0a67d12b5 | -13.22296 | -54.54194 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 065c089c-a5a3-36b5-9131-cdec90b25976 | -12.36476 | -50.03135 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d2450d74-dc0f-31c9-98c7-bf281b325030 | -13.68388 | -44.29012 | 2026-05-03 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a87f30b0-8b0f-35df-9b19-c2f558323df1 | -14.83853 | -42.89598 | 2026-05-03 04:10:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71dae425-1d41-38af-b32c-5555c87f6fbf | -12.37685 | -50.04377 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c662430e-5442-3145-979f-8a2946439339 | -10.57981 | -44.32737 | 2026-05-03 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cdef63aa-2699-3783-b670-1b4b8919895d | -13.22392 | -54.5372 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4914adda-662f-3d78-a746-cd32d96ec82f | -9.67239 | -43.79211 | 2026-05-03 04:10:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef71dd77-498e-3a4c-8f7d-c6534fbebcb6 | -13.21596 | -54.54527 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 544199da-9064-33ea-ba1e-e2159d72e483 | -10.97615 | -45.09803 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 05196b92-611f-37b9-9012-57743dd3c54c | -9.57004 | -50.68301 | 2026-05-03 04:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dbe0628-bb4c-3bd4-8683-19d6a8f7bcd7 | -13.20792 | -54.55367 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40a0b945-6b96-33da-83b3-4818dbfd30e3 | -10.97548 | -45.10204 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd0739a6-cd31-3d9f-b628-6872921e9302 | -13.20385 | -54.54258 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 086c649a-259e-3317-b201-f7df2b9d2485 | -10.96693 | -45.08838 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b59f85f-75c7-3f1b-a894-4638a2a140e5 | -10.59006 | -44.32907 | 2026-05-03 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6f2b6ee-27ad-3890-839e-6bf1c58f1bb9 | -13.2317 | -54.53397 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e9751d0-301a-350e-a54d-c69fedc9bbda | -11.55617 | -48.27009 | 2026-05-03 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2187c224-08e5-3bf1-bb13-375416c920f6 | -15.4552 | -43.32571 | 2026-05-03 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 09d3d257-ce6e-3315-b1e7-1e12be228443 | -10.59348 | -44.32964 | 2026-05-03 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61f34005-6651-3c0d-b5e3-b6413b09b538 | -9.67578 | -43.79267 | 2026-05-03 04:10:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3fe4384-9fb5-3716-a8b1-3796f185c454 | -10.6484 | -46.36972 | 2026-05-03 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55ce3369-d087-34ea-b188-4de949e003c6 | -13.21278 | -54.52983 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc6b981d-3c05-3d06-9a67-f2c9b56009de | -12.35642 | -50.02467 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1836c119-5ccf-3ceb-a5da-963625a8e2ed | -10.7724 | -45.01277 | 2026-05-03 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a35df999-2609-31e5-87ab-c42b2278d9f3 | -9.67299 | -43.78846 | 2026-05-03 04:10:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a339acf4-f1e9-3952-8695-18b718bb645f | -13.23092 | -54.5339 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b4b2079-2566-3a29-8ddc-632edeca4b85 | -10.58323 | -44.32794 | 2026-05-03 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 3c456b7c-92f9-3708-a8c6-52db03dd0bac | -11.88831 | -43.81425 | 2026-05-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 096aabe7-00e2-3d9f-ab47-1790f5c91bb7 | -13.21089 | -54.53912 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| afe04ed7-42cb-3fca-acba-2540e30e84a0 | -17.4723 | -42.30024 | 2026-05-03 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61e15d85-5dd5-3efc-b43d-32fbb5cfc61d | -13.19969 | -54.53197 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5d7a852c-ffb3-3e18-aa31-72d57f3b235c | -10.98736 | -45.09575 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99582ab0-116b-3278-b8db-94b136d3632a | -13.19874 | -54.53664 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2a8e1d46-bc7a-3594-b84e-98d80f19f4f2 | -13.20692 | -54.55856 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d049687-00ec-309c-8ef4-88086b7d0992 | -13.11027 | -51.72628 | 2026-05-03 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7b31235-4c13-3e65-9204-1dcf0a3966db | -11.8773 | -45.22416 | 2026-05-03 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34e4dfb7-9736-30fe-bbbe-523a30434f36 | -13.7977 | -48.23942 | 2026-05-03 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49218975-5904-3c50-84b5-763604946c39 | -10.9867 | -45.09975 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa802bf7-b14c-3cf3-957b-e4003f51eebd | -11.88554 | -43.8101 | 2026-05-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5e6d1228-4fd0-3f5c-92a3-329db149760d | -9.6696 | -43.7879 | 2026-05-03 04:10:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24503fa2-c700-3dc4-a616-6611791ff59b | -10.57638 | -44.32681 | 2026-05-03 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1a5dbf39-2088-353f-9314-50269648544d | -11.36027 | -47.0322 | 2026-05-03 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e6de689-17e9-3e5a-b9d5-340efef0a34d | -10.981 | -45.09062 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 036dff43-0830-31c2-859b-d9050af4017d | -12.36014 | -50.03048 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 49253138-6928-3c07-a70f-43b62911e46e | -10.58664 | -44.32851 | 2026-05-03 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| cfe6e93b-eed9-3e7e-9d80-f5ddb1c914ca | -13.21788 | -54.53583 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6e82e04-b5dd-38c7-8a78-cf24b23dafca | -22.85236 | -43.52496 | 2026-05-03 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a7987cc4-2ac9-37af-a812-37f21aa113db | -17.94743 | -52.98805 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0b9d0e61-3508-33c4-ad0b-1c95938d6195 | -19.03636 | -40.53213 | 2026-05-03 04:12:00 | NOAA-21 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4527f5fd-a2f7-3a9a-a5d8-b5d40346b7e3 | -22.61461 | -46.98138 | 2026-05-03 04:12:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2706d525-fc80-3960-8aa8-d9092a09f82c | -17.94679 | -52.99112 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0898f6d2-f9ea-38c5-acbb-91140bbe2083 | -21.1593 | -47.98697 | 2026-05-03 04:12:00 | NOAA-21 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7ead6a31-4d23-34e8-b6a6-acc91f45b987 | -20.26972 | -46.44791 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 387099da-7c95-3aa7-b740-e6ab3a66bdde | -20.18764 | -46.45362 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abf3caeb-f7e9-313c-894f-47a84a8c649e | -20.18337 | -46.43717 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a20d0abe-1f72-31f8-ad66-aa8a4565ec02 | -20.18422 | -46.45312 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4cf85c9-7bbd-3588-b9e7-e9afabff0b6d | -17.94616 | -52.9942 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e06ccbc3-9ab7-393c-a55b-7599bc6d1458 | -20.26699 | -46.44333 | 2026-05-03 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a69cfff0-eccf-39cf-8428-81616e5998ec | -18.25399 | -51.26408 | 2026-05-03 04:12:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46304e2e-43c0-3d29-a0e1-f0390a913355 | -17.95183 | -52.99229 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3cdd7ae0-10b2-3fd6-9a19-302e898e81fd | -17.95057 | -52.99846 | 2026-05-03 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README5.md)
