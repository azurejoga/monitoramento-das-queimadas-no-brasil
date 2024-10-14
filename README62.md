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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79114c3d-5f86-3699-ac05-bd3bb575ada9 | -17.01091 | -57.41227 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 07c2f6fd-5879-384a-9e4a-809978c16927 | -17.01011 | -57.41607 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8e44f00c-875d-3c03-b1df-3abbbeffdd7d | -17.00932 | -57.41987 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 13c5d330-5dcc-38b2-9044-310cfbf1357f | -17.00923 | -57.44785 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ed5e4d35-d4db-3f15-a7c2-46d440042977 | -17.00852 | -57.42368 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 44345309-528a-303a-a378-fcbe15aa2a72 | -17.00842 | -57.45169 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2b325cbd-0f47-3c6e-b3da-ffcb9ec2a7fa | -17.00772 | -57.4275 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 12a1d087-52c9-3865-a9f4-3a5b997e54ea | -17.00692 | -57.43132 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ff111af6-30e9-3e87-bfac-f477a70fa390 | -17.00611 | -57.43514 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5be1fcf4-098a-3621-843f-09d8e4126f66 | -17.0054 | -57.41103 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| bcddba69-07b8-38ed-9320-e1b2fa19ec4e | -17.0046 | -57.41484 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bd358dde-e73d-30c7-b0ed-98f876749dea | -17.0038 | -57.41864 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4fb7a362-9f54-3d47-95c3-1aba6b368d48 | -17.00359 | -57.47477 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 40bdb07d-bda3-35d2-b6c9-2277ea647249 | -17.003 | -57.42245 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4e658c21-2b9f-330a-ad4e-aea796921cfb | -17.0029 | -57.45045 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 751e8148-4f94-308e-84f8-717b45263d01 | -17.0022 | -57.42627 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| beda3ab0-5e84-3952-9602-735aae66e141 | -17.00209 | -57.45429 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f48bb9ea-1bea-3993-b0fc-dad12f0d2910 | -17.0014 | -57.43009 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b5e88355-e8a3-38ff-a947-02f0e1582d86 | -17.00129 | -57.45814 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ea13e152-efc4-3384-a44c-e5ac03b0d230 | -16.99989 | -57.4098 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0f800fee-b9ba-3b23-9b8d-2426a273f120 | -16.99967 | -57.46582 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 377c73a8-d5a4-3020-99a9-c54acab18295 | -16.99909 | -57.41359 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 168fbcd9-6be5-3c11-a294-cc023cafeb1d | -16.99899 | -57.44154 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 78ef5391-2fb5-3cc6-9b29-c9cb1f256198 | -16.99886 | -57.46967 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 43d91f26-0e1f-3459-8039-809c3fe41455 | -16.99829 | -57.41742 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b21bb82b-ee62-316a-84de-71fa69289675 | -16.99805 | -57.47352 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c3d30697-0197-30b0-9897-fc36e234980f | -16.99748 | -57.42123 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 97cea044-db60-3232-ac8e-fd37ce0e0640 | -16.99724 | -57.47738 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 35c679ed-66d6-37b3-9b67-824e939c2991 | -16.99668 | -57.42505 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e983c15f-9450-3abf-ba70-807d6d4118cf | -16.99587 | -57.42887 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1bcf1fd7-6a66-3a0c-a998-6cf68997a017 | -16.99438 | -57.40855 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 38aea379-06eb-3969-b22c-450f06fa49bf | -16.99358 | -57.41236 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 40397cd5-7876-3add-b1c1-49327dc2d761 | -16.99347 | -57.44031 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a5abbc1f-e2f7-3aac-8095-83d50a6c7c7e | -17.95601 | -57.36382 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| da29342a-11df-3070-8f34-823e7ee9bc5d | -16.99277 | -57.41618 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9300f471-4e80-36cf-9e8c-f900e1208ddb | -16.9909 | -57.47999 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6cc01a3d-cf0e-30d5-a723-11d3fe621d55 | -16.99009 | -57.48383 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 441b1c39-5a08-3b64-8b8c-02c65bfa814c | -16.98928 | -57.48767 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| af749752-bcae-3c31-bd1f-102b2a0a1205 | -16.98374 | -57.48645 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8f7297b8-3cae-37b3-90ea-4dcafc31afb6 | -16.95111 | -57.50343 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a7e6fdd4-5112-33f1-af3e-49eb010b3e56 | -16.95028 | -57.5073 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| aceb39dc-88ad-3c67-b4f6-17863e93f9d0 | -16.94946 | -57.51117 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 732737e5-552e-3d39-9d1c-8879b04a7387 | -17.87661 | -57.3842 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 304.5 |
| 8c941faa-b86e-3e68-9599-7262ef13c61f | -17.87584 | -57.38784 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 1fe9312a-9238-387a-8b7d-c9be1af12748 | -17.87275 | -57.37563 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d6477c6e-4aed-3b57-a154-8e7d7d1f949e | -17.87042 | -57.38661 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| fe42c1e2-afef-32c4-ab50-f23e735b98a3 | -17.86965 | -57.39027 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 72d9bc29-eaf7-30d1-82b4-a503a12e752d | -17.86887 | -57.39394 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 4c1ff425-8df3-302b-8806-25ad8b14e1dc | -17.86812 | -57.37071 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3047cfe4-3405-3cbe-91e6-715977110d3b | -17.86735 | -57.37437 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6b6aa40b-818f-379d-99f1-40f9cc214b64 | -17.86657 | -57.37804 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| b26478b9-796e-3696-851a-3c5b71ea0629 | -17.8658 | -57.38169 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 268509e8-654f-35a7-8fc9-dcd95e2633b7 | -17.86502 | -57.38536 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 0edbc3c1-b5ba-36ab-8b29-f916f7175c45 | -17.86424 | -57.38903 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 677dd6f9-5def-324e-aede-764f04afdbf0 | -17.86346 | -57.39271 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 4ca6ba6d-e7b3-39c6-a554-4d6ed9801376 | -17.86195 | -57.37313 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 473c6979-86da-33c2-87d2-bf1c401b0403 | -17.833 | -57.37038 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 518e166d-3fe4-3e27-b10a-e0683e80d826 | -17.82871 | -57.36944 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| f6ea1d02-1529-3cd2-a600-b205f21001b8 | -17.82792 | -57.3731 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 62ae9739-7094-3e0c-8bcd-69e36508704f | -17.82759 | -57.36915 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 6277a575-a948-3621-acd1-86957d11ba74 | -17.82683 | -57.37281 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7dad6587-e224-3295-afc1-7465f7d0fbaa | -17.83176 | -57.38167 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 211f52e9-59b6-314c-b168-a2849b7c1b93 | -17.83072 | -57.3814 | 2024-10-14 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d792ad85-7a25-3014-b839-5b776ec81c30 | -17.20358 | -57.4766 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 80b6640a-d0c1-3b29-a1a7-b7c31242d482 | -17.2029 | -57.45248 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 281621b5-926f-36e3-8f72-f33396535892 | -17.2021 | -57.45628 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 86d11106-ee95-35c0-9a11-29b9338f50a7 | -17.19901 | -57.44365 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| be643f73-58db-3b64-b0a8-6f5562975ee9 | -17.19887 | -57.47153 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 7d00da7d-427c-36ee-8ad5-9f2b6dc1d9d4 | -17.1982 | -57.44744 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 456df038-7335-3d87-8ea6-263779dcc22d | -17.19806 | -57.47535 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ce7e4419-4912-3cc4-a00d-d12982786cd2 | -17.1974 | -57.45123 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| f41d4327-e633-336a-b11d-4f58b410d6d8 | -17.19726 | -57.47916 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 11da59c6-20b7-3c3e-8c41-8d6a8ae75d01 | -17.1966 | -57.45503 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| c0394d61-b695-3404-863e-a339a6ef5255 | -17.19579 | -57.45886 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 5847d4f1-4dcb-356c-aa2c-b0565be3d260 | -17.19431 | -57.43862 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.3 |
| ab5a962c-e063-3db3-b3e2-c1be45f8757b | -17.1935 | -57.44241 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 4e1d31f5-85f9-31cb-8005-22ea60752ceb | -17.1927 | -57.44621 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| c15e378b-454c-3520-abfc-06a4fb190094 | -17.19189 | -57.44999 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 74954e71-6ef7-366f-bbd2-0f700bb5608a | -17.19175 | -57.47793 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1c7060c1-f30b-3d50-892d-4c45f8a0ddd9 | -17.19123 | -57.426 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7e89217b-acc9-361a-a985-2457d2d51fd2 | -17.19109 | -57.4538 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| fa61ab87-b222-3387-a369-1da768286680 | -17.19042 | -57.42979 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6e6542b8-14b1-36a7-ac5d-c79fd23669de | -17.19028 | -57.4576 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| e58c13a9-f76e-3a3a-97f4-94e7bdb8740c | -17.18881 | -57.43739 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4a052dcc-5b9b-35f7-9ca5-ef227b98dccf | -17.188 | -57.44118 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| a33414d3-1a9f-3382-8042-3ad51df075ef | -17.1872 | -57.44497 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b10a4892-bd7a-3714-a34c-7e65d025db34 | -17.18654 | -57.42098 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| fafe8cac-43fe-3a1b-a0ed-834437e6c9f8 | -17.18639 | -57.44877 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9242af16-cfca-397e-a8f8-8ec42bbab487 | -17.18623 | -57.47668 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 92d2af46-9bd4-392b-8245-79c00c129ff7 | -17.18573 | -57.42477 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 10024797-a4a2-3b89-a9b2-80ffcfbc7ac9 | -17.18559 | -57.45256 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f01b1a1c-9dbf-3213-a24d-30ca9b148177 | -17.95218 | -57.35528 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2712f82e-a77a-349d-b809-fcc2454d950c | -17.18492 | -57.42857 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 03748175-7153-3174-afca-2881fc9b6ab7 | -17.18412 | -57.43236 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c7285ba3-3e54-3b3d-8a83-7bb92cff2ae6 | -17.18331 | -57.43615 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f1e6ed5a-de9d-34c4-8249-feb05b16e585 | -17.18185 | -57.41596 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b39744fa-6e41-3356-8d6c-d9c46d583d69 | -17.18104 | -57.41975 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a56a7a2b-242e-3d1c-88b7-351d3d7e2730 | -17.18072 | -57.47545 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 39675a2a-bfa7-3a9a-b650-e5aae581aa0f | -17.18024 | -57.42354 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6c34d51e-87ed-3e5b-b1ff-3ed4ff76e752 | -17.1799 | -57.47927 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |


[Clique aqui para ver as próximas entradas](README63.md)
