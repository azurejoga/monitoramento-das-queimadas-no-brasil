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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59a8fb6f-872f-39da-8407-f5d6b8d162a7 | -6.70299 | -58.96165 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6379e86-3933-3da1-b8b4-437d72022c58 | -6.70615 | -58.93819 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8a8e0377-0656-327f-8950-243d7175ce5e | -8.09308 | -61.35828 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4e3637d8-4357-3eca-a60a-fcbaa1bd7ff9 | -8.90571 | -60.56474 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 294efa64-c9ab-3947-86e3-8214db619f88 | -6.96374 | -59.30381 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d7324f3f-175a-3e63-b98c-f6e71353b0ad | -6.77189 | -59.76274 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95c03b11-98ac-36e1-97d6-d5e5d2a1312c | -8.97074 | -60.52705 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8056bbef-6c55-3a8e-b302-f818192b3c6d | -8.72654 | -62.90141 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba5b742d-dc86-34a0-8063-f2e5b6af616e | -6.62651 | -58.9699 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c57d94e-740f-3b4c-bc16-4ac86d663e3b | -7.07043 | -56.65484 | 2026-08-17 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 26fa37f5-119a-30f2-980f-5174bba286a1 | -6.69806 | -58.95186 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62e39d5c-776c-3949-b80f-1006191d25ae | -6.98103 | -59.03401 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19e8c045-391c-3306-b3f0-d861543be575 | -6.60758 | -58.97156 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01397251-e0bd-3e87-aa70-da85011c73e1 | -6.60149 | -58.9751 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| afa59e76-1bc0-34ed-afe6-1d704428d5f0 | -6.98776 | -59.03027 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5722e8c8-579b-3705-9d79-aee1b1a90de3 | -6.11547 | -57.70865 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2592a76-e277-3a87-8180-0955b5193fe1 | -7.59445 | -61.23412 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65faea5b-4f68-3b97-b439-839dfccd26d0 | -7.42505 | -60.01624 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 747a9450-32cf-31e6-ab50-f483bf6c2f19 | -7.40671 | -60.02126 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c24cab85-f426-34ed-80d3-23e6bdab024e | -6.87353 | -56.40783 | 2026-08-17 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f44bc722-9ddf-321a-b878-84a9352c8560 | -6.11089 | -57.74271 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 38547c84-b7e3-325b-86de-a88daa9b5dfc | -9.18137 | -59.67484 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c723d03c-51c6-3185-92cb-753441a9efd4 | -7.46322 | -59.99824 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da94cad7-697e-36dc-bc4f-6901770858e0 | -6.71972 | -58.93032 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c4a7fd8-66a3-3c22-898f-b2a2aedc21b9 | -6.96757 | -59.04158 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 434b797e-f3b9-38eb-a2c7-023c8d787d45 | -6.62786 | -59.05892 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d64fed5-be39-3c8f-89ee-c8872b737106 | -9.35472 | -62.37087 | 2026-08-17 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 513bb2ed-b047-36dc-bbec-a65ea7c5ec12 | -9.35512 | -62.36792 | 2026-08-17 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 894f3645-00fa-3495-a46d-ccadb2e6437b | -8.96601 | -60.5183 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9363ce81-2a01-347c-bfe1-4d6c1f6564d0 | -9.37076 | -62.36695 | 2026-08-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7d7ef6e-8f80-3336-8d50-e63e254b40a6 | -6.72037 | -58.92556 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cfeaea9-43f6-3bbc-9d0d-73047d98a421 | -8.43247 | -62.65658 | 2026-08-17 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1dcb00bd-00d8-389c-b949-3b4218464350 | -8.97658 | -60.51078 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22315147-87ac-39a6-ab51-71743c5045ab | -8.97088 | -60.50989 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f4ad793-3faf-3b71-a1e0-28a4695a5e01 | -8.9745 | -60.52659 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3b326e7-7c4e-36f5-950d-d32af73a8128 | -8.90168 | -60.59631 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1a55e6e1-532c-3387-bcd7-58cbc44a7b4e | -8.89601 | -60.59546 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0544cd0e-f733-3386-8c21-e50fdd0152e9 | -9.3695 | -62.3662 | 2026-08-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f528127-6148-399d-b689-8c9ed15a5c6c | -10.07345 | -60.5009 | 2026-08-17 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a59a8f65-f520-3aef-8833-7550c359821b | -6.61914 | -58.97819 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 26e2827f-ce0e-35a7-923d-f48b70efeaf6 | -8.95433 | -60.59175 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0e25694-709d-3e22-aa8b-f83346521b2f | -7.61853 | -60.95176 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| deb889ee-aafe-3253-ba14-4b7ea5570c47 | -8.94649 | -60.5185 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ba747f1-df32-354f-8adb-acd7c793e212 | -8.81794 | -70.6115 | 2026-08-17 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a8543807-dcfb-399a-9993-e3d4ac4b28a5 | -6.60879 | -58.96679 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 76d765b2-1340-3289-83da-07915f4e5170 | -6.70681 | -58.93333 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 608d86b2-5741-3656-a9e6-07d1b1b28826 | -7.35099 | -59.59395 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 684bbbb5-8d85-3101-9413-c552f442f58b | -7.40252 | -60.00855 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33d016d0-f3a9-3193-93a2-9f6b78a59f90 | -9.08535 | -61.40333 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fac95020-3520-3cd6-9da6-c7c86427259e | -8.90052 | -60.55999 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c4a3223e-b8df-39fb-ae71-fad6795ee511 | -8.90117 | -60.60031 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e4e4c6c9-a8f8-3591-a441-c27ac6172bc4 | -7.43662 | -60.0178 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a5e6a92-c25b-332a-8273-8488798b0fb0 | -8.96827 | -60.52973 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dd792f9-3ffa-3e72-82f5-c970903a65c5 | -8.98229 | -60.51161 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c25c4ef3-f814-3bb7-96be-bc09931738fb | -6.9914 | -59.04981 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63a9e82f-7f6a-30df-bb62-23ea0fe861ce | -6.96819 | -59.03686 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 851d3bbe-999f-3e13-877d-a9d4ee77fb60 | -8.98363 | -60.51688 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bffb1628-609b-3ea9-9a5d-986104ec4cce | -6.86405 | -58.97405 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05e34939-bbe2-3e96-a61b-ff0bec5cd515 | -8.95219 | -60.51936 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83e12c2f-cc85-3f97-aa46-22e1420aa64a | -8.89499 | -60.60346 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 25e1d3d9-ddf0-3d4c-8090-b420473ff8ca | -6.60695 | -58.97623 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d466c610-a6ef-3f6d-8f77-a37fbfb9d709 | -6.1074 | -57.71898 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dcbb660-b5cd-3767-894f-cb9f2746ddad | -6.1124 | -57.73146 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8c9173a0-70ef-319c-8a21-e2a64d6d7456 | -8.98413 | -60.51287 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89c2f88e-a6f9-3e87-bfbf-375d47217656 | -8.97792 | -60.51604 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c7e7e92-1bf4-3f8e-8d99-aed982a808b4 | -7.43692 | -60.01934 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4661da0-cb1b-3949-93ff-b70bc84c411c | -8.09262 | -61.36163 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c419d1b6-c132-3493-8e06-766bbed320f8 | -6.71364 | -58.9279 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b941942-bbe8-374d-86d6-a37400b9aaa7 | -8.95121 | -60.57135 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 606d399e-da5f-37e2-90f0-8667efd903fa | -7.61357 | -60.9474 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ece46f7-8872-3091-ac93-ed0608c18fdb | -6.62542 | -59.06789 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe4b729a-cb97-3588-9fa2-b44e6fd67507 | -7.59165 | -61.22838 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 111c9fc2-1eb5-3cc7-b5ca-3c5c3d54c726 | -6.71297 | -58.93401 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8239a0e1-8d67-3826-8bdd-30a28301790d | -8.42383 | -62.68347 | 2026-08-17 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e480aa2-761e-399f-8a62-57a9e8c81289 | -6.63383 | -58.96582 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 067ef81a-bdcb-332e-b777-0494d4f31230 | -7.43084 | -60.01699 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2d29f34-d328-30ab-be62-63e710d181e5 | -6.85092 | -58.97659 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5a2f44e-67c1-3490-b9b9-fe798a18550e | -8.97606 | -60.51476 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10b4ae9c-e585-3717-b167-4bd875a7db27 | -6.62648 | -58.97446 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52070809-3f8e-3250-a0b6-e7e6693a8487 | -6.6461 | -58.96736 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47eff038-aa2e-3db2-9721-6f8dc34e4785 | -6.62478 | -59.07248 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d4b279e-945f-3025-8546-3f5833a04142 | -6.78293 | -59.46955 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d8ba8a0-7e64-343c-ad90-f4ee3d8caec3 | -6.76716 | -59.48075 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5653c4e5-04b0-3e7c-8c13-dd02fada56b5 | -6.7788 | -59.45564 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e66a6f4e-8114-3635-8f48-505fee9fe6c8 | -8.73551 | -62.90819 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 82d17868-fe09-3a46-ae3d-d7b2c7af5d08 | -6.6273 | -59.05431 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e865e2f5-00bd-3e7f-9b68-36c60b96570c | -6.60209 | -58.97046 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1cb3d508-6039-3bfe-9c1c-d67db9b7628f | -7.55615 | -61.16824 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84594997-67ba-317b-b771-03b56e19752b | -6.10508 | -57.73625 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 70a0c7db-45b3-3124-973a-e9db8c8ad73a | -8.97891 | -60.50807 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e145fb1f-3014-3eb3-a62a-ed413503dd51 | -6.71233 | -58.93871 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c816cec6-d7fb-3f61-9a03-6b25688d3274 | -8.9574 | -60.56832 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7332031-6030-3f6e-8d60-9970b0401005 | -6.63997 | -58.96653 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d80aeb53-d7ec-3fcd-8cff-e0e9cdfd2c56 | -6.70551 | -58.94297 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1e554155-7a92-30b6-8071-11ef60f8f51f | -8.90421 | -60.5765 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33380eba-9099-3759-acae-dd21ed97b348 | -8.94751 | -60.51063 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a20988a5-019e-3057-ba2a-fb5f22bf54f7 | -8.08775 | -61.35748 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3b541c8f-8f2e-3904-87f3-a5c951951fa9 | -6.87255 | -56.41525 | 2026-08-17 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c34880d2-1128-30c6-a774-144ddb2c0ad4 | -6.99202 | -59.04515 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36d1c234-cb5f-3095-b295-d8a3e266db54 | -8.09217 | -61.36497 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README61.md)
