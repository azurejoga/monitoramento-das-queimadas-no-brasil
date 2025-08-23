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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6ef3df2-a164-3560-b24c-f9e5c24fa0c0 | -8.61938 | -62.607 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d242cb31-925f-3f49-9c10-387c4f0586a2 | -9.95013 | -60.18296 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14634489-c10c-3087-9bbb-227124d27251 | -9.1902 | -59.5919 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c692ec3-a501-3edc-b5e0-34de1c998cc7 | -10.46705 | -59.1349 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88e2606f-cb78-3067-85f4-93ff668cac02 | -9.25185 | -61.02116 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57f81efd-f8e8-3906-a2a6-e6bb9ef69c2c | -6.68563 | -58.8661 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f76329e6-6c33-38e6-8a32-62cb20d3488d | -9.17421 | -59.61342 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe61e121-09a8-3472-93de-e66895f56240 | -8.88895 | -62.4273 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aba2ebeb-58ed-3aa9-aa00-a46daade4bd7 | -5.79707 | -59.21191 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92dba423-ed55-305a-af94-86e661d4bff8 | -8.5908 | -62.62432 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d258b07-7a00-3624-b048-3e67bbbf0070 | -9.95595 | -60.19085 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 75259218-4c51-33b3-9019-fb3bda272fb8 | -7.29418 | -59.63317 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69e20b26-aa9b-3859-9279-12d783023960 | -9.19043 | -59.62298 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0b7403a1-5521-3a6c-973d-ebe382add3f3 | -7.94937 | -63.04453 | 2025-08-23 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dadf9eb2-e8e1-3da8-b0c2-35aef2f89091 | -9.20928 | -59.61681 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6b3c318-cc59-3c28-b255-1b9deaee874b | -7.80835 | -63.56309 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b958089-42f8-3fd9-a083-734eca0e519a | -7.50399 | -63.83517 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e02f2b36-b396-3bb6-b0b2-ad63fce059fb | -9.14866 | -59.50747 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 71b4f4e3-f57a-3a5a-98d8-da0c0c4898bc | -6.88112 | -59.89457 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3cd0ca8-6807-3cf1-94e6-9b1cd82b5665 | -10.71294 | -62.74004 | 2025-08-23 05:42:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6517212-8735-32bf-b493-3a86a7176299 | -9.24964 | -59.61789 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3d2b20e-045e-3d92-865b-5bf49317e92b | -6.68402 | -58.86 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 771589f9-097b-3890-98cd-915c3df408e3 | -9.25504 | -59.77454 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe739ef0-21ec-395c-aea9-e3ee0b7b0353 | -6.6885 | -58.86061 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 717db710-fb64-3240-946b-84f5963590e1 | -8.46579 | -64.04769 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e22f6b41-bb41-3002-b360-9d163cea424a | -9.18007 | -59.66572 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af36cb0b-f55e-38cb-b181-dbf3da330cf3 | -6.68784 | -58.86505 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e17c916d-89b0-353e-90bd-0ee24fa3a714 | -6.87897 | -59.8196 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c0d74a4-af2b-36f9-9059-8b032471ec0b | -7.5074 | -63.83569 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24cc0fc0-5a4e-3da5-aeb3-d8d2aaeae949 | -5.80509 | -59.21738 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7825307b-f9a6-3e69-bc01-40195182fa0e | -6.68177 | -58.86101 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 316bfe2c-2b09-3094-988a-8cd43a6787d4 | -9.95502 | -60.17944 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f0ee6943-29f8-3c6a-b305-c0b0ce9da2e3 | -9.00876 | -60.51962 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7abd49b6-828c-3355-84ab-faf8cd59725d | -9.46482 | -60.37856 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b62638a-197a-3189-af2d-abfeb1e272b3 | -7.51081 | -63.83622 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0966c0bb-bdfd-3291-8cd0-2cd6e8d63b32 | -9.2176 | -60.79646 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 969b4a5c-f3c7-3bd9-ac9a-f2bbf57dadc5 | -10.02045 | -64.8413 | 2025-08-23 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec1365ba-3426-3889-a716-4ec20e02d6c8 | -11.32915 | -55.22054 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b460269-8c53-3f55-b316-acadb0a1b6c1 | -9.22455 | -59.7634 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56428a44-bc16-31ba-bcfa-819899393f4a | -8.59506 | -62.62064 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf9d670d-02c0-3125-8f29-3db465d21727 | -9.94643 | -60.17826 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f19b39d-8ef7-3e4d-aebe-c209d199b488 | -8.61511 | -62.6107 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 713fc075-ad19-3988-8fd5-20b658aa747d | -9.95131 | -60.17472 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 580bd3e0-55d4-3270-9999-7583d42bf451 | -7.54659 | -63.85305 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d28c28c6-5a66-3693-8c7a-70ff02f44d0c | -5.87781 | -57.7583 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8cde474c-365f-3067-aca8-903a0e3e1f11 | -7.62434 | -63.48607 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f027bed2-1e9f-36bb-bc68-7936a72b3dee | -7.30333 | -59.63044 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 051f62f6-f2d1-3ead-a279-62bdb1bf7aeb | -9.16346 | -59.59419 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7a09659-d5d1-32e3-812b-e8614c69ae4d | -6.90202 | -59.8978 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f92eab31-6c20-3742-8734-40fd7d2f8f0e | -5.8722 | -57.76033 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38fb47f0-f73b-3d22-942e-79ed7850f6d6 | -5.80824 | -59.22601 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16cdd892-9efb-34f4-a1b3-066a39804b32 | -11.19618 | -55.03402 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1eebc96-f163-3dad-94f6-7b8c97639fb2 | -9.64878 | -59.64931 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 068d3476-5c87-333d-8d28-835f12da5d07 | -9.81809 | -64.26887 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad89136d-e5c6-3dce-91a9-ab1a2e72887e | -7.10062 | -59.77718 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a9dd090-25d8-3ed8-9e3e-36f7020d8e9a | -9.16979 | -59.708 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5739887f-5d48-3662-a861-914d7961f1b9 | -11.11307 | -62.66566 | 2025-08-23 05:42:00 | NOAA-20 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7bc419c-2972-3de3-871a-8d744884ecd3 | -9.81467 | -64.26834 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6fc274f-6b83-3a70-92c5-ce8d6288abf0 | -8.69248 | -62.86464 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16fe192d-460f-372d-8ce8-6ce1378a66d1 | -6.62844 | -58.53954 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26e09316-b32a-3c95-88e0-c01f3e303e9e | -9.19881 | -59.44237 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 929e70d2-939b-3747-9e45-8ff0624df4cb | -5.7916 | -59.21934 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 075fdc54-761c-378e-8a26-638522474085 | -5.43467 | -60.16113 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de8f0c9c-4bf3-3c78-a505-20efb487f959 | -5.74595 | -57.58759 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| b00259b9-3cac-3a64-b4d8-3257fbc92515 | -9.50167 | -60.51702 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 679cee29-d7bc-33b8-91f5-9b59e097b625 | -5.74038 | -57.59207 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3625e2d9-a60f-3a20-84f0-41276aab21fa | -7.80665 | -63.55119 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5fb1c49-5743-3cef-bc23-e91708059714 | -5.74442 | -57.59815 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c6fdf974-6d52-35f8-bd9a-59d8f0f11ae9 | -9.18365 | -59.63963 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85a1addc-ed09-380f-804e-611be9f62a5f | -7.54716 | -63.84937 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cd4bfd2-1783-3db0-986c-6bdb7b4ec397 | -11.32303 | -55.21989 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53e08879-b941-3fe5-bf55-2d308e930455 | -7.81642 | -63.55655 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bee15d82-23f7-3873-b2f4-36f918b67ec5 | -9.8141 | -64.27208 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09112eaa-0b79-33a3-965f-9f3d2c3751b7 | -9.82151 | -64.2694 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0fbd0bc-c2db-3173-98bd-087a9d05c70f | -7.73104 | -67.05724 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30e50e4a-d850-38f2-9bc5-31fa270b16dd | -7.05482 | -59.82431 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0751787-54e4-386d-ac45-7e7722274ed1 | -9.19936 | -59.45853 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32faa9c2-a328-3d12-8f8a-c7aed8a34e7f | -7.79575 | -61.5802 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25302922-8efa-382d-be12-209454e54664 | -9.18245 | -59.64836 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afd19c50-814d-3669-925b-9ecb2aba18d4 | -9.64936 | -59.64511 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5af70c38-4f03-3f95-b5e4-ba51ebb5bbc8 | -10.42156 | -64.42045 | 2025-08-23 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2cac39e-ff4a-37a5-87d3-b4f15b2c3be6 | -9.64819 | -59.65354 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9ef022f-e212-3e92-b9c8-bd10e0faec02 | -9.51715 | -60.55806 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff22f75e-c04f-31ba-8ac6-4bac7c9c6a51 | -6.62777 | -58.5414 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1ed3e02-c1a7-3f04-90d0-dcaf162ec1e7 | -9.94418 | -60.18078 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5abbe44b-11d6-3e4e-903f-b93cb4a3032b | -7.5534 | -63.8541 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8437b9dd-e668-3077-b7d5-55ee87ea13b3 | -5.14837 | -62.51394 | 2025-08-23 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a3bb882-5a69-3e84-86ca-09b7b2d4cf44 | -9.18924 | -59.63161 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4ae8904-2de4-3a5b-a198-e79f97c441da | -6.93876 | -59.64318 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6716dc8d-e3fa-303c-a239-db870490f1be | -9.95324 | -60.19179 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 5d17b5f3-3c3a-3cc3-8438-36c8f202e94c | -9.17077 | -59.60226 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db4212b0-07fd-33b0-9f6a-bbaed02c1b46 | -6.31321 | -59.8728 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d81acb7-d400-3e09-84c6-890ae2c4ca75 | -8.59143 | -62.6201 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1954a648-5af7-3ea4-b4bf-0ce18c5cf018 | -8.60702 | -62.63969 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7e6eeb2-4b3c-3fdd-8bae-bc5a627dfa54 | -9.10388 | -61.43471 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae51cc57-9ccf-37ab-b732-909be4a8e098 | -9.19689 | -59.45572 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f283dde4-1f16-3a3f-bfab-b66983458aab | -9.16959 | -59.61093 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d72540e-3bbd-3f28-8cb8-9f62df732671 | -9.95561 | -60.17533 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70d9d152-2b20-3320-be6a-0f87e2264abd | -9.51109 | -60.51051 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fdfc8a1c-549e-3a95-9989-9ab9dd27d47e | -6.47315 | -55.88513 | 2025-08-23 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README80.md)
