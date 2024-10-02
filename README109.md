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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cba10371-5602-3ebc-a312-e82f8af538ac | -16.70351 | -55.51416 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fe1d9630-f59e-3f18-b6b9-8503b093f9c9 | -16.70286 | -55.51809 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a63775db-dbac-3e1f-bee3-fc602a5f50db | -16.70222 | -55.52201 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 927e8606-6b3e-3d01-a948-dc087c4498ad | -10.76719 | -56.37876 | 2024-10-02 04:49:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28221e06-e07b-32f7-a98d-32ac7c0380dd | -11.82663 | -56.84095 | 2024-10-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aaa97b8-c7bb-3ef4-ba24-fa362d1c754f | -11.82575 | -56.84594 | 2024-10-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e38733da-e147-38aa-ad04-7f98fc51052d | -11.77443 | -56.31331 | 2024-10-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72a7a947-aa22-3c61-aa43-85ba6ebbe6d2 | -11.77392 | -56.31447 | 2024-10-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c11d971-984d-3ee2-85c7-e8fad8864517 | -11.77015 | -56.31384 | 2024-10-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc3bb83f-03df-3145-9846-c9e0749b0d22 | -11.49155 | -56.79465 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c6413e07-65f7-329f-9e20-9f5b3ee2cef8 | -11.48853 | -56.78897 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d684c789-8ea5-3dd0-b32a-9c97eb80dda6 | -11.48766 | -56.79396 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f8ec0c23-5b36-3097-999e-4fcd13d4d8bb | -11.4874 | -56.79172 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| db9d08e8-34c1-3b79-8838-87d28a1f5ad5 | -11.48553 | -56.7833 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8370f685-a6bc-37fb-951e-d70a24584dd7 | -11.48521 | -56.78103 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 033abcc6-91ec-3d1f-9c26-272ad135b402 | -11.48464 | -56.7883 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8c087cd9-e831-32fa-bb56-f52af6fabb05 | -11.48436 | -56.78604 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0e36ed0-43b7-3dca-a13a-7349058cdcbe | -11.48376 | -56.79329 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 316c13b6-54de-3b32-b461-4c0440f6bcab | -11.48351 | -56.79105 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 56c639dd-4a7c-354b-a7a9-68dd4cc8b671 | -11.48164 | -56.78262 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7614819-01a4-32b2-aab8-182763373a36 | -11.42347 | -56.29316 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf9d4420-1527-3751-975f-4356d8cab78e | -11.32831 | -56.23525 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87edad8d-cbfa-393c-9e23-5c30c4dda704 | -11.32752 | -56.23995 | 2024-10-02 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c6c041b8-0f45-3a8a-8c7d-a829fd9ccaba | -13.75595 | -56.47435 | 2024-10-02 04:49:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a16892a1-9f4b-31d5-baef-e1f6bd110b2a | -13.28465 | -56.1553 | 2024-10-02 04:49:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aff01498-0aad-3366-941c-0c6c2a272862 | -13.28389 | -56.15973 | 2024-10-02 04:49:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecaccef2-cf63-37fd-abd5-b60013b34968 | -13.2883 | -56.15597 | 2024-10-02 04:49:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea381cdb-46ac-35aa-b425-c536e1977a37 | -13.2854 | -56.1509 | 2024-10-02 04:49:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccd5d96c-9b25-3771-8afa-c850cfca5004 | -14.30989 | -56.85176 | 2024-10-02 04:49:00 | NOAA-21 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfcb21f7-18a0-3dd5-adb9-53a48beb43df | -14.30955 | -56.84896 | 2024-10-02 04:49:00 | NOAA-21 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39453e69-d3b6-3aed-9dda-531bf5011859 | -14.30615 | -56.8511 | 2024-10-02 04:49:00 | NOAA-21 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 302276ed-95d2-32f3-bdea-a68d033f65fa | -16.62923 | -57.21756 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| d0a36d98-20c5-3b6b-a4a0-9e7ab820c6fb | -16.62844 | -57.22215 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| b9fd6196-9f04-3619-beb8-b93fc237999a | -16.62553 | -57.21687 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| b39baae9-80bb-36e4-8340-f3a3fd3f32af | -16.62473 | -57.22145 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| dcf488c0-1a34-3087-9a93-89cb36a540a5 | -16.62183 | -57.21618 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 058ff85b-4ee5-3a48-a875-183ab83afbb4 | -16.62024 | -57.22535 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 276bcb2d-f67d-331b-a237-4ee39ec34b3e | -16.61813 | -57.21548 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| bb7131be-07ca-3ef6-919f-3d86351d446f | -16.61733 | -57.22006 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 66843bd9-3ceb-3f6b-a6a2-263e0a092f87 | -16.61665 | -57.33437 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4909859d-691e-35d0-9410-efbea8cecb42 | -16.61363 | -57.21937 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1104199d-dcf0-3cfd-a805-a2e9adcbe3e2 | -16.61283 | -57.22396 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| d061b15c-c853-3e55-8cf6-a6e9edae86bc | -16.61203 | -57.22855 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| ee8c8b43-321a-3fc9-b7ea-789917229bc6 | -16.61174 | -57.25222 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b305c5de-d748-3237-8675-fa1bb5bbdcce | -16.61123 | -57.23314 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 679d6435-a49d-3231-8cb4-c97406678633 | -16.61043 | -57.23774 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a23739f2-d576-3b93-81dd-d881fc9b3151 | -16.60964 | -57.2423 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 4469b586-0cb3-35ec-a801-b262240da4bc | -16.60884 | -57.24688 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 5eb76494-a49c-3cb4-8ea4-564903de545e | -16.5822 | -57.28957 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f22e40ad-0959-31b7-91cb-d34c4d824795 | -16.58139 | -57.29419 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 741fd14c-dd94-3e38-a011-30901e913a9f | -16.5793 | -57.28425 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d121b24b-46f2-3fe8-9f5a-4338be013f80 | -16.56464 | -57.41142 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 3a14a819-989c-3c1a-999b-6fdb71aaf4c9 | -16.53142 | -57.29439 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8e393da5-eb7b-3c66-b477-cad1cd457545 | -16.5277 | -57.29369 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 54c7ff72-ac37-34a0-a6d7-15ac75753610 | -16.52687 | -57.29832 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 39d6d893-d417-3cd6-be75-c0c9f8f76d14 | -16.52398 | -57.293 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f2bdfa7d-6924-3172-8598-7608830e390b | -16.52315 | -57.29763 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f5d07c45-f404-33b2-bf1f-c3815128579b | -16.5186 | -57.30157 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f793895d-f1f1-34f8-b8fc-c48609d32842 | -16.51835 | -57.29419 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 963a746b-f3f8-37f1-97d1-da707729a135 | -16.51755 | -57.29883 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 32c872f8-2d55-3545-80b3-0d5b5cf81e87 | -16.51654 | -57.29161 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 9a16d12a-1fb9-3d6c-b06d-fbd61bc107b2 | -16.51571 | -57.29624 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 849961c7-5d19-3c81-8a3f-7c4fdda2271b | -16.51544 | -57.28885 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 5a8f25a3-8ba4-3fc0-927c-abe395377105 | -16.51199 | -57.29554 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| c84dc59e-b719-312a-9af2-48bd453f7622 | -16.51142 | -57.31204 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fabc08e9-5b36-330c-8431-4b11684378ba | -16.51092 | -57.29279 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| af58cd6f-4114-3818-a6ba-fe38b0cca070 | -16.51033 | -57.30479 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 60835510-bd29-3a59-9c5c-2a6a9f8b0630 | -16.51011 | -57.29742 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| da391b2c-d701-3b1a-9bac-41b789a84652 | -16.5085 | -57.30669 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 82512f67-fee7-33ae-bbc9-49673e437c2f | -16.5077 | -57.31134 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4653d8b1-b447-3c87-aa6d-11239f74f1f8 | -16.50609 | -57.32063 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2a0863f3-25c1-3abc-b5ee-a37f32292f35 | -16.50559 | -57.30135 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| fc6b3de4-3d6d-32df-8ba8-2f29b5b26af0 | -16.50478 | -57.30599 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b18c069d-e313-3ed3-8ba0-7ce38e557cf6 | -16.50397 | -57.31063 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7dc52038-289e-3ac3-b176-3270a735139f | -16.50236 | -57.31992 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| dbb9d7d8-b4be-3414-8eaf-88245b6bb749 | -16.50074 | -57.32924 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c18345c7-807d-3ab8-abcd-09b452ec8a2f | -16.50025 | -57.30993 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a91a1c3c-c240-3a1e-866e-69941143a8e1 | -16.49944 | -57.31458 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a0a8ab5a-7977-37e7-aa17-52908e70bf6e | -16.62103 | -57.22076 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a0f19adc-cf7e-3f4e-9258-4d0884598f24 | -16.61826 | -57.32508 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d909c780-3138-3500-9093-fd494ff59da2 | -16.61454 | -57.32437 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 70c3b191-d61f-3cd4-9090-452d4867d08e | -16.61334 | -57.24302 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f1ee74c8-6f87-32bf-8e0b-6befd7fb626d | -16.61254 | -57.24761 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e69309bf-0177-3260-94b6-4f5e5b6a3165 | -16.60803 | -57.2515 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b46ebdb2-f667-39a6-bd7a-7c94f564fd89 | -16.60723 | -57.25613 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 0f812b2d-efd0-3682-9170-41499dc096d3 | -16.52208 | -57.29489 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| daec024b-7c8e-3bc6-b287-81a165d61396 | -16.52127 | -57.29954 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2eb6999f-268e-3b22-bd71-6e9bd6d03f50 | -16.52026 | -57.2923 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 52219079-f81b-3414-b530-6e039a0deb1f | -16.51943 | -57.29693 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fb2a241d-9ef5-31c5-b762-9151a6186cda | -16.51464 | -57.29349 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| a0a2a2d7-de47-3fd9-9b64-1a0b168a20f6 | -16.51383 | -57.29813 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| f3eeba4e-bb03-32a3-a063-c86c2cfe07bd | -16.51322 | -57.31013 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e929e0bc-efa0-35bf-bb89-36f962428ed3 | -16.51282 | -57.29092 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| e594bec9-3207-3bad-8756-d3060b9e86b3 | -16.51116 | -57.30017 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d4f75352-88c4-32ea-9156-0b13c70ee749 | -16.50931 | -57.30206 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 144cb4d4-76e0-36ac-aaed-f0763073166f | -16.5072 | -57.29208 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 2f49586b-0f93-3b93-84df-8134a2dc7736 | -16.50639 | -57.29671 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 8a3f8d59-5d53-3963-81cf-a6774048555c | -16.50447 | -57.32995 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 44913d49-67f3-3667-b677-5354d7d2a6bf | -16.50317 | -57.31528 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9491fa42-bc63-34db-ab15-e9a250d1b159 | -16.49281 | -57.30851 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |


[Clique aqui para ver as próximas entradas](README110.md)
