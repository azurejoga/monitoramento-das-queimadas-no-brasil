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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47894b85-bc0b-3682-b7fd-3dded0665d45 | -5.02528 | -44.51186 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae65073d-c23e-3dfb-a302-f72992990c1c | -5.71532 | -42.91479 | 2025-11-14 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 91c15863-c8a9-35fd-ab98-612a65e69d15 | -7.5989 | -46.38816 | 2025-11-14 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7d6513f-9d01-3c4b-9e4f-98106d711949 | -7.49706 | -47.33669 | 2025-11-14 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9918602d-78f0-3712-a69b-760b014a6665 | -6.09346 | -41.61032 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 32ecea17-cb1c-3d12-8e60-095c4f22e195 | -6.1657 | -48.05145 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 89039576-85d4-39eb-961d-41fbfb2af44f | -5.74709 | -42.7248 | 2025-11-14 03:53:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8fcb6511-b672-3f37-8305-c679b08167d4 | -5.74976 | -45.10473 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87021b5b-a092-342a-a9fc-0ec88df483fa | -6.89049 | -42.85379 | 2025-11-14 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| df97c749-e199-30f9-b766-979b0231af76 | -7.47526 | -42.54882 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 05690ad3-8688-3ab7-a603-8c803725483a | -7.1521 | -41.25624 | 2025-11-14 03:53:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 493b1f89-f1bb-3fb5-a2ce-d31047b11fbb | -6.90117 | -42.09111 | 2025-11-14 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 37827b92-19c7-3104-b390-2c8485492119 | -5.49678 | -41.91215 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7cdca338-30e3-381b-99fb-b13366304dc7 | -5.25181 | -46.17985 | 2025-11-14 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f917c113-af93-33a2-9eeb-4b0d8004da7f | -6.53254 | -43.40326 | 2025-11-14 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c26dca0f-f6a7-355b-b76e-4459784e2e83 | -5.42286 | -44.80882 | 2025-11-14 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e839223-b1ca-3434-ab97-b9771336c567 | -4.98845 | -43.88467 | 2025-11-14 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0807f375-1c59-320a-8194-d32ad23dd1be | -5.52949 | -43.68177 | 2025-11-14 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c89de6f-f726-3869-aac7-30d074cd7e12 | -7.46392 | -42.57055 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d79ef11-3379-318f-b748-60f202b90403 | -6.87828 | -42.84945 | 2025-11-14 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1f45de21-d4e5-3835-b6ec-2cd5f98fd2a0 | -7.92457 | -44.34949 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe81e537-98f6-3cac-8527-a88f4d106312 | -7.84783 | -44.2921 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9815d848-7df3-36f9-aec0-0fa83931b42a | -7.93987 | -44.33585 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce46f444-1aeb-3b2e-8b87-e6260e24f6e2 | -6.45127 | -45.65813 | 2025-11-14 03:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87148735-e8cf-34fb-89f3-4d1b60d1e182 | -4.53529 | -46.39902 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7afd2fd3-c07c-34d8-b258-765ddd86f39d | -5.61593 | -41.06045 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e76d760-938c-3e2c-bd41-865ec6834d6f | -5.55724 | -47.34159 | 2025-11-14 03:53:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00fff794-8839-3e52-919d-2e08ffe58a7e | -4.64537 | -47.95057 | 2025-11-14 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa63bb9d-9dff-32a4-9f22-7512ad9490ad | -5.52966 | -41.75613 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 86bf9928-a53d-3df2-810f-2495090208b2 | -5.50966 | -40.54731 | 2025-11-14 03:53:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5edb30da-775a-3172-8b7c-00be89c419df | -7.12016 | -42.72461 | 2025-11-14 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 36f55246-9c0f-3c72-bede-c0fd807267d1 | -4.70556 | -46.45163 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ffde43fb-20c5-34e9-9e01-722bf5e483ee | -5.46313 | -47.10192 | 2025-11-14 03:53:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 263406f0-c5a8-3b80-9336-ff89aab1b78f | -6.58058 | -42.1571 | 2025-11-14 03:53:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf442b46-4ba9-3931-aede-cead20382bda | -6.08884 | -38.46199 | 2025-11-14 03:53:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f579803-9488-365a-a327-dae4b3355d25 | -5.57159 | -47.10035 | 2025-11-14 03:53:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcffb503-addb-3ebd-93a6-44fd9f31983a | -7.39178 | -43.31982 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f39620f-19d4-34f4-92c1-f405ec6faae5 | -4.75175 | -46.39662 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3801c436-4e13-3ab9-8dff-0d9fb5e82d53 | -7.92657 | -44.33765 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33cbbd20-b4fa-35a2-af85-c814711f857c | -6.16079 | -48.04676 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f9b17b59-0f7a-3da8-bb94-bd7130dfff30 | -5.58419 | -41.09758 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93d30319-4e73-36e5-a693-381ecada4f5c | -5.52422 | -43.60991 | 2025-11-14 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ccb52b5-a751-3688-be1f-6a9438ee150a | -6.92617 | -44.13765 | 2025-11-14 03:53:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7672017-f1da-36cf-a7c0-f968f6733a3b | -6.07896 | -41.63023 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf752e91-37de-39cf-b222-90569f73750f | -7.88649 | -44.31876 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5be5ca2a-bd07-363d-88de-82c96c11c54d | -6.45598 | -45.65901 | 2025-11-14 03:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d8989b2-b5f4-3aa3-91da-f4f87207ff45 | -6.56854 | -42.12923 | 2025-11-14 03:53:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7cdba3e7-9be5-34f7-bc0c-913b7a9a8e38 | -4.01426 | -48.80579 | 2025-11-14 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 776df02b-f1d0-3a5f-a2e8-61f92d22e7a6 | -5.16004 | -44.65777 | 2025-11-14 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f64fe50-dee0-3765-acfb-18e7206e0c5f | -5.36113 | -46.29146 | 2025-11-14 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 984a1e21-555f-3491-8b9b-aa7f0b57437c | -7.10129 | -41.82818 | 2025-11-14 03:53:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c31cf85f-e414-3792-8539-9f23c05bd76a | -7.55242 | -47.24415 | 2025-11-14 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2caa0a2-e33a-33e9-a276-3ea4a9e45200 | -5.75099 | -42.72555 | 2025-11-14 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fea6ab36-937a-3cf2-96a8-6d4c13535df9 | -4.61122 | -46.55888 | 2025-11-14 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd72c3b5-1e26-3834-be96-6b8e044f551c | -6.07329 | -41.54997 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 030f236d-faf6-3b54-b2b2-c22eb7dba753 | -6.4833 | -39.34663 | 2025-11-14 03:53:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 519b4602-3b02-3b22-b479-886d11c43a1f | -6.41169 | -39.75591 | 2025-11-14 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07592aca-3394-39b8-a1ee-78cad7827e50 | -6.88992 | -42.85151 | 2025-11-14 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ed8683c7-283c-3255-9f01-3dd4d6424ef5 | -6.07824 | -41.63464 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4c69c9a4-683d-3b3d-81cc-55ee123697a0 | -6.1426 | -48.05219 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd04eb01-d2ad-311b-b5fe-2fcaef6a8e5c | -6.41226 | -39.75233 | 2025-11-14 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd8d89be-257b-3341-91eb-a18e0c2daa82 | -5.84599 | -38.40204 | 2025-11-14 03:53:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b31339da-58a6-3b7c-9717-c6da79b92a2b | -5.02866 | -43.24571 | 2025-11-14 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1a76cb8-543e-3b83-8319-d30f73d97ff0 | -5.3656 | -46.29551 | 2025-11-14 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 421e101f-bc4f-3521-b887-04d73447e180 | -4.00743 | -48.80927 | 2025-11-14 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f22d9eb-3e31-3daa-919f-c7cb13241c75 | -7.87034 | -44.31198 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4a563f2-1698-389d-86a7-a5cb3ab09123 | -7.3538 | -43.36205 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee9ecaf1-7f2f-321c-a067-b00f90e9e284 | -4.69972 | -45.67532 | 2025-11-14 03:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 171e35b7-68e1-3ed6-9c45-08ead3fad2b2 | -4.81226 | -44.87959 | 2025-11-14 03:53:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43f6e6a3-5b79-3967-a90e-80a072c92f15 | -6.68644 | -47.80147 | 2025-11-14 03:53:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6d57ae3-cd8c-3ab6-8a61-50fa09a125a3 | -8.91262 | -41.07372 | 2025-11-14 03:53:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| dc220082-6351-3c51-a704-57124bb778de | -6.24143 | -46.23964 | 2025-11-14 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aadf408c-95cc-372f-83e7-46fc271c3fc2 | -7.53989 | -45.85667 | 2025-11-14 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b0a2f85a-02a1-3d02-b11d-4f162dcc533d | -5.7543 | -45.1079 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12a622d7-4672-379c-8a6b-8a60e239e8a7 | -6.89745 | -42.09054 | 2025-11-14 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ccccd6cc-4366-3401-b2ac-f7d6abe5c673 | -7.26578 | -40.17538 | 2025-11-14 03:53:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| daa54db1-77b8-39e7-b2cb-54ab3979abea | -4.95736 | -43.72728 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b51f8074-b9dc-38c5-91c3-c376b6916fda | -7.92524 | -44.34554 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b330db01-002c-3035-bfaa-f24b3b412e71 | -5.65262 | -41.08319 | 2025-11-14 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 589f2501-5f90-3204-a73e-e561826b4d06 | -4.81288 | -44.87712 | 2025-11-14 03:53:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2148a373-1993-3d8c-9388-f37e0701f2d7 | -6.55469 | -44.24902 | 2025-11-14 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf7603d6-854c-3d5f-96b3-e19e658457c4 | -7.85517 | -44.29688 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ba219b31-7ce4-3856-a408-0d108df3a25a | -5.54262 | -41.81802 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cf4022d3-7f70-3ff5-9a3b-a30c7dbc5b1f | -7.86044 | -44.29421 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b342b8c-40dc-34a5-aa64-0b37274ba047 | -7.71177 | -42.33971 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bc3774e0-b04e-3b45-973e-0f60251cab61 | -6.55541 | -44.24483 | 2025-11-14 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1399fc37-b0b3-342e-8b5e-b17b5cbea55c | -5.36611 | -46.29254 | 2025-11-14 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| c1fefea5-1e0b-3fcb-b8ad-2f34c1ca069c | -7.0216 | -39.19094 | 2025-11-14 03:53:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b37642a8-1be7-39c6-b4e0-5836c63a640b | -6.85663 | -46.76067 | 2025-11-14 03:53:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54dafef2-4a0f-37d3-ada0-58fc64c63690 | -4.72816 | -46.7305 | 2025-11-14 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 059e8844-bc11-3778-a0e1-f4a40af70779 | -5.02986 | -43.60231 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f33b5b5-daa5-3733-8fa2-96cf3cff4cec | -4.9866 | -43.8875 | 2025-11-14 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c1389722-bc01-302d-8fad-2e0fae275709 | -6.859 | -39.57339 | 2025-11-14 03:53:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ee21bf0-2e1e-36e1-8600-803fb1656a84 | -7.84742 | -44.29154 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dd3f8142-613a-3458-b4c0-379750cc7b07 | -7.45401 | -42.58338 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 81c98d86-36e4-3c99-83b4-d74a69a5e537 | -4.01348 | -48.81031 | 2025-11-14 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 775e72de-6748-3a8a-a1cc-a49cfc772aea | -5.53786 | -43.68323 | 2025-11-14 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 56d0bb96-9e85-3912-b551-2b6d6dbb1a99 | -4.77432 | -46.45033 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 418fb89e-c622-3f26-877f-673c5db891df | -5.53037 | -41.75167 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7f688830-db04-3aeb-9503-9c34b3f17e22 | -7.0854 | -41.57868 | 2025-11-14 03:53:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README18.md)
