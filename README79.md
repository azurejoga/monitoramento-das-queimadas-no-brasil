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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dcb9339-63f0-34f3-b622-6a0c126b5097 | -9.14886 | -59.45743 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0462c47e-075c-3ff8-ac6b-fdf85efc02dc | -9.10489 | -61.4293 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b55f2fc-28b8-34e5-88b6-c08add98cc53 | -9.20168 | -59.47697 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b20d65a-89c8-3b21-bef4-f09d6c56f274 | -9.04565 | -65.72556 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b8b98aa-76c8-37a1-8461-d950ea5d5e01 | -9.50746 | -60.50882 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb5a344a-3bcc-3de9-8cbd-362f625e24f8 | -9.16024 | -59.47437 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3521d39a-c9fb-3a4a-9943-11f704cdc076 | -8.92299 | -62.44012 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a26ef12-cbaf-3171-859b-f4dd0a9a2385 | -8.8995 | -62.43629 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f10d971-02a2-35d3-9ffb-ca002d2b2152 | -9.1996 | -60.78379 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0860f493-8969-3b32-91c4-d279b5a48b0a | -9.15058 | -59.4691 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 52fa9e23-b866-3325-800d-999f8de8af90 | -9.17342 | -59.59335 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66bc7b41-c354-376f-9bd8-eab67467e092 | -9.01022 | -65.69906 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ddb2e3e-2f28-334b-b7b5-44c14a5518e4 | -11.186 | -55.03064 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 334c1401-9989-32a7-938f-350d3c53012b | -9.16607 | -59.59595 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78969962-b243-3204-a749-79af4145d354 | -9.17158 | -59.46854 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ee50c4f6-a2f5-3798-9097-f884a5445043 | -15.67773 | -53.87593 | 2025-08-24 05:25:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ef60ae7-0a63-31de-9c16-789e1b1a9e0a | -9.16485 | -60.81053 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 918b1b25-57ec-375f-b2e8-6c332d31ba43 | -9.17471 | -60.76911 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af40484f-7df4-34d7-a3d6-14248ae62bf9 | -9.94666 | -60.16859 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4861af6b-0878-3005-a335-c19eaf07434d | -20.34665 | -51.68539 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0a865131-4b49-3fb7-a1e1-f7b34fe3314f | -9.19372 | -59.46059 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6675f3b9-3072-37d6-a844-3a92ceaa9226 | -9.5131 | -60.55656 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b9ccfb1-9c3b-30e3-bff2-b38d06b3e187 | -9.15459 | -59.48861 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53728532-2a36-3d86-855e-57f999072906 | -8.90285 | -62.43685 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51c7d1ff-0143-3284-8f5d-7450d320fd17 | -8.90783 | -62.44871 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca5139af-1251-3025-ab5e-b5268c25e3a7 | -9.67614 | -65.71301 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ee9f6a0-1e09-3bdc-8e22-c8553627bb5e | -9.14778 | -59.48755 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9927f5ac-6cdd-34dc-96ba-5e0c79ab1a0d | -11.33329 | -47.84967 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfa8cab7-a6e4-3820-bcb2-f563435833e6 | -9.63295 | -63.10059 | 2025-08-24 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db2a9867-cf13-374c-868d-d02b96d6364d | -9.15683 | -59.47385 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cee0b330-ee66-39af-afe5-0b80e646b1be | -9.23509 | -60.9254 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f5edf6eb-0092-3ac2-909c-1dd13d9be6a2 | -9.62655 | -61.45934 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f30c4fe3-f652-3e55-ae6d-71cfaaac4af6 | -9.05426 | -65.72195 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 271a04ff-2b01-3d02-aab3-d803805903a3 | -9.52248 | -60.53997 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e4e8f7a-4ae2-3c4b-ae71-2fc1fbd0cc52 | -9.19515 | -60.76877 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aafeb368-85d7-30de-bede-1731eed36bcf | -9.20792 | -59.48172 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c578d708-1147-3de8-8d6c-e24db40af387 | -8.92357 | -62.43652 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8acfad53-e6bf-313d-aaac-5042fe01c804 | -8.90208 | -60.55764 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 358f2336-8433-34f9-a498-76e7aa6da00f | -8.89001 | -62.43107 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c691deea-e56b-3d18-af64-dd64bfce6b6b | -10.34916 | -58.60168 | 2025-08-24 05:25:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dee6c979-b42d-3f56-a49a-aa660a29c5a5 | -9.4549 | -63.50786 | 2025-08-24 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc25870a-96ad-3837-bc62-98982d43d4b0 | -9.01713 | -65.70531 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0959148f-7cd7-3a7b-8ca2-6ed6608acbe2 | -11.54832 | -51.90989 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fd9da08-a678-37f6-8da6-96c7d189c347 | -8.90298 | -62.41478 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89198111-fc28-364f-bde3-41603e9ae1d3 | -9.15511 | -59.46221 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b99666a1-b813-3518-b9ab-e807df8428a3 | -9.23718 | -60.47699 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb6b1867-f82c-3c1c-ba09-d425c38b258d | -8.60661 | -62.59285 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7f1b6b8c-12a9-3ab1-83a8-52fb9b595b29 | -9.19378 | -59.61908 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 583e1ae3-c017-3bb2-bb5b-9406f4d3810f | -8.92779 | -60.71942 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34e72a2d-71ec-3279-a03e-83949b2a6eec | -9.15743 | -59.49284 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e2d5a3d-7a2f-3f62-9816-195c7e3ce996 | -8.91233 | -62.1063 | 2025-08-24 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23dbbe42-eb65-3461-899b-79ae21c4daef | -9.19461 | -60.77226 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e661cb0-9cec-39c6-a546-a50ff1be7dc7 | -9.9562 | -60.19589 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caa109a2-d1c0-398b-92cf-c8f8a14f18bf | -23.10673 | -49.98339 | 2025-08-24 05:25:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 4c2e608d-180a-3214-8c40-1597026aebd6 | -9.24835 | -59.63079 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bf6a435-dcd6-382b-9595-956b2a3b0b3a | -9.15062 | -59.49179 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b982e886-1489-3cf8-8af0-ce8b02677634 | -9.00279 | -65.69029 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6985abae-8c52-34e3-9b8f-0f8630284f35 | -9.16649 | -59.47913 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4827ea32-6a7e-3814-b60c-92264b5c0cbc | -11.32887 | -47.85521 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bedbd1bb-111a-3efc-9f01-e294b51f7295 | -11.53022 | -51.91882 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ce26e2a-c91c-3d2f-80de-2fc899c16490 | -9.6482 | -59.64969 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4dd976de-74a8-3acf-86a2-8063e8bdd997 | -20.35878 | -51.69144 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| af6f0582-cf87-3d1d-be8d-5584df28994c | -9.15006 | -59.49548 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db782d1e-2a2e-3eae-a87c-c3700b34cb73 | -9.16874 | -59.46431 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 446af3b6-1162-3253-a059-9bb25f53825b | -9.50691 | -60.51234 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aa8bf1d-8419-3d35-93ed-fc8bf15d1c62 | -14.79708 | -59.63121 | 2025-08-24 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 131ea043-9c7b-3a7e-b3dd-23f46102dfe2 | -9.17952 | -59.4622 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22af1469-d918-3156-9017-35aceedd261c | -9.15567 | -59.4585 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e9a0a4bd-07e1-3018-8f35-661e917777a6 | -8.60999 | -62.59341 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 44d6cdd8-7300-305f-9ad7-0d4d3aa0531c | -11.17946 | -55.02739 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00af7095-864c-3c9b-8737-7b9f9f425004 | -8.89627 | -62.4137 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da984ecd-300b-3a06-ba47-23f51c116726 | -8.63571 | -62.62745 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7a6943f-19a5-34d9-8eb6-bae0f7408842 | -9.80523 | -61.20941 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0280b7f4-c879-3982-848f-1c878c916436 | -9.18349 | -59.45901 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e5e44de-bf11-35a8-8980-ff3c956649ae | -9.24439 | -60.47451 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adec37cb-d647-358e-8f17-9f438eed8489 | -8.89963 | -62.41424 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2776100d-9921-3fe1-9124-65eaa5099992 | -8.6655 | -62.66593 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b025cf5-33dd-3475-9b80-7a42b45bd337 | -8.90111 | -62.44761 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d47b435-cbac-3c5b-a1c1-f556b5d2b42a | -9.80137 | -61.21237 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d6681ed-46d7-3061-bb90-9030ad18ff81 | -9.16551 | -59.59962 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbb04f46-c464-3dbd-b695-f796cc94c25e | -9.19792 | -60.77278 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f5350cc-ccef-3284-977f-88f676f8b55a | -9.02707 | -65.7173 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a30cc88b-3f54-3975-a828-a43c802b48da | -9.26504 | -61.01588 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 727421a5-6619-3583-9261-a16b9af73ec1 | -16.39448 | -49.64618 | 2025-08-24 05:25:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f04ef9f1-3cd2-38e2-9e9d-2d3bbb68beca | -9.13653 | -60.77417 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13a9ff15-7e56-3e15-88be-d9d410212497 | -8.13505 | -62.86366 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60426bee-fe36-35e6-9739-5a539a796fd2 | -9.24889 | -60.92402 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1471edbb-40eb-3833-80fc-db2032269a5f | -15.29779 | -56.15605 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6a27e197-baf6-388d-a7c7-94cd0e04324d | -11.18455 | -55.02348 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ccaa001-c7c2-3d2f-963a-e9455c6039af | -20.34524 | -51.70118 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2121dff1-0474-3b3b-a17e-422d6bca4fd7 | -8.90853 | -62.42305 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b91fb957-28c8-3ca7-b92b-76620bef2249 | -9.01798 | -65.70039 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be01f0b6-6850-33a8-a13e-722d8d421008 | -9.20452 | -59.4812 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 892a1042-dd11-3752-88d3-7657922d6b71 | -8.68826 | -68.68974 | 2025-08-24 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b22015c-d23f-3ab5-bb58-2f35e7a8f0a4 | -15.32401 | -56.15754 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 662ab52d-ebd8-37ca-9c52-36429faa7601 | -9.51964 | -60.51424 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7510becb-becb-3e9e-aee0-ddaab52c001d | -14.79474 | -59.62223 | 2025-08-24 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0e7a4f3-12ab-37ae-95b0-c4ba2cbdd1dd | -8.88915 | -62.40196 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb3ee7b9-4380-3cff-9a43-bbaeec69a9d8 | -7.80832 | -63.56133 | 2025-08-24 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 059e953f-a4e2-377e-9f68-ac93822a6e5c | -10.60866 | -55.41338 | 2025-08-24 05:25:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README80.md)
