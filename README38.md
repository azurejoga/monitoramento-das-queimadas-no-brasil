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
| 8ccc0ddc-ae13-389b-9328-4880133e0c7a | -6.08252 | -59.93996 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f569f26e-16e6-33da-a758-4f5e78426335 | -9.16349 | -59.6303 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdb1ae98-e764-387d-ad05-10600e8aa787 | -9.22252 | -59.65243 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82fc0be5-ce15-3751-84ae-997b047e4edf | -9.158 | -59.62963 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3b2bffd-d7fe-3017-a20c-8f5793198586 | -9.20003 | -60.82951 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d10fd455-046c-3887-9bfc-397a5b10a7c1 | -8.98905 | -60.53489 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18636d3c-657e-3a8f-9ecc-4a59e299b4fd | -8.98946 | -60.53179 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82efc186-90b6-37a1-9fe5-7f17f9120379 | -9.1963 | -59.63517 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bde6817e-0bc3-36ba-8741-0f3d33bf1b78 | -9.17824 | -59.69382 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0ccc30de-57ea-3e66-9dbf-05829c0f8ed0 | -8.9823 | -60.54636 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f19681-aa46-3014-973b-05ee959e7e74 | -9.1787 | -59.64661 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8767571-4f83-3825-99e3-2848260d83fe | -8.90006 | -60.74675 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeef6f5b-add2-3609-b617-0c736bdc72de | -9.15896 | -59.62242 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 049970e6-8563-30ae-9f8b-b0888feea216 | -6.07525 | -59.95446 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7da55181-ff48-3d7c-8656-afe7a055cdca | -6.07997 | -59.95804 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b3fac78-a663-3ea9-83e0-3b80a2f4df9f | -9.16994 | -59.62375 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9e5f990-67a4-3c0e-9964-06ed2a9e24ec | 0.96923 | -60.41386 | 2025-08-17 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4387987-2ea7-3c04-94b6-49789f3a449d | -9.17778 | -59.6974 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 47c2c49d-3b6e-38f7-8770-78a5e9023a45 | -8.99174 | -60.55405 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0168465e-fc7c-35f6-a646-f487bec38a80 | -6.07482 | -59.95749 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f58d2bf-554d-3242-8528-0fbc62ee6c25 | -7.97785 | -70.03613 | 2025-08-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fb177e0-024b-3854-a1e4-55b3c33cd070 | -9.3927 | -60.54448 | 2025-08-17 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6a4c012-1b95-3b72-b362-052adb54db6a | -6.14212 | -57.93403 | 2025-08-17 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4a101c4-0636-3a20-b865-d06ea07310c2 | -9.21703 | -59.65177 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92675552-4d3e-3467-969d-b50aa94b65d4 | -8.99378 | -60.53871 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 804a4521-86c9-3f8e-8165-e008a29461b3 | -9.18912 | -59.65226 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f561c6b-57e9-382f-b584-5129a5f4f3cb | -9.19963 | -60.83247 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad28839d-07f5-36b4-87e7-5efd59c335ba | -8.89539 | -60.74315 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de2eb26b-00e2-3d8b-aea5-29dcebec1b8d | -9.18246 | -59.65503 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 897821c7-e9ea-33ee-8188-40299afa3fa8 | -9.21795 | -59.64469 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e41b0294-eaf1-37c9-af63-688b049f549d | -6.07651 | -59.94546 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d80749e7-66d5-3b93-b0c6-642caabe2003 | -9.14123 | -58.29892 | 2025-08-17 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1039147-5412-36e6-bc90-ab582056c90c | -9.163 | -59.63393 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49ac8b1f-c0c8-3110-b0d6-ba287ecee08f | -9.22298 | -59.6489 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91ddfb52-8b38-3845-af9e-977d0ca3ea60 | -8.23928 | -61.47087 | 2025-08-17 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 058b5e50-fad5-304b-b470-97d2563fb517 | -8.5965 | -69.71247 | 2025-08-17 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1429ffe7-05d7-3be0-8b56-611ea0aadade | -13.01276 | -56.86533 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 85c04630-6658-32c3-b994-0580d1a3f084 | -5.45779 | -60.13168 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a7e46f4-6f8e-389a-b510-7a66b74e5e83 | -9.50827 | -60.53162 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e68f82a5-bec0-399f-b823-b7344f9babe2 | -9.50949 | -60.52221 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 376e107c-c16d-3039-a2a5-46b75d59715a | -9.92763 | -60.46876 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c63cd373-0ece-331c-9b2b-500cc5296844 | -9.55913 | -63.66842 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 252bcb4b-fa73-38c8-a8ac-87c0d8b6da6c | -9.50335 | -60.51938 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26edc84e-3410-39be-81e7-1f70e7551da9 | -10.5743 | -67.9442 | 2025-08-17 05:55:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f547ffdc-3f36-3d11-adb2-b57e088883a5 | -10.57091 | -67.94369 | 2025-08-17 05:55:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f15fcf9d-cc10-30d2-92ce-668816f230ca | -8.0184 | -71.2626 | 2025-08-17 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71fb374a-8e9c-3ab0-85df-58ee4f31ed99 | -9.51783 | -60.53922 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38b0eb2c-19b9-32a0-bcac-588fed5c8369 | -8.59262 | -69.71545 | 2025-08-17 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e448b3c3-3336-354e-bfe5-f39562bf1f22 | -9.51224 | -60.54167 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 344fdbab-0774-3738-b57d-63cf06774613 | -9.99772 | -65.28752 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ca81ee3-637c-3018-b79f-4610e319c139 | -8.23062 | -72.82331 | 2025-08-17 05:55:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fa6e7c8-aab8-396f-89e0-5cc0b68890bb | -9.51428 | -60.52599 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 38bf0a6c-d235-3706-85a3-f4ffd9646860 | -9.55359 | -68.5743 | 2025-08-17 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3924d43d-e3b1-33ad-8ea5-fef244e89409 | -8.59982 | -69.71301 | 2025-08-17 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a877479-627e-3a7a-b562-cfaf3f97129b | -9.38879 | -60.54852 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 095d5f7b-f661-3172-a1dd-2391632186a9 | -13.00436 | -56.86618 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b2ab543-f119-34ca-81d8-409ef69f0c15 | -12.99968 | -56.85796 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b188ce72-056c-3646-99b7-a0ee74da02d1 | -9.50583 | -60.55037 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2e25b7c-77ec-348a-bf0f-f0dd23db6c3b | -13.0126 | -56.85429 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e5ce00b-ac96-31d4-ab72-e8948d16a3e1 | -9.51264 | -60.53856 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e42a25dc-bcf2-3591-ac2d-b531c0ed18bc | -9.5047 | -60.51843 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bae54f9-d764-33ae-ae4e-ec691d9fbfdb | -8.33054 | -70.57231 | 2025-08-17 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b59dcf24-5eb7-3040-a0e9-656947b0cb9c | -9.55691 | -68.57481 | 2025-08-17 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6c60eb5-5be0-3f14-9cae-910e8c175714 | -13.00506 | -56.85989 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd15f8b4-5716-3925-b454-3791a8c53e39 | -5.44565 | -60.14469 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2532c37-8db3-32d2-9a3a-c57bf69bc35b | -9.83353 | -68.97789 | 2025-08-17 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51eb5a42-78f2-3815-8755-58f336b6b9f1 | -9.50908 | -60.52535 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 130be06a-9142-3e35-b475-e1ecfcc5176b | -9.92817 | -60.46582 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3258fe31-39cc-3afc-a44c-1bc479316a7f | -13.00589 | -56.86486 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 82f43a3d-b639-3858-bb2c-5f459c7e875f | -9.51865 | -60.53295 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15f9aced-2dba-3d3a-9e36-f3e295aadf08 | -14.8387 | -59.64087 | 2025-08-17 05:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fad16a2-d65f-37ef-afc6-863c0cca77c7 | -10.09429 | -68.45612 | 2025-08-17 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8579a15f-84c1-366e-8c11-ea722547b6bc | -9.88909 | -64.26653 | 2025-08-17 05:55:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbd5c608-b1d5-3d28-9f6f-e4800d631f52 | -8.88322 | -68.51889 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e90a9285-e0a0-3763-baa5-d8c3341459c2 | -8.88104 | -68.51169 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa8cc2c9-b042-302d-80de-249e02ef8670 | -9.53814 | -63.57414 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79a586ec-3a75-3c5f-ae84-b772151a39f5 | -12.99134 | -56.8587 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38f70c2e-7c7e-3fbb-8a9b-b4b109fe5e96 | -9.52987 | -63.66407 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec95882-4bd8-3913-85b4-00070580891d | -9.50624 | -60.54728 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22687b5b-ae76-38b1-b30b-891db9b7d73f | -9.50543 | -60.55347 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd3f6d87-9ad2-3304-aeaa-640c98465e7e | -8.02551 | -72.50047 | 2025-08-17 05:55:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e68ad328-6542-33a1-89aa-019aaf6c9150 | -9.50206 | -60.52879 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f86f1884-a0b9-37af-861f-7ad60dc8b012 | -9.39397 | -60.54918 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 236cfbf7-f0f1-3ac8-819c-e071538da0a4 | -8.02622 | -72.50203 | 2025-08-17 05:55:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dd553723-ca5d-329d-acbb-ab5adab5633e | -9.52933 | -63.66796 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fb74e15-bc09-33c3-9604-8852c2fa7656 | -10.11752 | -57.76465 | 2025-08-17 05:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86bd9c8c-676c-32e6-ad5b-03c9a62d53ee | -10.11065 | -57.76882 | 2025-08-17 05:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb4e8a9e-29e2-3fce-81be-037b41c2664c | -9.50292 | -60.52254 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1925272-0d11-3ed4-9a1b-5d5ed5a727ed | -9.55969 | -68.57886 | 2025-08-17 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18941595-b84c-3372-8254-046520d63f45 | -13.42214 | -57.03059 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1d4a701-c00b-3d13-b8c6-0784642cd844 | -12.9982 | -56.85932 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05b56939-05fe-3f72-9b9c-b8318440eed6 | -10.33974 | -64.47955 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 80ba8695-83d0-31e7-be1d-a8a498d678bf | -13.00654 | -56.85857 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e58f2762-90d5-3448-b187-c9e1ad495e43 | -5.4561 | -60.14324 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b60d826-8df1-3a6d-a0c8-d6f2b6196ecb | -5.45151 | -60.13964 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 252c0df5-3a32-3a8e-bcf2-338b61926251 | -8.05957 | -70.58099 | 2025-08-17 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 160aa7cf-bcc1-329b-8b11-0c7e7478a5d8 | -11.36295 | -61.85036 | 2025-08-17 05:55:00 | NOAA-20 | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8adb39f5-a3e6-3f3f-87e9-bd753bb683ae | -9.39438 | -60.54604 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0edf7c47-b5d0-3d0b-9537-ef2bb73209f3 | -9.50348 | -60.52788 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 845745f9-bdd1-3dfe-87cd-83bb5259ed2e | -9.76188 | -67.53404 | 2025-08-17 05:55:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README39.md)
