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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e05914a-2bad-36fb-b68e-683f7a71b575 | -7.44791 | -64.46576 | 2024-10-20 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1e178f8-5935-3103-8368-f77d615bd755 | -7.44703 | -64.46677 | 2024-10-20 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 279dfb43-0dce-36b5-aa31-e3032e092f0f | -7.44642 | -64.47071 | 2024-10-20 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19798d0d-7837-335a-a512-29d37dd5c9ff | -7.39428 | -72.78689 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63f74686-5a50-3bc1-b67e-9c3913d3b902 | -7.39035 | -72.96324 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d14bede3-08a0-302a-aa37-c87487e0238f | -7.36787 | -72.86669 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8a397be-c679-30c3-9d58-5b2a3deca8c3 | -7.3672 | -72.87062 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 77e6bd8a-8cb9-3339-8e32-15a109d9f017 | -7.36631 | -72.85031 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1296d936-54e1-3bbd-a1dc-d32c0404704d | -7.36365 | -72.86599 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2057c9b-1a40-3489-9778-c2a44a645182 | -7.36299 | -72.86989 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3e06f326-0a30-3904-b0c6-89ce445df907 | -7.35878 | -72.86918 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d6c0aeb-25ae-36cc-8053-e5a12f8a907e | -7.35811 | -72.87311 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81271197-6c5b-39bc-9546-f52b4a4089b4 | -7.35745 | -72.87704 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68cb27bd-eddd-3124-9910-8152ec8930c5 | -7.32642 | -72.75562 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e45cb377-d542-39eb-9df2-9aae61d97f3d | -7.32575 | -72.75948 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3412fc7-fa5d-355b-babc-d96d7ee063c6 | -7.32223 | -72.75494 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4899f24-148e-3b0b-a4e6-76d5a4ab521c | -7.32156 | -72.75879 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 911f77d1-39ba-3ae4-b98a-18fe0eea46fd | -7.32096 | -72.75539 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c96c65fb-5518-3fa8-958a-492cc28f46bd | -7.32032 | -72.75925 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51bdb9b9-982e-3fef-b456-43c500eeeade | -7.31738 | -72.75809 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d673f448-a112-313a-97f5-ae1b1f22f972 | -7.31613 | -72.75855 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d558ee41-cca5-3d66-aa4c-b65d3fe068f9 | -7.28082 | -73.06913 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7fe33d7-f674-3658-b7b8-bc98fe812cee | -6.95331 | -71.49358 | 2024-10-20 05:50:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 550f11aa-42f5-37a8-a84f-2eb105feaf0e | -5.93602 | -59.96576 | 2024-10-20 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3399179b-9643-3dba-a905-8b9d33501c44 | -5.93538 | -59.97036 | 2024-10-20 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc5c1777-3f2c-35ed-a4a3-8f0b30ce1b71 | -12.71302 | -62.90127 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae776c4b-d1ab-3c8c-a5da-b89cf2d2ef9f | -12.52147 | -63.30419 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ea5d186-01ec-3d61-ac11-b00b00ebed82 | -12.52099 | -63.30771 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be2daa95-b9b2-37a0-b38f-21216491adc1 | -12.51748 | -63.3036 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23d84570-4f9e-3248-a360-67ab6c5b8826 | -12.517 | -63.30713 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0765c13e-d694-3036-ac18-ed0add9ede96 | -12.51444 | -63.29597 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7690cac2-2444-3720-b596-df515ab3f163 | -12.51349 | -63.30301 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d23fa61b-64e5-3c78-8fdc-e0682b71b332 | -12.51301 | -63.30654 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7fb17391-68b0-35ec-94d7-e0adcc2929ca | -12.50902 | -63.30595 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 00b09648-cd54-3815-8ca8-18bc1781ba8f | -12.5055 | -63.30184 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb3736de-f7e9-3748-a123-8c9354112b9e | -12.49941 | -63.28657 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbfc1869-5891-372e-9f11-7188a5f44989 | -12.49894 | -63.2901 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca061407-c0f2-3239-887e-be51cf9ea80d | -12.49816 | -63.19299 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4d903c6-4689-3788-b243-8fa744dd0663 | -12.49719 | -63.28698 | 2024-10-20 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ea56b42-21bc-3ad9-a475-756c3245d6f4 | -19.55792 | -56.62121 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 81ee83ae-c6e7-3340-b104-2107a0d06b32 | -19.55433 | -56.6194 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8cf66795-5796-30ba-bd2b-51c46da2736b | -19.5512 | -56.62052 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e55a1f3d-1471-3e2c-9950-974dab3ddfb0 | -19.54762 | -56.61868 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9d6e71c3-bada-331a-98e4-f23637d8849c | -19.54711 | -56.62491 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 601fbd26-9a37-3019-9523-7c691dca91ca | -19.54661 | -56.63113 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c5ee2191-2d72-36f1-addc-929b872259e9 | -19.54611 | -56.63735 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8b49de21-7cc3-37c7-adfe-5088ee1c16fb | -19.54449 | -56.61982 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| eabc9128-2a7f-318c-96d4-c2e5c211e1a8 | -19.54395 | -56.62603 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 80261e05-b447-36e9-830a-53881cffaeb2 | -19.54341 | -56.63224 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 31fdfa1c-f467-31c3-a3c2-b6ce44e4a3b9 | -19.54288 | -56.63844 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 48a15783-b421-33e3-8fad-a213f73df233 | -19.5404 | -56.62418 | 2024-10-20 05:53:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ded73143-0f58-3e7c-9adf-150ba5e2aa60 | -12.96317 | -62.80418 | 2024-10-20 05:53:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3ce2ad0-d699-3acd-af6d-2085d7d9cef4 | -12.77915 | -62.96383 | 2024-10-20 05:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a3c272c-d3d5-3be2-8a54-a876fc4be482 | -3.05555 | -61.67302 | 2024-10-20 06:12:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c136ee5-5590-38be-ae3b-993abb8bfeaf | -3.04959 | -61.67217 | 2024-10-20 06:12:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a89e2f4-7321-38e1-a851-e3ac0d1e9b2e | -12.54423 | -63.27898 | 2024-10-20 06:14:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04260162-d490-379b-a73a-f39b384723ba | -12.5437 | -63.28364 | 2024-10-20 06:14:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 305cab61-ca20-3469-bbcf-a1a3f08a2973 | -10.20113 | -64.8427 | 2024-10-20 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49e3a979-f13c-35af-ad6a-614a7a922bea | -10.19579 | -64.84192 | 2024-10-20 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d232e59-7a90-3cec-8f0a-05f48a5cd40e | -8.90169 | -71.26309 | 2024-10-20 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2ec7623-0c85-3f84-ba20-dbdf8fe0e093 | -8.87576 | -72.74523 | 2024-10-20 06:14:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3539a4c9-a094-3548-9020-85c187fac62d | -8.33932 | -72.60396 | 2024-10-20 06:14:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b7cd9fb-6dd5-35b3-a9d1-f234c9d5a03e | -8.33876 | -72.60749 | 2024-10-20 06:14:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3534f84d-99df-3c49-b811-2d88cc21b077 | -8.33766 | -72.61459 | 2024-10-20 06:14:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4094fe-c037-32f8-8cbf-69b7d4c3ffd3 | -8.33597 | -72.60343 | 2024-10-20 06:14:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f946b765-df3d-368f-8681-8c5f3608b182 | -8.33541 | -72.60697 | 2024-10-20 06:14:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d27b9862-2e00-3fb0-ab6e-cebd6b20e1f3 | -8.33431 | -72.61407 | 2024-10-20 06:14:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63ecc4b9-5efc-3060-8b17-fea1f1ce0f2b | -8.33097 | -72.61354 | 2024-10-20 06:14:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de121828-7266-31eb-9166-71037d5d2743 | -8.31135 | -72.8059 | 2024-10-20 06:14:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab246996-6e4f-390e-a791-2f36afecac44 | -8.01441 | -72.40848 | 2024-10-20 06:14:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 74fc3c45-367d-393b-abf7-3256c32272fc | -8.01386 | -72.41205 | 2024-10-20 06:14:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2a64ac48-ee8b-3c58-9af6-fdc71da57757 | -7.85087 | -72.87398 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90bc3037-5150-3df3-97ab-a53caa7fc387 | -7.85033 | -72.87748 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0114567-c7be-31bd-a6f9-da4764c7827a | -7.84699 | -72.87696 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 447e5ec6-d64d-3a26-b7f5-0508353b22ee | -7.84058 | -72.76463 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1eb8dce-158b-3e94-ac57-daf10d489451 | -7.83021 | -72.83129 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a586bb41-8fc1-35c9-935d-74797015edbf | -7.82749 | -72.84879 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9d81593-55c9-3cb8-94c1-681401a2c319 | -7.79569 | -72.77594 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abf1fcee-e3d4-307f-9e54-36103d7a08d1 | -7.7891 | -71.98779 | 2024-10-20 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85e1c19b-001d-3fab-8949-58c684c2af1b | -7.78621 | -72.96056 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a30fc47-e4f2-3825-90a6-15d14fb61702 | -7.77157 | -73.07626 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb03df64-a920-33cf-983f-6426f4e1db7d | -7.76825 | -73.07574 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 232356d4-cd43-38b5-8862-cc276894da51 | -7.70978 | -73.04182 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc300497-1e67-3bdd-8b77-ae9c7b2a8d64 | -7.70923 | -73.04531 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b9b8003-23ed-36de-9bfc-e6e5ce7ee87b | -7.70868 | -73.04881 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37ea1044-9400-31a4-89c4-f5ac3b2d8a38 | -7.70645 | -73.04131 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e16c3d3d-8cb2-317b-a688-365bafa020bc | -7.7059 | -73.04479 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae24bf01-127b-3f71-be07-a45f007787d6 | -7.70536 | -73.04828 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 812ab6c3-5996-393b-bcb5-cabc3496c7f9 | -7.70313 | -73.04078 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb786574-684b-3ed0-86cd-178cc12b17c3 | -7.70258 | -73.04427 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43191f16-cd5a-366e-8273-42127f3fd5f2 | -7.70203 | -73.04776 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93a66ef6-ed64-3e54-9024-f66c9b400b34 | -7.70149 | -73.05125 | 2024-10-20 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 726701f9-14f2-3ed9-af9c-4fd607efa82c | -7.66939 | -73.06048 | 2024-10-20 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e91666c5-fde0-3382-b44f-daa702eb9aeb | -7.65765 | -73.24405 | 2024-10-20 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84a76982-6f92-3e13-8b69-f9e89ad907c7 | -7.61121 | -73.06569 | 2024-10-20 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 643b5ac3-cdd6-3662-8406-05d0385ec329 | -7.58347 | -73.04704 | 2024-10-20 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a5ea270-892b-3e25-92f7-ecdbf13a9165 | -7.58015 | -73.04652 | 2024-10-20 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b8b8d41-49a1-32b6-b2fb-8363d113b8e3 | -7.5796 | -73.05001 | 2024-10-20 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 048588c8-cb90-3c92-a613-32add2d65824 | -7.57628 | -73.04948 | 2024-10-20 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d99cea3-aa85-30ce-a714-95d2b31eaecc | -7.45863 | -72.72303 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README58.md)
