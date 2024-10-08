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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b99d053b-691e-3a93-8780-7640eddc672a | -16.69386 | -57.44389 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 31f73b91-7b9d-3faf-b216-29fb50a58fd7 | -16.68806 | -57.45155 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4dadb6f0-5c49-3428-a76e-234aa669e0ef | -16.6787 | -57.13188 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| fbba1dba-247a-3744-b910-16e8f3bac4f2 | -16.67336 | -57.1356 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| f3f6419b-d7bf-391c-9743-a2bfe7692ba4 | -16.67247 | -57.11629 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| 6ffce5f8-523b-3249-8ae7-4a1af063b2c6 | -16.67158 | -57.12088 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 650c6a96-9500-37a3-a2ea-e4d58378851b | -16.6698 | -57.10618 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 764d7df6-aefc-338c-968f-cbe6f0db3dc0 | -16.66891 | -57.1347 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| f6aac6d9-d7b4-3098-89c5-6e4f2da7c4fe | -16.66802 | -57.11539 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| 77862db5-0866-3265-a8f5-73f0b713d291 | -16.66535 | -57.10529 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 215f01be-85fe-347f-89ad-39818f3bb4bb | -16.66356 | -57.13841 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.0 |
| 397ce089-cd7b-36cf-a96f-c9f54f699ffa | -16.66178 | -57.1237 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| dc3e10ee-24a7-373f-a89e-ba7307fab1dc | -16.6591 | -57.13751 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 600665ff-012d-395c-8b61-ada447e71f0b | -16.65821 | -57.14213 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 2948ad7a-66a3-3aae-a667-cff0c7bcbdc4 | -16.65644 | -57.1274 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 7434ae33-7131-3823-9b9c-6145921c7de4 | -16.6875 | -57.45261 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 280f1140-d19e-32c6-8206-62b52348ea54 | -16.68313 | -57.10889 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 62f1a8a4-1e5b-3483-99d1-8737e9705079 | -16.67957 | -57.1034 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 273f37d4-e29c-3691-a313-b40dfd351725 | -16.67513 | -57.10249 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 6a5a42bf-b01d-3671-becf-7ecad4a3c91a | -16.67425 | -57.13099 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 47f9d43d-bbc5-31e9-abbe-06dce7beac1e | -16.67158 | -57.09701 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6b8465ca-aa43-3cd6-aea7-5f326ea0c62c | -16.67069 | -57.10159 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| f427b831-92a4-341f-98d8-db363e81b304 | -16.67068 | -57.12549 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 41f26415-df9b-3233-bbb7-3913071ab7cc | -16.66979 | -57.1301 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 9245e019-3dee-3ccd-98f7-12300d80ca55 | -16.66891 | -57.11078 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| e5d10aa4-8800-32aa-9998-64b19c465f07 | -16.66802 | -57.09152 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f36f757c-cb16-3bfa-9ae5-b2fe858e20c3 | -16.66801 | -57.13931 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.0 |
| 62221428-87ee-3e7a-b9a2-e72202c0e438 | -16.66713 | -57.11999 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 4dee4065-d81c-30de-b3d4-cbfbb68604cf | -16.66713 | -57.09611 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| ffdf46d0-250c-3b9b-b16d-85241e48cf14 | -16.66625 | -57.1007 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 6edee9c4-0002-38f4-bfa4-0c0192cfd9dd | -16.66623 | -57.1246 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 5f5e0e2c-5c57-3a56-8354-5302bcfcc8b8 | -16.66534 | -57.1292 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 9fc9a0ba-91a7-3007-8533-95ef3dc4cf59 | -16.66446 | -57.1099 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 6ab8131a-eda7-33f9-9637-00799ad4b1e1 | -16.66445 | -57.1338 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 11d972c7-27a2-3617-92ff-52049c36cab6 | -16.66358 | -57.09062 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 46af47c5-d906-3c56-9acd-dd374c9c2f02 | -16.66357 | -57.11449 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| e8d77d6a-aba7-3c48-af5c-3c1c348b0eb4 | -16.66269 | -57.09521 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 507aacac-b992-3ae5-9991-4df72dc8102a | -16.66268 | -57.11909 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| e17df37c-d81c-32f5-8923-3f460901beb6 | -16.66117 | -57.0874 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| cf26de24-e2e9-348a-87e1-73cf0447bfb1 | -16.66089 | -57.1283 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 3aa2bf7b-e08f-33d2-924a-62363cc7098e | -16.66003 | -57.08514 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bfc67847-134a-3ae9-9a82-e17e37e6f906 | -16.66 | -57.1329 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| a5f47779-b28f-3081-baad-611c6b7180ff | -16.65554 | -57.132 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 0ec05d80-089a-30a8-83fc-4328d721f11c | -16.65465 | -57.13661 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 9e6e913d-326b-3a1b-9440-4510bdeb5da2 | -16.98982 | -56.69463 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a9f9e913-5e35-3d54-a56a-f5b64289bd1b | -16.98901 | -56.69891 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 76e634b6-2674-3135-bdc3-c0bfc4bab651 | -16.98307 | -56.70661 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0e161ecc-20f9-3f23-998b-fc7b88214200 | -16.95861 | -56.76428 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 606624f5-362d-3ab7-8958-9570e338f9a4 | -16.86692 | -56.74282 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c0dcf664-38e1-3874-af31-f80c22ac5ef9 | -16.85459 | -56.71338 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 49a56270-8f2e-320c-9085-1365e01da09a | -16.85027 | -56.71251 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 30769e2a-5245-35a6-b3ec-c2a179f8e107 | -16.84612 | -56.73412 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| be889a9e-6b3d-3a6c-98ef-b7f8a004e674 | -16.84529 | -56.73845 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4519120a-e77b-3cbf-93c7-6904d7c128c1 | -16.74533 | -56.71407 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5998e4ab-a5ed-3145-a787-78f942899fe2 | -17.74119 | -57.09293 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f629b516-e6e1-33e5-b8e8-71ab131d49b6 | -17.73684 | -57.09204 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ce1bd71d-704d-3c94-b7db-445d4168d22e | -17.7323 | -57.06813 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 945b45ea-f46e-3ca3-9e63-62368d608027 | -17.73165 | -57.09556 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8285f435-9ce3-3b94-a582-db41f6d44506 | -17.73147 | -57.07254 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| da147a3e-71e9-31a2-b95b-1ec6df6d3eeb | -17.19244 | -57.34488 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 340c423b-5172-3a16-abfd-67d3f4832550 | -17.18531 | -57.33372 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0c39f88b-17e3-3155-a02f-c723bbb7681e | -17.1661 | -56.75095 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 21f92f08-6340-3960-a49c-fb7096921c79 | -17.16527 | -56.75524 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4e8796e6-bd50-334b-bc41-672834da4071 | -17.15831 | -56.75866 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0734b033-6fcb-3660-89f4-aa2e3332c33e | -17.15666 | -56.7535 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| e1c2f000-8ccf-302c-9073-b715327ccf1f | -17.15548 | -56.97048 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 51563d7e-0577-35c4-b096-6ca62882eb25 | -17.14438 | -56.80958 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| ac66ad40-49eb-385f-a47f-e03b36607b62 | -17.14428 | -56.73798 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8b21b8b9-7e8e-3374-81a9-7b1d9f3e4d79 | -17.14403 | -56.79559 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1d3f7d9f-2e24-3dc2-a88b-3092f80a9061 | -17.14357 | -56.81393 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 1bed319e-63b5-352b-8099-3c35ce9e535d | -17.14276 | -56.81826 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 4d3695f0-d5af-3b66-9ca5-24c73af5c552 | -17.14237 | -56.96779 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 49fadf21-66d4-3e33-9d88-4be59346118b | -17.14189 | -57.42949 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9c8ccea4-892b-3a9a-adb8-d9ee29820641 | -17.14115 | -56.82694 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f6fae055-bc48-361f-b078-875ac86b7aa9 | -17.14055 | -56.79042 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e806d55b-c0f6-340c-a4e6-51ba6b1af61f | -17.13984 | -56.8172 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| ac38a05a-7293-38d5-b742-23f0741fd694 | -17.13901 | -56.82154 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 227e6df8-1b42-3bd6-9a60-3f06f5f219a6 | -17.13822 | -57.43149 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b21f0f82-0c07-36d9-9905-c7a5cc41ff40 | -17.13817 | -56.82586 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| cd0e52c3-85ea-3c66-bc85-2de0a6c10921 | -17.13763 | -56.82172 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| e7c74602-6342-3a7e-a6fd-e093e3af7194 | -17.13739 | -57.42856 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1df3bc99-7a7f-39d0-a78b-d2bfb5fa8fba | -17.13733 | -56.83019 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 55e69bf2-75db-3742-9243-29fc1d90f841 | -17.13601 | -56.8304 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 5245052f-8692-3460-824a-20162a018105 | -17.13047 | -56.84231 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b3d6e578-bd4f-31c2-8f2e-e6cbf9193ddd | -17.12572 | -56.83732 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 4c4d7404-348a-3900-a8e5-a97108d757f4 | -17.12491 | -56.84166 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 14985524-e0d1-30b8-804b-057d6ae4a902 | -17.11848 | -57.42957 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a18abb53-b088-3cda-84c8-a0f3e7930e81 | -17.11624 | -56.8399 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| aead3d05-1839-3aa6-bb8c-5d0fd5a9e2e0 | -17.1146 | -56.84862 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a882e090-353b-3c9b-bed3-eada319c09f5 | -17.11308 | -57.4334 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 89dd73a0-ed7c-3e8c-96ab-fbeb404801ac | -17.11027 | -56.84773 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ac04eac6-31a1-30de-a7f6-6858fac5e698 | -17.10675 | -56.84248 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b0341655-b01b-3b12-a908-42ac2d2e788b | -17.10593 | -56.84684 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d35e6afe-f5ab-3ad0-aaa3-77e90900b516 | -17.10324 | -56.83723 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 661af818-740f-346b-a9f1-12e02fb09af9 | -17.10236 | -57.36731 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ac93deb4-eafd-33d4-830b-be2539094416 | -17.10146 | -57.37201 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 86116d2a-0905-3b8e-8f8b-c6904ec4ed9d | -17.09808 | -56.84071 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2d1bd6b2-79d4-3587-940e-9dd040976023 | -17.09788 | -57.36638 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 450a95bb-ed80-3110-8d98-51ae1ab98c1f | -17.09726 | -56.84508 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9881aaa6-567e-3d4d-a2c4-70fdf34f27b6 | -17.09697 | -57.37109 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |


[Clique aqui para ver as próximas entradas](README69.md)
