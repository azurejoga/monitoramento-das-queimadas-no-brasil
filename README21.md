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
| 204f44fa-bf8d-31d5-ae90-525ea2a9ac00 | -10.92163 | -43.04749 | 2026-07-04 06:08:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c1c733b5-1eb3-3191-9fba-24a2ab45eba2 | -6.89806 | -43.7129 | 2026-07-04 06:08:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f4adbd14-bfb6-35ec-8e91-1240b7f218f7 | -12.7553 | -44.5194 | 2026-07-04 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4d1d8b15-3e4c-3f19-ae9f-bf185a745310 | -13.2404 | -54.3303 | 2026-07-04 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 919d71e2-6be9-3a0d-87eb-be6166f331aa | -10.9401 | -43.0355 | 2026-07-04 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 4352d7d4-8177-3aae-985e-7a86a537a2cb | -10.9205 | -43.0622 | 2026-07-04 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a9a5718c-e95b-3df0-9335-f2e3ad8162bc | -10.9397 | -43.0593 | 2026-07-04 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3bb37069-f451-3c81-875e-896baf3b0aa2 | -13.2592 | -54.3489 | 2026-07-04 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| af72ae37-b6a7-367f-8c39-b8cb640ab766 | -13.2212 | -54.3324 | 2026-07-04 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 903eb471-dbe1-3418-98d1-28a17579cce2 | -13.2209 | -54.353 | 2026-07-04 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 76473cba-0973-3e36-b047-79a7dee6f6d0 | -13.2401 | -54.351 | 2026-07-04 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| d0701b82-a1ce-3c0e-8c30-031db96752c3 | -12.7548 | -44.5428 | 2026-07-04 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 97d61d43-e291-3d72-ae96-3cf86a7cf219 | -10.9209 | -43.0384 | 2026-07-04 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d534354c-8a4d-3174-965a-4773c1d29500 | -13.2209 | -54.353 | 2026-07-04 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1cadb229-2372-3742-949b-6674b21f984b | -13.2401 | -54.351 | 2026-07-04 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| b0a48799-312c-3c4d-8863-5e934a7770e2 | -10.9397 | -43.0593 | 2026-07-04 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 9a60a600-471b-34e7-be90-1829bf0c2a30 | -10.9209 | -43.0384 | 2026-07-04 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c0c567f8-15eb-3714-b436-71020ab7af40 | -13.2404 | -54.3303 | 2026-07-04 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 5b33c12b-dc27-3f77-a7a7-8de408514a3b | -13.2212 | -54.3324 | 2026-07-04 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| db0c76bc-ad40-3dd5-8442-50ae2c9c43d7 | -12.7548 | -44.5428 | 2026-07-04 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a47e78e9-d553-32f9-a913-5a9ec871a54e | -10.9401 | -43.0355 | 2026-07-04 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| f7154f7f-75a5-3f60-8fab-e5469ef68cf2 | -9.37545 | -65.77795 | 2026-07-04 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 582e8ab6-2151-3db3-8227-bb3424b934e9 | -9.46539 | -68.3849 | 2026-07-04 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f77a63c-190d-323e-9b2c-deb8806102ef | -9.465 | -68.38799 | 2026-07-04 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb5f52c1-a285-3f9c-a14f-2080106e48a8 | -13.2401 | -54.351 | 2026-07-04 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 8e9b4507-9e3e-3354-8f18-02ebdefc1954 | -10.9397 | -43.0593 | 2026-07-04 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c185c717-69e5-3554-b727-eae5348fb239 | -13.2404 | -54.3303 | 2026-07-04 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 593178dc-4146-310e-92a1-56ca8abcfb54 | -10.9401 | -43.0355 | 2026-07-04 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| f608e777-4e3f-3e0e-98d8-6910f9051592 | -13.2209 | -54.353 | 2026-07-04 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a5d19bbf-d11c-30b2-a728-61b04873d909 | -12.7548 | -44.5428 | 2026-07-04 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| f6889d7c-2f53-3bb2-97da-e3667e853f80 | -12.7553 | -44.5194 | 2026-07-04 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| dc050ecd-d58d-3175-b633-6d08f2146be7 | -10.9209 | -43.0384 | 2026-07-04 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 883e4055-46ea-3b92-abd1-3bd9cfe8a203 | -13.2212 | -54.3324 | 2026-07-04 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 16a0415c-d9a6-3b76-99b4-dbc0e0326b7e | -10.9205 | -43.0622 | 2026-07-04 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| f9332f85-2f3a-35ee-8b3e-094db38afef5 | -10.9401 | -43.0355 | 2026-07-04 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 18765d7a-46f4-35fa-aba3-b93939dd7714 | -10.9209 | -43.0384 | 2026-07-04 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 35483f3b-f3b1-3bd1-963a-e3948770cd58 | -12.7548 | -44.5428 | 2026-07-04 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ef418f68-33b4-39d9-8280-221df6e65eb5 | -10.9397 | -43.0593 | 2026-07-04 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e649d554-5274-36aa-8d87-b256107994bb | -10.9397 | -43.0593 | 2026-07-04 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 65ab7523-aa0b-394a-84af-9b68ac92b36f | -10.9401 | -43.0355 | 2026-07-04 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| af729694-3645-39ab-a593-d280f6e5e449 | -13.2404 | -54.3303 | 2026-07-04 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4a439bc0-53b1-3973-8e52-0f76234ac163 | -12.7548 | -44.5428 | 2026-07-04 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 425c8b15-5ef8-3ecd-9762-40e671c0e7ef | -13.2401 | -54.351 | 2026-07-04 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 801d1a8e-e80f-3019-bdc4-8ad3b8669acd | -10.9209 | -43.0384 | 2026-07-04 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4fa20576-40ef-3b2d-ac61-21602bf1a520 | -12.7548 | -44.5428 | 2026-07-04 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| fabcab03-8df5-3f0d-84df-4d1da9e25484 | -10.9401 | -43.0355 | 2026-07-04 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 07ddf9df-0f25-32a3-a683-645c36d5a37c | -13.2404 | -54.3303 | 2026-07-04 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| c4e347d9-a868-377c-96ba-0b67a777a2e7 | -10.9209 | -43.0384 | 2026-07-04 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a02dcb24-cec4-3380-8b92-0c51713c80d2 | -13.2401 | -54.351 | 2026-07-04 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| eebd426d-8386-3030-8f20-a85433e0a522 | -10.9397 | -43.0593 | 2026-07-04 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 5de8e958-2a01-3afa-bf8a-c0a6daf80e8e | -10.9401 | -43.0355 | 2026-07-04 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| ca020179-4560-3de0-bf01-5cbf4c9e08aa | -12.7548 | -44.5428 | 2026-07-04 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 4a2e17be-36ef-3086-ad29-ee7737d089a3 | -10.9397 | -43.0593 | 2026-07-04 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b63539ac-213e-34b3-b33d-b1c8cea7a89b | -10.9401 | -43.0355 | 2026-07-04 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c85a5d96-0f91-39a6-bd26-38ff1f35138a | -12.7548 | -44.5428 | 2026-07-04 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 40bc17db-f5dd-3928-9b23-7785732dadbf | -10.9401 | -43.0355 | 2026-07-04 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 76292ba7-e186-3a86-b468-bb0cbf27e8fe | -12.7548 | -44.5428 | 2026-07-04 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 9741e12c-ddac-3311-b1e4-d4d15ab52f2f | -12.7548 | -44.5428 | 2026-07-04 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 7ff672e1-4aa8-3134-acbf-bd5639e27b29 | -10.9401 | -43.0355 | 2026-07-04 07:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 3c2eaa15-887d-3648-b8f1-59872dd77bf4 | -8.8627 | -62.21639 | 2026-07-04 07:44:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b0de5baa-054b-39d7-b353-ebf72b3548ce | -10.9401 | -43.0355 | 2026-07-04 07:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9e584053-5ef6-300f-9b92-2d2401efb3be | -10.9401 | -43.0355 | 2026-07-04 08:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| e5e0379c-dbaa-3d29-97e9-58f51f310a03 | -12.7548 | -44.5428 | 2026-07-04 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 7f99636c-5235-347e-b75a-6d79913d6bdc | -12.7548 | -44.5428 | 2026-07-04 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f41f09e6-8220-395c-87b6-3a0140b052d9 | -10.9401 | -43.0355 | 2026-07-04 08:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d74350b6-77fa-3ea7-a693-1dae5c5fb71c | -13.2595 | -54.3283 | 2026-07-04 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 19e8a105-05ac-35ab-abdb-f33be72408cb | -12.7548 | -44.5428 | 2026-07-04 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 3a0c6486-9274-31bb-838b-e660cde1503c | -4.34885 | -47.76473 | 2026-07-04 12:04:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ca10800f-e35a-3a75-b38c-77d3a954cd97 | -5.97395 | -45.0982 | 2026-07-04 12:04:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ea1a5590-bbf1-3819-855c-ada27367c7c2 | -6.90309 | -43.70714 | 2026-07-04 12:04:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 4c05539a-219c-3232-8184-c41c5086ec68 | -5.96417 | -51.40837 | 2026-07-04 12:04:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 2568b713-534b-3cf7-994f-d9d9adcf2287 | -6.90781 | -43.70229 | 2026-07-04 12:04:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6951843b-5684-37ad-9cde-573d5a59a518 | -5.31555 | -43.57186 | 2026-07-04 12:04:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a6eba717-ec10-3210-acf2-f3ea036e4d4e | -5.98295 | -45.08846 | 2026-07-04 12:04:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a9134e2f-d73f-330e-bdf9-6ff7588ff3de | -3.56387 | -43.56292 | 2026-07-04 12:04:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 48b19641-8159-3193-9611-75a6b315dcb9 | -5.31836 | -43.55056 | 2026-07-04 12:04:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3eec5f16-8c3b-33d6-b1b2-498ecba15eae | -5.9762 | -45.08167 | 2026-07-04 12:04:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 63bbabee-08af-33b5-b3e8-99efc02b30b6 | -4.5803 | -48.0205 | 2026-07-04 12:04:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a7dcfed3-37c1-39bc-9fa3-b5d54e5285a4 | -6.90034 | -43.72914 | 2026-07-04 12:04:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 64fcde7a-f213-3b02-bc36-c036b46595e9 | -4.57893 | -48.03042 | 2026-07-04 12:04:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c216cd0c-7561-3ffe-b690-56601591f4ed | -3.50912 | -48.0403 | 2026-07-04 12:04:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b1c7b7a7-c670-3df2-a17a-f41af234d5cb | -4.29558 | -48.35014 | 2026-07-04 12:04:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 46daa246-630f-3c60-b706-64f020a6ddc9 | -4.28641 | -48.34898 | 2026-07-04 12:04:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 90bceccf-5eb7-3c62-a58c-0f5d0bd5b03d | -6.90489 | -43.7243 | 2026-07-04 12:04:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| d0a5e3f2-8c2b-3511-ace5-59fa1a2a7b8a | -11.91758 | -43.39633 | 2026-07-04 12:06:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 5989131b-7133-32cb-a79f-d465e84fc99a | -7.90353 | -48.25176 | 2026-07-04 12:06:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e762d17f-e802-3fdd-a7b5-b82d2e9d7258 | -13.23383 | -54.33256 | 2026-07-04 12:06:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 1e7c0913-6845-32ce-a7b6-8359898c7541 | -12.75913 | -44.53458 | 2026-07-04 12:06:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 9981e817-1c75-38df-a90f-afb65a926f1a | -13.25902 | -54.33244 | 2026-07-04 12:06:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| d28e2b35-dec5-393a-8dee-6aa8e87cb1e0 | -10.78446 | -54.10633 | 2026-07-04 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| edeab994-8c25-323c-a806-530646e829fe | -8.03582 | -46.24125 | 2026-07-04 12:06:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 0e1caf8b-cc8b-3ef9-a1a2-f8f76ca599bc | -11.31623 | -54.47352 | 2026-07-04 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4544b8f6-65ad-3714-9353-6a0dedd09581 | -7.22974 | -47.11394 | 2026-07-04 12:06:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| bc8c3288-f0ff-3b06-b698-dd14b43802a1 | -13.25259 | -54.3354 | 2026-07-04 12:06:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| ac638ea9-82c9-3650-baf2-fa06526b4a21 | -8.03514 | -46.23557 | 2026-07-04 12:06:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 916e9eda-1467-3b6b-b128-38cf55e8cc8e | -10.92824 | -43.04353 | 2026-07-04 12:06:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8e5c7625-3e2c-3245-b084-568296c984dd | -13.25744 | -54.34267 | 2026-07-04 12:06:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 669927db-3348-3a36-8a19-5015adbbac1e | -11.50621 | -54.50421 | 2026-07-04 12:06:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 569e2b7d-37cb-3217-8617-3679d6594912 | -13.23229 | -54.34279 | 2026-07-04 12:06:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b6a61a7a-8764-3422-83a1-5639f84b2b0d | -8.03759 | -46.2274 | 2026-07-04 12:06:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README22.md)
