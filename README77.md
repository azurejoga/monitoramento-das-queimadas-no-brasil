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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b5494ae-9bcd-3ab6-ad51-9b3cf1f07dd7 | -5.42443 | -60.16755 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a37c77da-bff2-3c65-8d6d-e671e7481846 | -7.34837 | -59.66242 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec1c9805-16b9-3de6-8b08-12801a40afe0 | -8.67285 | -66.58851 | 2025-08-27 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 465c8d32-7478-3597-8403-f6d7dd9fa867 | -10.09462 | -62.89253 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 881233fb-f4fb-39a4-8163-cf714f19bf81 | -9.05042 | -65.72525 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc7dda10-0f7f-380e-98dd-2e72cc675db4 | -9.28365 | -63.72263 | 2025-08-27 05:46:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87ea0b4f-cc57-3903-8015-ee0c0b4113e1 | -14.76742 | -59.73029 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a3a6027-d508-3ed4-be39-02878ecc843b | -8.93753 | -65.94349 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c088d59a-6866-351e-a801-659f78222a2f | -10.42937 | -64.80979 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2e551a4-6cd4-30a1-9236-b96424688c40 | -9.82959 | -64.28813 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 803fb4aa-4f52-34ec-b9de-8076d4d2dc6f | -9.02272 | -65.72799 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e4f98039-bf43-3924-a2d4-d786ec42f169 | -10.09337 | -62.90096 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f8c8d28-ce2c-3493-ab52-2ca26641baf8 | -9.79488 | -64.24104 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6762244-721a-365c-b735-95dc45be163f | -8.99451 | -65.41566 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b250604-f5cb-37b3-a071-23070e60c7e8 | -9.79433 | -64.26751 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 984a6b46-5764-3764-a051-8c81aaa99f1c | -10.08674 | -62.89579 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a3d8465-6bc8-37d2-ba0b-cc917a1a3760 | -9.62156 | -62.26484 | 2025-08-27 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b613b40-c4df-33c8-a154-7d1c7f102be0 | -10.42295 | -64.37369 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a7862e3-9698-39d2-81f1-946002f9e1f3 | -10.31711 | -68.04807 | 2025-08-27 05:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9db53753-3e15-39a1-8d4f-c3f362b3d883 | -9.89385 | -64.09147 | 2025-08-27 05:46:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5ca752b-8190-343c-bf89-92cd991578dd | -9.07814 | -65.71883 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9539e93-0569-3faa-8c73-e0b63faa4aa8 | -10.47102 | -64.46761 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c2f878a-5843-3899-a8b4-fa81cdfe67ab | -8.93642 | -65.92899 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06414172-ed4f-348a-8bf7-395f95b288df | -10.2962 | -64.49448 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0e59177-e455-3997-85a2-cc9b3bc05345 | -14.77372 | -59.72693 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6270611a-0c73-3040-a854-dc868e6beef1 | -8.92354 | -65.93072 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70dcf318-0697-3ef8-9c30-eca5b1f90e3e | -10.27694 | -64.50658 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af7ff7b2-50fd-32e7-97a2-5efdc059a748 | -14.76839 | -59.73137 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e5f8c667-768e-3110-a50f-e43312d462a9 | -9.01715 | -65.69846 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f464be13-0fb4-3bca-9ac9-fbea03194371 | -10.09399 | -62.89681 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbf8d29c-a44c-3db1-a642-f73ab1331ae2 | -10.27125 | -64.49817 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bd60c080-08ca-372b-92cb-09c3526d9d27 | -8.92853 | -65.94226 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ff50133-0c00-3f4c-a5ca-d9905bc61e4b | -9.02549 | -65.732 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b090400-26e4-3e5b-9df1-a6bd345ba0f6 | -9.06334 | -66.07103 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a78694fb-ea5f-3897-a5e3-79fe32199893 | -9.14082 | -65.28053 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ca91106-2950-30e9-84d9-97b88fecee71 | -8.95915 | -65.97919 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d102860-82b8-3d87-820b-d5297f7e391f | -9.80741 | -64.25059 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 932dee42-663b-3bcd-bc9f-ba8ace5c368c | -9.66027 | -65.00346 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccae2621-6912-3638-a15a-ef2a76232a13 | -8.96303 | -65.97623 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0fbec0a-e4fc-342d-87b1-f271d41fbaa2 | -8.99784 | -65.41618 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8cb66d0-2420-39a3-b411-431065f4860b | -10.09036 | -62.89632 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a716cdcb-b60c-3dae-9abe-a59207c2a98d | -10.09099 | -62.89203 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d791a44-e69c-3e6a-ace7-8dfd13fdf428 | -9.67213 | -67.50033 | 2025-08-27 05:46:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b2add39-c3c2-3197-a1e7-6409b32d96c5 | -8.92742 | -65.92775 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef5f90dd-f566-33d8-a5e8-ca90fa3bb1cd | -8.93532 | -65.93597 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db50c0f8-0b99-367a-a603-fe785d46154b | -9.25214 | -65.62451 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87f786d3-4355-3dd2-bb2a-788211641aab | -8.96469 | -65.94425 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd40cf0a-9347-3674-bc76-627c20829861 | -11.70184 | -63.67204 | 2025-08-27 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de9f06c2-6c5b-39cd-b1b4-d41665a08dd9 | -9.0177 | -65.69497 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a18857c-804c-3963-b33a-aa71880883e9 | -9.28769 | -63.71935 | 2025-08-27 05:46:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2023e604-c650-3ece-8e11-139c155d1d20 | -8.96469 | -65.96575 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a8ef617-a2d9-361a-a914-e5e503450058 | -9.25159 | -65.62801 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6adf9113-e9e7-34fd-b04d-a18a310b8529 | -9.28422 | -63.71881 | 2025-08-27 05:46:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5fbc75f-46a9-3598-b305-b1a6c297b77a | -14.77218 | -59.73045 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90cdd120-994c-390e-b8de-37a87de1c866 | -9.06371 | -65.72737 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1eee69af-4aab-3cf7-b877-1653d07d5c13 | -8.10427 | -71.25209 | 2025-08-27 05:46:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dd8681b-2194-3e5d-819d-b21adcabb1cd | -8.92409 | -65.92722 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd521f74-e320-3ba7-bfc8-482f64e9846d | -10.77133 | -60.78615 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e90ae5fb-1e42-30b0-8b4f-60317bbd23d0 | -10.58062 | -68.38094 | 2025-08-27 05:46:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f70c4928-0d9f-3043-9fe0-9554617c6d65 | -9.65747 | -64.99938 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b88493bb-028b-37bd-9759-8d711d7abd52 | -8.94031 | -65.94751 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2323b44-f530-30e2-8701-2f79ab5f01fe | -12.22411 | -64.22804 | 2025-08-27 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61c21d7c-ecfd-383b-aa06-d00ca023ae6e | -9.0783 | -66.06267 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fa22da9-5859-3ea7-a14d-46fa6340be30 | -9.04987 | -65.72874 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7619a55b-3706-333e-ac5a-cd945c406bc6 | -14.30567 | -60.35429 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54245588-98b7-3d54-a981-4f0c9a77e45a | -8.9525 | -65.95663 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6f1b0734-0443-37b2-9c91-6e26c63981e6 | -14.77471 | -59.71083 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 621f8db6-3a02-3333-9c50-ed3cf1703bd7 | -8.93129 | -65.92479 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac4dcb44-2f7b-387b-ae32-3c4591acd43e | -9.02268 | -65.68501 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da180085-7eb7-3ff0-8bb2-0db1f95ae264 | -9.00614 | -65.40674 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d4ef9d0-36f0-35f1-aebe-7183c71407d7 | -8.95638 | -65.95367 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 2fb726ba-42b8-3bce-8c15-abf2cb71794c | -9.80514 | -64.2654 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06618b73-d8c9-3b67-b8bc-386a402bfcd4 | -8.96026 | -65.97221 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c1f11e9-56c0-3e6c-be29-88b6c67fcb22 | -9.13859 | -65.27296 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30789d79-9c42-3d41-b17b-e68d83075f81 | -11.31924 | -55.21335 | 2025-08-27 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3caa5008-897c-3a63-aecd-0d6bad22e185 | -11.30692 | -55.11015 | 2025-08-27 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcc0f917-4831-3861-a1c1-85053a9e73ba | -10.77907 | -60.79107 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec72680f-5068-3c2d-991f-7225aca2bf5a | -9.01826 | -65.69147 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41b7a058-a92c-3a94-b43c-80172c84a91c | -9.75751 | -67.53269 | 2025-08-27 05:46:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 283e9fba-990e-3472-af07-81544a68a33f | -10.01079 | -65.03284 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4caa58dc-b0d6-3c99-b6d8-96cefd870e5b | -9.82618 | -64.2876 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f1e39a8-27fd-3c6b-ad49-e8bca960fc89 | -10.09577 | -62.90974 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2db956f6-4cd0-31c1-9e7e-f39a12f5ae23 | -10.24628 | -59.66334 | 2025-08-27 05:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40652a3b-cd0d-3766-917c-ce8c3915e3fe | -9.79489 | -64.26381 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cde9d97a-f981-3779-bb26-d498281298f6 | -10.79418 | -60.78461 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ef49fe1-d177-35d3-84e3-6cc7ab123c09 | -9.02435 | -65.69602 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a96677b9-5256-3d59-8ba2-b57b4ffd6723 | -8.92686 | -65.93125 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c0202b3-eb47-357c-924e-91ec8fe0b2a2 | -9.7983 | -64.24158 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 141fbd24-292d-3fb1-b5cb-d5e6d806751e | -9.02882 | -65.73254 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f05dd6a1-c621-35bf-b36a-002a9432c2ff | -10.08975 | -62.90043 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e07afb8c-074e-33b6-a088-2052adb720ab | -10.09825 | -62.89302 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e348c8b9-cbe7-3304-9c57-3187e75ea90a | -10.27354 | -64.50605 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad7094d9-03e5-304e-8467-56f979917500 | -8.99506 | -65.41216 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ba3bd7e-85f0-37c9-bba1-ae9ac60bc409 | -14.31144 | -60.38031 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd4bcfe6-2506-3174-9f94-9d51732927e0 | -8.92077 | -65.92669 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b518494-34c7-3f63-839a-66a0c9ebedea | -10.2775 | -64.50291 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43084538-18d8-36a2-95af-1f057c39e7f9 | -9.04709 | -65.72472 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f01670d-7f78-3d09-adcb-4e987c710ba6 | -15.62467 | -52.73382 | 2025-08-27 05:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 938b8c6a-03b9-3304-865a-75a9e0f6d384 | -11.1898 | -62.64585 | 2025-08-27 05:46:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abfb2b12-0854-3096-aff6-37ccb2bcc1be | -14.77339 | -59.72106 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README78.md)
