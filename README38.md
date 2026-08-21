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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78ebaa22-4ee6-395d-aac0-9d4bb60d0fa8 | -6.58769 | -58.99581 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e12ddb63-5d1c-37b7-9c3a-bbc517340da7 | -4.94139 | -55.78296 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7cc53ec5-a793-3646-9d9a-235227a21149 | -7.00902 | -56.5453 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 983d98c2-a530-3025-a541-3874a1d68e19 | -8.16216 | -46.72842 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1ae6f7b7-02a9-3e97-bfd3-8b522fa6dfe3 | -6.69659 | -58.93319 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 782d0407-1300-3939-8eee-275e5780d2e7 | -6.89942 | -59.43248 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f206179-1311-36ad-b318-07baa77fa8dd | -3.86331 | -49.09465 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f222fe54-4af4-3e85-91ac-618322cd62f5 | -6.42776 | -52.74521 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df0da103-6744-3385-b773-3822494f42e9 | -6.0175 | -57.82914 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f00f43a3-364c-356c-9908-6b342864946a | -4.93794 | -55.77886 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5a3b1477-69c1-3e51-a4d7-dba4929db2ef | -8.54136 | -54.86856 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba30e6ff-9915-36b0-8dfe-cf1d42a412d1 | -9.40316 | -60.43403 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1be17158-fb1d-37c9-8c4f-7347a91e0fa7 | -9.92762 | -53.63449 | 2026-08-21 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08c53710-c138-3e56-93a3-5533aa00f310 | -8.54868 | -54.77966 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 235df987-577b-3231-b195-0373042797c4 | -6.51683 | -45.9045 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 108d8945-90ef-36ad-ac88-72dd33a030b8 | -9.41428 | -60.41858 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4a7d259-bfda-3462-bf4a-783f096dff29 | -7.772 | -61.13926 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cd29ae7-0375-391a-9ac5-10a40a930e26 | -9.22275 | -59.77163 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25f586cf-bebf-38ab-83f1-1fae82b2dca9 | -6.11838 | -59.90359 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2806a95a-9e85-343d-9776-8007c213d649 | -6.27233 | -43.27369 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eeea8aee-b158-3fdc-bd6a-a7704f633136 | -9.41054 | -60.55367 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f47d150f-d3ab-3636-9fae-0e843d646cbc | -6.68992 | -58.94308 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9585a96d-bc0a-31c9-90eb-f7c0c522a84d | -6.69568 | -59.10125 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7661fe0c-8cda-3a26-ac20-d434578f72d1 | -9.394 | -60.55703 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c862b2a7-a05c-379b-b82a-e943f4baaf07 | -8.38669 | -62.70653 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2a35cd9b-c58d-37c3-9fe0-8e3136c9a640 | -8.6565 | -54.63074 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9795328-1d94-3e79-bf50-f11d7b6e7156 | -6.75927 | -59.46743 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 012553c7-4804-3839-aa32-59bd14876596 | -9.23958 | -60.39058 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2644f6e7-a6ec-3918-92a9-2c79933ffdb6 | -6.69807 | -59.09996 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13aaf64b-e2a2-3672-ac5c-64cba8f3689d | -6.34752 | -44.07913 | 2026-08-21 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4c14054a-773a-3cf9-9e0d-4d272be42b47 | -9.5192 | -51.64339 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e341ccd6-6a0c-3069-9b73-934bca548d93 | -6.13422 | -59.91044 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bfcf88b-fe0c-3255-a386-8c20c7aa1708 | -6.48285 | -55.90002 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 277a418f-d2d3-3f14-88b5-163974be5056 | -11.63255 | -46.54995 | 2026-08-21 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b4440047-ef14-3429-9114-1e049d5c338d | -9.17611 | -57.00551 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a48f0da-d6a2-35f9-a05f-dad4ef688b22 | -6.8967 | -55.71421 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b20c1978-6d69-32d3-9f75-c3cf20880817 | -9.25007 | -59.8164 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68eed54d-b2e7-37b2-bd24-ee2b75d55e86 | -7.349 | -45.8117 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d7742a5b-9712-3736-ba71-07b0a35efd26 | -10.30105 | -48.23047 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fbb951c1-57b5-33f0-acee-f615fa60c568 | -5.66617 | -51.64336 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2ff76cf-7473-3ac6-a17d-813a90b4ec2a | -6.2335 | -55.40802 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e546875b-c6ed-3ce8-8f57-9b4a17e12d61 | -6.0996 | -57.87499 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c6fb689-4d3f-3c3a-a32b-6f1f625deb9e | -6.76684 | -59.45377 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 326ff14e-17fb-3061-ad52-35eba607fab2 | -7.73155 | -46.15913 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25ec2ca1-c2a2-3b7f-b0c8-959748e71764 | -9.40862 | -60.42074 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f346a458-50d1-3884-8160-c448f38e770b | -7.86606 | -63.76392 | 2026-08-21 04:46:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1aa0fa9e-6885-3f5f-95f5-7d325a21053f | -6.42267 | -54.93357 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 151d7c11-ab1a-3bea-b603-6ec6cbb17408 | -9.01243 | -40.99654 | 2026-08-21 04:46:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5f31c36c-23f0-3d08-a891-16fcf7670026 | -5.32548 | -50.95107 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9579460f-1ae3-3d3c-8c90-7a17c94d971d | -11.63308 | -46.54598 | 2026-08-21 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70c3b04b-8dfe-3103-97c7-f8dd2e32f767 | -6.3899 | -54.94669 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5f7c558-25e6-3ce2-af0d-40abde4782e6 | -6.58377 | -58.98956 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf8f257b-a251-3332-a9f4-ebb13e9f6861 | -6.20088 | -55.48711 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88bbe35c-2ce2-304b-b377-04c6f8ee0167 | -6.57385 | -58.96013 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53fe6ad0-aed8-3814-8ec5-f2492e496280 | -3.85031 | -49.0448 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d46e69e-b0fd-36ff-a671-dd98b6416e4a | -8.54231 | -54.79576 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9209992d-092f-3d1d-b79b-0b17d81a4152 | -6.65726 | -56.34886 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 291e7f6d-2031-3b7c-bf63-ed43e8fe9fa9 | -8.33559 | -46.49971 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2624f63c-e65e-3003-b56a-673154a3573d | -9.41882 | -60.42248 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7046ff61-d544-34b7-8bc7-a058c630159f | -6.24904 | -55.4229 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a5f878e-bba0-3498-86a3-b527d9b824b8 | -6.99851 | -48.03532 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ab2b10f-2c19-3f14-81dc-e3b83f87bee5 | -9.1714 | -57.00855 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 234143c1-e6bf-309d-b5a3-d7f7a5b0cce8 | -7.35371 | -45.80849 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e6c7c993-e5df-37ee-a2d3-ddd8f4437423 | -6.72288 | -59.08944 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d366c12-c044-39bf-8ee8-a19a64ad30ab | -6.24271 | -55.42438 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02568795-1f01-3cb7-861c-1c1f65d8b049 | -7.14395 | -47.51168 | 2026-08-21 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb4fdf2b-094f-36ea-9f83-bc01374bbb4f | -8.55289 | -54.86625 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7239ba2-ebc3-3845-a307-a52824c699ae | -6.24679 | -55.41272 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c329a7de-53ec-3fbe-9c2e-700048290a86 | -6.65321 | -56.34819 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89e753bd-0213-3f33-96cd-3c1e0419febc | -8.06022 | -50.10884 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d58b1813-fa80-3454-bef6-d112c493edda | -10.80822 | -50.27511 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e04c99d9-115d-3df6-8928-f6ec0fd84082 | -9.41142 | -60.40561 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 904a23f4-328a-3457-abfd-0592e012e6ad | -6.89271 | -56.43981 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 349f2ee0-d19e-3360-816f-f3f8531d59e8 | -6.70387 | -59.09535 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22e370b7-364f-3ad4-bbd4-662fc8a0c1f8 | -7.60187 | -60.94869 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99974b0e-5509-3380-b6d6-7b7e3b58ea46 | -6.57293 | -58.96547 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7457f67f-7906-3d97-9b43-bb91415e4d3b | -6.86114 | -59.03289 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd6203ed-cc15-3152-a6a6-f3f8e87db961 | -9.11334 | -61.60675 | 2026-08-21 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15059015-66eb-3750-9a1f-f3313d483bf3 | -8.65758 | -54.6318 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a1ac7ce-c6cc-3397-b644-0eacc04bcc2e | -11.28495 | -45.78509 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dec2c87-6412-3e86-bcf4-db1f79158773 | -8.16115 | -55.375 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c0e92f6-1333-3a06-84e2-5e4c276702ba | -9.06109 | -60.44299 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 578194ec-6610-3fb1-88ac-cc061d1823d4 | -7.03732 | -45.89971 | 2026-08-21 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eaabb46-db6b-34a0-94a2-443709931670 | -8.03486 | -54.02009 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f13b6ff9-6015-367c-8058-985b5ee6153b | -6.8768 | -56.63622 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42f6ac62-2082-3e04-9152-272c6d31214f | -8.17035 | -55.00001 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 504a8236-fd39-336d-b2a8-90a57fe410b8 | -7.88782 | -61.71494 | 2026-08-21 04:46:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c82cdfb-0e51-3632-ab2f-84dd8ffa3d3c | -9.20594 | -59.767 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 30dcb859-e0d9-328d-a083-e493398399ba | -6.33257 | -46.52319 | 2026-08-21 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52fc2c9b-edd7-31e5-8b42-8797e85278e4 | -5.8725 | -57.66339 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07064f51-2986-3f03-86d6-06c34a875199 | -6.87753 | -59.44038 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d53e875c-3a30-3917-8e75-3bea85d4bf04 | -9.50759 | -51.63084 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3192ecb1-9ce1-3420-b184-17bba279f562 | -6.23967 | -55.39425 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5cc8c44-8c1f-3340-9b47-788889ff8024 | -7.2557 | -49.89746 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4acd04b-bf0c-38e7-a57c-b9fa85aadc57 | -10.24278 | -54.37144 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb411fa2-dac4-3106-ab62-43430c09be61 | -7.46571 | -49.70999 | 2026-08-21 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0c8ebfd-ca8c-3866-840f-3185ab18dbaa | -9.40182 | -60.42905 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e107616b-99d0-33c0-a5b0-e348e45345ed | -6.69958 | -58.94468 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8a7b488a-665c-3946-9197-133a29057fa3 | -6.81644 | -59.40497 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3530a5d0-c2b7-3742-8ca8-e2da351c87a3 | -8.27324 | -57.34975 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README39.md)
