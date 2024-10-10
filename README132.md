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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4701fe0-6c8e-38cd-969e-043184e0b8aa | -6.7368 | -59.30193 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d283d728-31da-3c97-8807-1ff4c5018acd | -6.7367 | -59.29525 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2015aeeb-f4df-38b5-ba42-c27c077b95d4 | -6.73523 | -59.30499 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c4f57c5-8b10-371b-b7b0-6331dda64562 | -6.73432 | -59.29159 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22437797-78a8-3403-a662-418677acec6f | -6.72987 | -59.31425 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5a4529a-ddb2-3c65-8f0b-bd9be9736235 | -6.72832 | -59.3057 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67a46c6e-3105-3be5-9dc8-97dc9645df63 | -6.72761 | -59.31062 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c174bed-5981-35ab-9c6c-ba7b6fce9316 | -6.72672 | -59.30879 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a1c3a40b-29ac-3c9f-b9b6-fc5e0e3d803f | -6.72621 | -59.32039 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2afe0233-a896-3038-afff-e47c0dcd053f | -6.72525 | -59.31855 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b9161e0-0667-3a51-9b75-463d71c89662 | -6.72443 | -59.30514 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5af27274-83ad-3c09-a640-301fcf28257d | -6.72431 | -59.29842 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8d3d0d5-9146-3bb9-a56a-e7f53b3bc849 | -6.72357 | -59.30332 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13db20dd-afbb-3ecf-98c4-b441accd4287 | -6.72284 | -59.30823 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1601aae-0f1e-3030-b039-9a383374f523 | -7.46991 | -60.60923 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 725195ec-b610-30e3-b550-ef030eb724b4 | -7.29773 | -59.73565 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd5bf2c0-3155-306b-893b-6f3f2602953c | -7.19099 | -59.77555 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 349a45e3-2598-3769-b8be-3bae1735f18a | -7.19029 | -59.78024 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc74f388-fad6-3672-9d6b-06fe7a1aa4fc | -7.09735 | -59.41219 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 956030bc-ba4c-376e-b556-c190b6941245 | -7.09347 | -59.4116 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1fd69813-6789-3edf-82e1-9531fdf7a591 | -7.08959 | -59.41101 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b02037c7-5fda-35da-b391-268f50465ff8 | -7.08572 | -59.41043 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| f9b4d13a-9ea5-3534-810e-40bbe0a2555d | -7.08501 | -59.4153 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6c0b9618-2055-3aa8-8543-1285a640ddc8 | -7.08184 | -59.40985 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| abf30805-aa6f-385a-9364-547cf3bd6902 | -7.08113 | -59.41472 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 02e8c8bd-455a-3380-877a-05d5ce4371b8 | -7.07796 | -59.40926 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 717a746d-d570-39c6-8d52-d1c6da25dbd4 | -7.07725 | -59.41413 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5a2dfc5d-645d-3d64-9653-336b771d78ee | -7.07409 | -59.40867 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d9dac243-c133-34fb-a926-0eb46d3d4317 | -7.07338 | -59.41354 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 084857f1-5f86-3ad8-b51d-20a2dda6fb83 | -7.07021 | -59.40807 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e809e16-12d5-3888-a4ad-c6c47dff4efa | -7.06106 | -59.41661 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2f4466d9-07b9-3112-80d4-d6df34a772ae | -7.06035 | -59.4215 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92a3a4bf-8ec5-3341-9796-9144dbd0b114 | -7.05718 | -59.41602 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6850f4f0-6090-3618-81cb-a98087165a2f | -7.05648 | -59.4209 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83f01171-30e1-3238-9cee-3a5b80e0633b | -7.05401 | -59.41055 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 669e11dd-f40b-32f5-88e4-c1fe057fdf90 | -7.05331 | -59.41543 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bf63c2d5-d011-3edb-9d60-3a3c63b4566a | -7.05261 | -59.42031 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 43749855-0ea8-31f7-af66-bfa6c83c6c76 | -7.05014 | -59.40996 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9d287ddf-dad0-371c-b6e7-deae66639cc8 | -7.04943 | -59.41484 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 638ae1d2-c4be-36e3-a5a4-7487d4230a2c | -7.04873 | -59.41973 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b5a263a7-6fa9-306e-8dc6-e7d6bbd84d7f | -7.04818 | -59.41303 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b649c35b-9e5b-31ee-84fe-e9282fdbe467 | -7.04803 | -59.42459 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c5723ca5-e2e7-394a-9fa2-f326dd5fdb16 | -7.04744 | -59.4179 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 836ea06b-e0ea-34d0-97ee-55525786072d | -7.04671 | -59.42276 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29e7e646-216d-367d-9642-4d9793ed8352 | -7.04556 | -59.41426 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f44afd54-d730-39ff-9ffd-3b6b6a4cd6c9 | -7.04486 | -59.41915 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76c34eec-7a1b-3605-9d81-74492f4aafcd | -7.0443 | -59.41245 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 95aeb319-ae21-3903-ae0b-7fde9b3982b8 | -7.04416 | -59.42401 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf3b5363-8410-3087-a353-413b5e7c4539 | -7.04357 | -59.41732 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba804fcf-6101-30f3-b4e9-26c19d8d4cd9 | -7.04284 | -59.42219 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 19c6da5d-453f-37d0-ab98-ae969a8cf177 | -7.04276 | -59.43374 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d6d3319-c175-30c9-9659-a00ce60b6c83 | -7.04169 | -59.41367 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 554b8542-cf9b-3daf-9dda-38520edeec28 | -7.04138 | -59.43188 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b73cc9c1-f126-3d31-96de-1a8e9e779671 | -7.04099 | -59.41856 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c965e3a5-06e2-360f-8bb9-e9b96dab4245 | -7.04043 | -59.41185 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 646a6475-1c98-32a8-9d7c-b714e37f683e | -7.0397 | -59.41673 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0a0adf9-10f4-3f93-9adb-152c2db72db0 | -7.03959 | -59.42831 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a9ca1ef-73be-3ae4-8851-65711d5fe33d | -7.03889 | -59.43315 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fc2686c-44ff-39fa-b3cc-efb3bc2581c8 | -7.03824 | -59.42646 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61dfa7fa-34f3-343b-9c19-f0f538dcf2b2 | -7.03782 | -59.41307 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60d475f0-c0a3-3c5e-98e3-ec1d75407ce4 | -7.03751 | -59.43131 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33d9b2aa-8984-3cec-8de7-d9ee85038983 | -7.03656 | -59.41126 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f322019-0e39-3626-920c-c53b5a5fa2a6 | -7.03583 | -59.41614 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d69062d7-b047-370e-9de1-c0f74ac80bd2 | -7.03572 | -59.42772 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9aecc3d4-3938-3f8d-b0c6-5a026b89caf2 | -7.0351 | -59.42101 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46b60307-629d-3c9d-a78b-daeb8226bbcb | -7.03502 | -59.43257 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edf68d95-bbee-39bd-b4d2-ec9930f29c27 | -7.03437 | -59.42586 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f86ae8d-0224-33bc-9a3a-c004328f5e91 | -7.03364 | -59.43072 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0cd57e27-4ae9-3aa8-992b-8c0b8e7be60a | -7.03324 | -59.41737 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13d05ce3-dfe9-357c-b590-262a75d7bb87 | -7.03255 | -59.42224 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c4b1edd-257d-3529-831e-004b151f897d | -7.03196 | -59.41555 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d615ff9-98f2-34f6-80d4-e240c13292f0 | -7.03185 | -59.4271 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ec842fc-4cfc-3350-a8d3-98daf9af1b7c | -7.03123 | -59.42041 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97a9e02b-c300-3f61-8a66-50306093ba0c | -7.03116 | -59.43197 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64532e46-2d07-3f95-9f35-d1015c2adc29 | -7.0305 | -59.42526 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a09ba4c-2c3c-3816-94a2-2e7e1881f752 | -7.02978 | -59.43012 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1058ec45-78f7-353b-b5b2-83c8d4d67f48 | -7.16629 | -59.35476 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a544a916-8185-30f6-98a2-63ee2b581c08 | -7.16511 | -59.3571 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d6822a3-c7ff-3264-9b8b-9e45464d4c3b | -7.16239 | -59.35417 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d05591a-89d9-360d-b765-a4ec739a5da5 | -7.16169 | -59.35907 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce7fd6db-f473-352c-a301-b9984104bfc8 | -7.16122 | -59.35652 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd61a917-fa67-3f42-bb38-de815cdc52e8 | -7.15819 | -59.3835 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a909e33-22b6-3035-a043-220ec2090ebd | -7.15748 | -59.38845 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40722902-1903-31e5-b6b7-6cde67e5dc15 | -7.15681 | -59.38585 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4c1bd77-6065-3763-b83c-300f0c4fc09d | -7.15677 | -59.39338 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c2ad9cb-ad19-3270-8952-5e25e0b8b38a | -7.15607 | -59.39078 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3a8ffc1-9449-31a6-bb83-460ecbddd34f | -7.15533 | -59.39569 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d40d4980-52f6-33d3-8f00-2af4b33fe223 | -7.15358 | -59.38795 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15c2dac1-af62-3a26-a6de-81818aef3c38 | -7.15288 | -59.39287 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3972e2e4-bd4a-325d-929b-86ec11a190e9 | -7.13806 | -59.37835 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c42c16a4-8256-3192-a1c9-4cb23f225221 | -7.13418 | -59.37776 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 16a17e17-8de1-3232-8664-f9090937156a | -7.09031 | -59.40612 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4b3d5d75-df2c-3d3c-9dea-99122ff5b535 | -7.08643 | -59.40554 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 50ac4f6d-af3c-3dba-bc43-2894e7c6446c | -7.08255 | -59.40496 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| c9ede6e8-56ef-3d4d-bce3-308e5f95f450 | -7.07868 | -59.40437 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f804c98a-e3a2-3fc8-97c8-9971a1702cb7 | -7.04767 | -59.3996 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d816b70-94e4-3ed8-b948-78385f23fd6f | -7.04651 | -59.39781 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c92ed22-e4f6-3906-a835-7150a3d018ee | -7.04577 | -59.40271 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c14e0991-c49c-34ed-9f14-4d355f3f2769 | -7.04379 | -59.399 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a523eb6-6751-3b3d-a859-177bd8d88007 | -7.04309 | -59.40391 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README133.md)
