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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 853d827c-be50-38d2-8e5a-1e69d80c13db | -7.73759 | -54.80254 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c552d32-f38f-354a-b0d4-a63ff18ef0ed | -5.76578 | -57.4676 | 2026-10-02 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f28694dd-1c91-33bb-9473-43f5b9103339 | -6.34099 | -55.32352 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bae5ba5c-da6d-3c7b-9458-69c2f6261851 | -7.48526 | -54.99878 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c820c7dc-ca04-30bc-811b-b92595ae49a8 | -6.24094 | -53.13553 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 462714a5-be6c-3b11-a294-adb668be1d8b | -7.03636 | -55.62963 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84f2116d-cebd-398d-b7ac-3dcf541cd708 | -7.27797 | -55.58961 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7331a362-da4f-3a99-99fe-6696f11a5aa9 | -7.83606 | -55.1256 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea9c8282-5f41-3015-a8a1-cf00e3a599c9 | -7.71973 | -54.80407 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb04c9ae-e3ee-3f87-9818-f1ed309e9c3a | -6.29513 | -58.14617 | 2026-10-02 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9e635bc-5698-3ed5-9ea7-72df5db2d052 | -7.73819 | -54.79844 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f0117b4-b6b3-3e1e-a0b1-b3ddbe6deb20 | -6.82177 | -58.8604 | 2026-10-02 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da5d4fc7-f1c9-37cc-afc1-2e3e370553a6 | -7.0404 | -55.63029 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 445d1f94-45e3-335a-9c1a-c05af9cf684d | -8.09009 | -54.87765 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cbbad4d-4cf5-3577-a87b-f56242e21097 | -6.39342 | -56.41575 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 101df991-b271-3946-8a7b-7db1cd0f2967 | -5.73983 | -55.74338 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 712e6157-5240-3831-84ce-58b6684b430e | -10.26281 | -49.65774 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee5ff0f7-72a8-3f7d-aad0-79cd09ae4b09 | -7.45558 | -54.99412 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40bb0ea8-bd9e-320c-8b05-559af9d264a3 | -8.54591 | -54.56352 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b66ae61c-e4e3-368d-9b30-c08da6e16acd | -7.54871 | -55.0311 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 108cf28d-0dda-3559-a029-f21bea19fc83 | -10.53396 | -53.71663 | 2026-10-02 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dab1eaf-3410-3a12-bab5-64d2d5f3c94b | -7.83551 | -55.12949 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44202dba-764f-3abb-9faf-4f7630cf17c7 | -7.46832 | -54.99595 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adccab44-cbec-363e-b371-da70dbf4b964 | -6.00829 | -53.54434 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c62f144b-3b4a-305d-b373-356b6d93556a | -8.3075 | -54.72872 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f43bd6f4-afc8-36f2-b170-f475c0e4f1b2 | -6.5 | -55.89198 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 256af2d3-ec94-35da-b278-d52e4a2e0564 | -6.8359 | -55.26866 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eecd2c4a-9536-31ed-8116-6eecaabad83c | -7.46523 | -54.98736 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9da6326e-d456-3424-99be-855435fa316a | -7.04693 | -55.64209 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04d388a2-6de2-3853-b39d-f7a296e25c4b | -8.25282 | -54.73437 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 851bf38f-b370-3db3-b5c5-73e4d93823de | -7.33612 | -55.22255 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53260d21-5234-3996-bd83-1a48a0d38d98 | -10.26848 | -49.66359 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a19f716-7771-3fb6-aaf7-fa5c0c8d1094 | -6.70081 | -55.57648 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98593d8d-9f7d-396c-94f3-9072248d76c0 | -7.83127 | -55.12888 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 838e71ce-0861-387d-83c4-23029aa35c57 | -6.14674 | -52.80451 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56f28c62-b0f2-3913-81c6-7ce62b163455 | -7.83151 | -55.12907 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99b00c6d-0889-3045-8add-1a86528d9a71 | -7.12645 | -55.72218 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec57cc22-e0f7-3a8f-89b2-778ab800c73a | -7.19145 | -52.61457 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f0d375a1-2c7a-347c-9d5a-2fbfb0c8e6db | -6.11398 | -55.70304 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99492599-ab01-3d62-bd7b-3be7d7249335 | -7.68176 | -54.76106 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 731704ab-edb5-3d75-8db3-2b8b7ec714d2 | -5.85543 | -57.56271 | 2026-10-02 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 40546acf-b08d-34ba-b41e-e68028cde4ef | -6.49924 | -55.89703 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59b991e1-5ce7-3eea-a092-f01996345042 | -7.49669 | -54.98003 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc01bba7-80cf-33da-aa2a-249d3d873ced | -6.23694 | -53.12973 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1182a16-0057-3afe-8cb5-155e51f624f5 | -7.74398 | -49.20671 | 2026-10-02 05:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b270f827-e79f-39a6-aa4f-d42e575ce9a4 | -8.23025 | -55.28299 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8696a599-6435-34ff-b6a9-89b8c72df875 | -5.97673 | -55.37779 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ad7671e-12d7-3954-bfad-fe1164c03974 | -8.53703 | -54.56225 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d688384c-8e69-30c5-810e-96d3a1853989 | -6.15351 | -55.44298 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cee2dcb2-a99e-36ea-ab2c-dc47cca901c1 | -6.86931 | -57.71983 | 2026-10-02 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9270d894-babf-3c21-87f8-a51a386c78d6 | -7.34135 | -55.58022 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5202597-8179-3e92-a117-e66229a3aba9 | -6.40106 | -56.4169 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7935d7d-bd4a-3152-90c1-8fbcbacac089 | -6.19603 | -52.80548 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fa36cd8-2293-3ce2-b7d3-bd7ab44ddca0 | -8.54147 | -54.56289 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f35d3321-274f-302c-b59e-8893df256b74 | -10.83097 | -51.09404 | 2026-10-02 05:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a635950-ac2c-300a-8528-74db9bab9ffe | -7.68118 | -54.76514 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6961b91-431e-3c09-9127-ca43ef52d027 | -10.25195 | -49.66731 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 323e8415-1606-3306-8bec-307dcaab32e7 | -6.23547 | -53.13985 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00143111-d4bb-3b73-91ae-41673df3a031 | -7.18724 | -52.60847 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc4c9c43-671b-3dbc-9b5e-7551c06622f2 | -7.05866 | -55.61868 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43e1d3b4-f616-3517-af02-a0c006d9b597 | -7.72626 | -54.75899 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f7ba895-6114-3df5-8bc6-a76400688799 | -8.23694 | -54.78342 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c753293-e0c0-3be4-bae0-503389d91027 | -6.29627 | -58.1455 | 2026-10-02 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e16f8263-f035-3e24-8ac8-3db274b7b01a | -10.75083 | -54.08907 | 2026-10-02 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b291b1bd-75d3-36e0-9515-f985507d9fb9 | -7.73387 | -54.79782 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70906332-c5d8-3740-9637-585a1643c464 | -6.4087 | -56.418 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ab84340-c86e-3304-9625-b3e625b52543 | -7.50037 | -54.98452 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebacf086-e788-3852-a355-984adb2e9f3d | -7.56909 | -55.12885 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64b10f85-3b88-34b1-89b3-113bd1b10199 | -7.27283 | -55.59624 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc4b0f75-2abc-321c-885e-2dc2d7e859c1 | -6.39412 | -56.41109 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9885f4ce-1c7a-303c-a228-f0b1d27b3cfa | -7.83661 | -55.12171 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d6e755e-0035-39d1-8710-4012f9eabdbf | -10.82516 | -51.09327 | 2026-10-02 05:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a77faa7-8c9d-3750-b029-91940af55624 | -5.99438 | -53.54929 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2ae44c4-3363-341d-9aeb-8cbfde179a9d | -7.49553 | -54.98788 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38861a5d-ac5e-35d1-b4c0-976d83ee1a79 | -7.27743 | -55.59329 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4553c314-9604-362d-a0d9-596058b9946e | -10.82466 | -51.09737 | 2026-10-02 05:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0de17370-62a8-306c-bff2-2cbeb319bbbf | -6.43705 | -55.80851 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b94bc0f-9624-3248-bfb9-eca3a6f0cf45 | -6.34917 | -55.32472 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 845bf4c8-047d-3106-b888-cd0b38fe0cd8 | -7.33079 | -55.22983 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb6d4aa8-63bb-310c-bf7e-785dbf8cb692 | -7.83716 | -55.11782 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a45226e2-3767-3259-a666-4969b9fb6670 | -8.30711 | -54.72954 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e8419e7-d4bb-3f13-89cb-d7e1b9c97d90 | -7.75487 | -54.80505 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6272f7e-f637-3720-bca0-82a035ac4fe6 | -6.13952 | -53.29073 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 921100fd-26ae-37fb-aa3e-98d8c15432ca | -6.22969 | -56.04439 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7d9a27e-54ae-396f-af2b-50fcffbb14a8 | -8.26471 | -55.69184 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 381c261a-4992-3e74-8bce-ac80cf1e4369 | -6.62651 | -57.98751 | 2026-10-02 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95ea2107-f3cb-3347-a310-1cb930ad4972 | -6.31767 | -54.78022 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a35bef52-8037-3347-bbdd-c55efa1413dd | -6.23948 | -53.14557 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fb1e35bc-b8bf-3c90-8161-9c1dd41a2e78 | -6.10517 | -55.68074 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6cc71f0-1942-33e4-b7c3-bceddb783983 | -6.70536 | -55.57355 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04ab35d3-16ef-3eed-838c-966527759363 | -5.98483 | -55.379 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82854eaf-42a8-32d5-8ed2-646748486777 | -11.42753 | -50.97977 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfadd35c-c8e2-3857-bd11-f71e1e148966 | -7.73147 | -54.8143 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d6e6fa2-59f5-3560-9591-56ab53f7c785 | -6.11537 | -53.09295 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aefc4f1e-9553-37d2-a13d-c9d587530ad3 | -6.40557 | -56.41285 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bcb3fda-1c92-3a0e-80a2-95628cfa8625 | -7.55156 | -55.0113 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d026c59-e2b0-3c24-adff-9eee135adac4 | -7.83919 | -55.13396 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdb9a4a9-a02d-31ac-b49a-c4c6e5a25bbf | -7.052 | -55.63572 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7176d2d3-cc8d-3b6b-8e5e-81d9e5400dfd | -7.46177 | -55.01127 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e928f413-75af-391a-ae60-06739f32d9c3 | -7.63638 | -55.04993 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README77.md)
