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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e954c6f1-630e-30df-9fb7-9bd933bd148a | -12.90722 | -62.53022 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31b7fa7b-f2e1-3426-95f4-717ccae22950 | -12.9023 | -62.53465 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c633794e-e8fd-3239-b1de-ce7b92d168bd | -12.89825 | -62.533 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06fe1dd5-889f-3045-b4b4-ed682cdb73d9 | -12.89808 | -62.53406 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e8a910c-f6b8-3971-b3cd-fbb312fe5084 | -12.76504 | -62.27327 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58a0ef84-3738-3376-aae1-db78ba9603e1 | -12.76021 | -62.2768 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c7513bd-10be-35df-a9f2-fe52db588ab9 | -12.75966 | -62.28092 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dc33afd-25ce-35d6-a7aa-6bbaee5710f7 | -12.75911 | -62.28505 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdf5ed4e-3697-31f0-9864-3e6db73053c2 | -12.75537 | -62.28036 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8a4a34c-c34c-3365-9ba6-ff88b6d583b3 | -12.73452 | -62.23969 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d39e7f39-bf75-3bd3-88bb-16a11403398d | -12.73398 | -62.24379 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35d7430a-05a4-3f2c-99fa-2e4a05d75571 | -12.7329 | -62.25204 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3dab372-b0ac-3a85-8dbd-ddad420fcd9f | -12.72969 | -62.24318 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6b499c9-3602-3a7b-aa88-930e76b2f538 | -12.72915 | -62.2473 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32efdadb-fd05-3fd3-8368-e497ad99e2e1 | -12.72861 | -62.25146 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc5db5b9-7125-32d6-b627-e72b9db4f2cd | -12.9797 | -62.79781 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56c07a4a-ca1e-35bf-a504-aab3e6892f95 | -12.97241 | -62.78895 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5181b9c4-3cc6-3e84-9fad-5b48f0ecaee5 | -12.96775 | -62.7922 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b3d6ec2-e0d9-3409-8fa6-49e227d82e1f | -12.88464 | -62.79743 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05edd8e5-08b7-3c0b-9893-80d36ec87793 | -12.88413 | -62.80125 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73fa3360-2236-3a8a-9520-4b225fe25c8d | -12.84319 | -62.80786 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2edce68-dcc0-3f18-84f1-be913ce96fe3 | -12.82082 | -62.90891 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51c74291-1466-361d-a8f5-8ceb4662aecd | -12.74021 | -63.04125 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d585de74-24c3-304b-8584-3e15bec8cc9f | -12.70006 | -62.97157 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f249844-443c-333b-8b18-fad893c1fb57 | -12.50613 | -63.26874 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2acae050-9ec6-33cf-b85e-c6752496ba87 | -12.48386 | -63.00531 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a2c7e00-91ae-3aff-a740-d2c35620d0ac | -12.47421 | -63.01506 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01f645ec-16ec-3214-b67a-60f3d17b5af2 | -12.47065 | -63.01084 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9405fdfe-59f9-314f-9b4f-125915d3802c | -12.46708 | -63.00663 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a131962b-27df-34dc-b02c-e760ef436423 | -12.39957 | -63.01569 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba2472e7-c904-30d2-9fbc-26d8d55501f3 | -12.377 | -62.96906 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a85354b9-e2c7-3b62-b1f1-25094c6152c1 | -12.82441 | -62.91326 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39ad46cb-e2d6-3ae7-932a-485ba59ba211 | -12.82073 | -63.00004 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0081a454-8e32-3cb3-8b94-d7ec9bedd9e9 | -12.73614 | -63.04066 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6bb96a5-e25f-3fec-9361-11167f4d64ee | -12.71581 | -63.03776 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c76f3d6-cfad-374c-bc1c-7a576b6d75a1 | -12.48436 | -63.00166 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd46fbf4-d2a2-312e-b89a-21a9f26d1b72 | -12.48029 | -63.0011 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69ef28b9-a25c-3336-ab69-0d29af732480 | -12.47979 | -63.00473 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0213bf79-dc4a-3151-ac54-45b92f5c6f79 | -12.47928 | -63.00836 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e17c74a-150e-352b-824c-e5797076ff61 | -12.47572 | -63.00415 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88cd85ea-2222-38b1-b90c-bd6c510f6b89 | -12.47522 | -63.00779 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c78ca47f-0169-3f1b-97ec-5c285719e251 | -12.47471 | -63.01141 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7651bf34-821d-34b6-8a8b-2fa57381bd40 | -12.47115 | -63.00721 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aed96ed3-f7b1-35d6-bc77-0767d0b1a1b6 | -12.47014 | -63.01448 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd45c4d5-98c9-380a-a409-f7fc38b29904 | -12.46658 | -63.01027 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c53da3fd-14e7-33c4-a214-cd417e4c1e21 | -12.46045 | -62.99453 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e356389-5ae1-3e87-9238-a5231ec5c418 | -12.45995 | -62.99818 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 314b08e0-77f8-37d6-9666-0966d715c82f | -12.45945 | -63.00183 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a8e4ac2-8231-3667-919a-783ab9039b5d | -12.45588 | -62.99762 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f58f59c5-6f4a-3808-93f8-d5b19e00558e | -12.37649 | -62.97273 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88d53085-ba3a-32d5-93ed-f0df5d605dba | -12.99254 | -62.73278 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79865768-ea54-3657-81c6-5fe470754c79 | -12.99152 | -62.74053 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31846f85-4b4f-3dca-9d29-57ae55dd8c9e | -12.98888 | -62.72831 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0c22488-9fdf-3dc8-870e-83990e6ecfe5 | -12.98837 | -62.73219 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56d71405-4d0b-3284-8aae-b8a5cad4f5d3 | -12.98105 | -62.72324 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1653ff71-acb2-3d48-8584-8d720356a0dc | -12.97989 | -62.72054 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24866867-350e-37d8-85cb-c0de6efd1b41 | -12.97936 | -62.72442 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffa2ee42-807b-3d70-8bba-054f0f6e2c41 | -12.97687 | -62.72266 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bcc3b51-7a39-3cc4-b701-f5f62d491463 | -12.97572 | -62.71997 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1129742e-2bdc-3dcb-b416-03a3dda98371 | -12.97555 | -62.79722 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdea5479-a75e-34e9-a5bc-eea889c3c5c4 | -12.97504 | -62.80105 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b654ac46-eb43-392e-866e-cd5c0d9071b6 | -12.97335 | -62.79818 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3de7c4f-df04-3b09-a4aa-b54173acb9b5 | -12.9719 | -62.79279 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e30e70e-c425-3639-803f-9f6ad527ddbf | -12.97139 | -62.79663 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4206916d-ba37-31eb-847e-5a372633a197 | -12.97089 | -62.80046 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21a5c443-12fa-34a7-876f-7934caa206aa | -12.97026 | -62.78994 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce4eb885-811b-380a-8522-ddc828e45cb4 | -12.96973 | -62.79377 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b57a27bd-bcce-3a1b-8023-451cfeaab93e | -12.96919 | -62.79759 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9438c2ee-2bf1-3491-8502-9795b46d7a38 | -12.96904 | -62.51852 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36c8d5fe-e7c4-3b77-9af3-24e96abed116 | -12.94736 | -62.51957 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c8d2a25-0d3d-3798-96a6-ab4675994af6 | -12.94683 | -62.52357 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac00300a-460f-36c0-9a62-5fe3b8ad2a5e | -12.94669 | -62.62032 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd715ec4-09c5-3ff6-9d96-66d3fe24b9bd | -12.94314 | -62.51897 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b3a4725-6531-3df5-86f2-cfd99ae6ba3c | -12.93189 | -62.72963 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25e014a7-17db-3bb7-afa1-b15465a71a40 | -12.92772 | -62.72903 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f4c78ad-acb3-394a-bbea-2d3e2246fd81 | -12.92668 | -62.73676 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5105b70f-7fe8-3081-a5b5-a5bcc68b950f | -12.92199 | -62.74002 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5f3fce6-c8cf-3aaf-b01a-747ee6a20808 | -12.91196 | -62.52682 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5d5b4ff-ecf3-3175-b350-5fadd009279f | -12.90247 | -62.53359 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a651a136-5126-3b5b-a79f-6936564b761b | -7.83916 | -63.5937 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea6a5988-5fc7-3283-b59b-4433ccc74d9e | -7.83612 | -63.58878 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc326518-926a-3490-ad91-7415a643b7af | -7.83547 | -63.59316 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea060c84-fd20-35b8-9471-c418466cabce | -7.83243 | -63.58823 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c796317b-9a56-3402-a9a6-aad8a12256b1 | -8.8148 | -63.00828 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49ae4c8b-093e-312a-a507-3f645fd9df2c | -8.81217 | -63.17747 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d22215f7-5217-3954-a814-c56558ee42a5 | -8.80833 | -63.17693 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 808b71c7-1c47-3330-a990-bb7d7d826219 | -8.80605 | -63.17397 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1222682d-0c1c-36dc-bb49-7edd834cb4b9 | -8.80534 | -63.17874 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 110dd151-2480-3fa4-b701-98099f270f2e | -8.80373 | -63.11019 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12c0b217-b12a-3956-8e4e-2828a6dbdedc | -8.77162 | -63.22205 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7c48b6e-e1a0-30a8-8aa3-e00508b25065 | -8.76781 | -63.22149 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4172ab3-2018-382b-9782-363cb30ea100 | -8.76712 | -63.22622 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a405d49-b7c1-3f86-85ae-cf00b83cb6d6 | -8.68976 | -63.09696 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5eae5cdf-3248-3e8c-bd17-71f282b7134e | -8.68592 | -63.0964 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 604066c2-b1fd-30d6-b619-911f1ea5c462 | -8.68365 | -62.86782 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2f56750-4903-3096-9f50-6cdf0335b618 | -8.68294 | -62.87276 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d23174fb-6b30-3a77-9e77-7591aa74c26e | -8.67824 | -63.09528 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6f864cc-34c6-3ff5-8590-cd3bb037034d | -8.6744 | -63.09471 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 956a6c85-8d72-3a18-bff0-da3dc1b24624 | -8.67069 | -63.49107 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd99d42e-b5b4-3ab1-ab34-896756a29f87 | -8.65774 | -63.26143 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README148.md)
