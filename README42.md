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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e481fc7e-5fde-309c-8538-fecc5cdd1993 | -6.1445 | -42.80221 | 2026-10-02 04:14:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| dbb3a9ef-e39a-3070-8deb-44cfee605e27 | -5.00167 | -47.45221 | 2026-10-02 04:14:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc294820-be9e-3f5e-b327-e170104b0505 | -8.21643 | -55.09747 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1418a87d-98fa-364d-8685-2b807e3205f8 | -7.82436 | -55.12983 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12c2303f-b30a-36bd-84cc-a58dbbfdc8fb | -7.62657 | -55.05494 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f74ed63-a284-34c3-bfcf-1b8badcb8adb | -6.14617 | -47.26929 | 2026-10-02 04:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b59ac91-4ad3-324c-bc3b-35e60ee6b961 | -7.56361 | -47.20971 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03842052-fba4-3c16-925b-318ca1e391c7 | -9.82636 | -44.81648 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d06412b7-d4fe-3dd2-b6ae-deb681e5602f | -7.81885 | -55.1219 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bbb328d-ea8e-3447-9150-3534e88d2cfc | -4.89151 | -48.3763 | 2026-10-02 04:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c56420b-11fd-38a5-92cd-143dd585d25f | -5.72741 | -43.51826 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27b4497f-8edd-3b9a-8e13-161b486a9b5f | -6.21118 | -53.26159 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e412e70f-52fe-35a3-87fc-20a2dcb1750e | -9.84462 | -44.83548 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 577ea05a-00dd-3254-8039-a365f6bade03 | -2.8776 | -54.8818 | 2026-10-02 04:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41285881-7c66-3980-a29c-942f24a80395 | -5.48337 | -45.86508 | 2026-10-02 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47608c63-0f81-323f-82f5-d1dc6135e871 | -4.04212 | -54.23764 | 2026-10-02 04:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84a4b85b-2f98-3ff5-aff6-5d8eba23a0ba | -6.91027 | -43.68563 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2137422b-7159-3045-aaf2-485182c13aff | -9.83201 | -44.82543 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b5fde82-85f9-3c44-8e0f-7d637bfe4069 | -4.25204 | -50.74785 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4434b343-f67f-3faa-8fe4-130bad09dc99 | -7.40599 | -55.59782 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db73bf65-9d9e-34ed-8ee4-207c1cf0b798 | -5.87043 | -50.15885 | 2026-10-02 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c833c2d8-faa3-3cc2-8dc3-40cecfc22f98 | -9.84334 | -44.84326 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2816941-7c7c-325c-8de0-735dae1c768d | -9.21158 | -45.7752 | 2026-10-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 754f40d6-bea4-32b7-b3da-4eb36e10b8b1 | -7.83691 | -55.14561 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fde1673-2b9c-378f-a2f4-59a68ae70a49 | -3.03267 | -53.87313 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db2107fb-cba8-301f-85dd-bef25fa6936d | -6.08551 | -47.67479 | 2026-10-02 04:14:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c15f3b5-f1a8-333d-8e08-f57da1fb9714 | -6.70547 | -44.8358 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36099f26-f932-3755-b934-8c34f79304ff | -5.99673 | -53.55117 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92ae4fd1-5078-3000-8b24-e2a579101223 | -7.83231 | -55.12485 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 112edb9c-0e96-3b45-96de-a6afe1f444cb | -7.63447 | -55.05035 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7700e76-8e9f-3481-b70c-d8a97f86b0fb | -11.66 | -43.58 | 2026-10-02 04:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3502ef02-8ab5-357a-9f13-59a99c89fe46 | -11.66 | -43.63 | 2026-10-02 04:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3096a59-87ba-3835-9a22-2f64e1b52b52 | -11.15 | -44.61 | 2026-10-02 04:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d4c9923-048c-382c-9fae-abc52c6fc5a9 | -11.65595 | -43.60891 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a53f6be3-8e3f-39a2-85c8-19747215c11a | -15.15115 | -46.12029 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffd51700-0d8a-3f7b-85dd-b5afe5911c73 | -11.76791 | -43.5472 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edc8fac3-e32b-3be1-98b5-324be6fa0705 | -10.30573 | -44.63546 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e6c776-5757-358e-af88-55c1edf67686 | -11.43072 | -43.40491 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66e71084-fa56-3788-87a1-c5c19682900d | -11.21212 | -44.84098 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25ab60f7-2983-3265-836f-4b30e32c3a34 | -12.98914 | -51.28717 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 5e4980b5-8304-3f49-bac5-364c0ee20b46 | -13.34149 | -43.86222 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad61beac-bf1e-35c0-b179-fced83547244 | -11.14654 | -44.60263 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0bb5aa82-c093-3929-96c1-81ca9da863c8 | -11.77722 | -43.57404 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6812a94-a6cf-3f3b-ae32-a624f9fbe03c | -11.5109 | -43.49767 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ded86bd7-5bb3-3ba8-8e2a-bd1be1b47fca | -10.81616 | -51.09444 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d36a8ad1-8ae6-3fc7-895e-06221041d406 | -12.52057 | -43.06727 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9286c608-6f46-3527-9e72-3fd1d4af7172 | -17.70924 | -39.75572 | 2026-10-02 04:17:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7c45a3f8-edb8-338a-a07f-7b09fbecfbb0 | -10.82061 | -51.09835 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a94eaa6-d56d-36d9-af7d-c9677a4540db | -12.52716 | -43.09003 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f6d35236-dfb4-3c7e-b71c-e6b5b4c5471d | -10.91545 | -43.84138 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53afe267-c80f-3cc7-b7c3-d714314f5192 | -11.14252 | -44.60578 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9a23a199-592d-3483-98c7-4a34f92bc4df | -12.78042 | -47.2773 | 2026-10-02 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46c2b481-2c75-3af5-bd1f-9aec2840a18e | -11.94083 | -44.80742 | 2026-10-02 04:17:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1fe559eb-e8bf-3a9b-b9b4-56d8a411a5ab | -11.42409 | -43.40382 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a564cba-a8db-35fa-8cf4-83aa136bcf40 | -11.73897 | -43.57869 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 677ffcfd-c4be-3edc-951d-16e0ca36b8f6 | -11.73133 | -43.43644 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c98267a1-cbbc-3bc7-9f1a-af9d0bc3c438 | -11.77446 | -43.57001 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cce2d7c8-0a93-3c6e-9e3c-e93d43cd11d2 | -10.21593 | -45.30729 | 2026-10-02 04:17:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a1268ed-4644-39fc-8e33-0fbc1c2edc2b | -16.51948 | -46.8649 | 2026-10-02 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a419cd9-cf44-3d44-b3a6-f4737e52b3e6 | -9.33457 | -50.99521 | 2026-10-02 04:17:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6200f6b-1e18-32ac-ac77-49c6ad5f8690 | -11.14128 | -44.61326 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 16f24c8f-6742-304c-94ca-a72479881c98 | -11.7944 | -43.57319 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ac903c2-b4eb-365b-bcf5-cb4c14c02fec | -10.25178 | -49.67043 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6b1b26b-8113-3948-a8ef-e6f8e682e3bd | -12.5205 | -43.11063 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d12a8171-43d8-39a5-9993-2d65a3145c45 | -11.77673 | -43.55591 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b1daa94-70ca-3ab3-915b-7a6f676284bf | -13.86081 | -43.63235 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5acd2ba0-6a04-3f29-aae1-1d43032ed1aa | -11.4355 | -43.52145 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1da0f3ba-c7f6-38cb-9231-1850320b09eb | -9.78162 | -53.83212 | 2026-10-02 04:17:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a1b22a83-0c17-30dc-bef3-bd78b956f8dd | -14.04322 | -43.85172 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b15bb2f1-00ef-33a4-89e0-5156ca18c57d | -10.2509 | -49.67522 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40ae6b45-0489-3f54-82f6-28bb9192b81e | -12.54878 | -46.799 | 2026-10-02 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4323e4c1-5d78-37e9-85f6-7e499357adcf | -10.90542 | -43.83972 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc6114db-3791-30f3-bf63-e27062b6772f | -15.11576 | -43.62159 | 2026-10-02 04:17:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8bdb2020-41c4-3e57-8244-2adad2b2cbc5 | -11.76223 | -43.58244 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3da01a9a-f111-34f1-b1a1-fa8fca84d848 | -11.52135 | -43.51752 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b00e097b-39f3-3cb1-b386-4acd04316c9e | -11.69088 | -43.60377 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 601109b0-0e8a-3ee3-89bb-1e8900c8be78 | -11.73352 | -43.44404 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33759cc1-48bc-35d5-8786-a15ba8bdd925 | -11.73309 | -43.57448 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5d5b45ee-4a41-3119-b6ec-d1cfec2d87d5 | -14.33505 | -44.73798 | 2026-10-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5462b6f-7c24-3291-b163-1fb21ceb1436 | -13.80059 | -45.25666 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb9fca51-a801-3a90-a4ec-e59f2409c12c | -11.34844 | -43.36604 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48f1e693-fcd9-3c6e-b098-d25a72788405 | -12.53267 | -43.09816 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df6aff20-f2ed-3e93-820e-765f1585a309 | -11.4075 | -43.40108 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43ac5de7-24f6-30ce-be7d-98344f2432dc | -13.51186 | -40.82368 | 2026-10-02 04:17:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8ce98566-e236-3207-bf0a-ecb93640a91c | -11.70198 | -43.59837 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2009cec-0038-385c-8e97-ef63fc4ce088 | -11.80579 | -43.311 | 2026-10-02 04:17:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78d6d46d-52a0-3b68-8bde-f8ce61030d4b | -11.77398 | -43.55182 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 355637a3-f2f2-3d56-9e64-4f5f4f339933 | -12.66869 | -45.09803 | 2026-10-02 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86608335-7fbb-3464-8ca8-fbe3d3890809 | -11.25117 | -45.22704 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ca6d0b3-cf00-38dc-9ee9-d02218ef05ef | -11.69899 | -43.5108 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 844dba38-3083-3360-82dd-2a05e2405811 | -11.68756 | -43.60324 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8059de0f-ad4f-3cf0-8597-f1797a77fba4 | -11.46467 | -43.42487 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ff62e22-a58f-3c6f-b402-38684627c331 | -17.22767 | -41.1999 | 2026-10-02 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 27bec8b8-00ac-3f4c-abc1-e6ed18474510 | -11.46629 | -43.43599 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f214159f-abe8-3eda-aec7-b315d71f2785 | -13.34046 | -43.84743 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83bff12d-7dfe-3999-a193-d44681712e94 | -11.68869 | -43.59618 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23564ee5-3085-3a81-987e-6eb1ac1a7e38 | -10.25001 | -49.68002 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f7eb629-9371-3fc2-bc35-eb36c77fd078 | -11.78443 | -43.57157 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9d465a6-89a8-333c-ad3c-2e9b6819c2be | -15.74967 | -43.64997 | 2026-10-02 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d63ea142-3384-3607-8045-d157286b27e3 | -8.53308 | -54.56813 | 2026-10-02 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README43.md)
