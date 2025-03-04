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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 852f9ab8-2f7a-3910-bed5-b58cc84f6588 | -21.60996 | -48.47107 | 2025-03-04 04:06:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef443661-cde0-3d22-9649-bf7cb49bc808 | -22.15772 | -43.10097 | 2025-03-04 04:06:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 203a507a-38c4-3641-be9e-b2b20dc20b6f | -20.10244 | -43.99113 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a63b2721-974d-340e-beb6-49bab9e26942 | -23.00866 | -50.40689 | 2025-03-04 04:06:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1a35d8bc-39f4-34f9-b0c0-4dcbec395e2f | -23.11625 | -46.60619 | 2025-03-04 04:06:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2747ea38-308b-3c3a-a32f-c536081b045f | -20.10182 | -43.99492 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e8c30070-9efc-3116-9eb8-e0057cfe0547 | -22.16105 | -43.10159 | 2025-03-04 04:06:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 41c104a6-8422-3389-a2b8-6edc9234e9a5 | -20.10304 | -43.98736 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2ba47415-4a8c-3463-bc13-28887ff939e9 | -21.96353 | -45.40753 | 2025-03-04 04:06:00 | NPP-375D | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bf2a3992-f6a4-37ae-8a03-2459fff88968 | -22.75257 | -43.26884 | 2025-03-04 04:06:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77eb92c7-2190-3cc1-bd65-cd4710f78925 | -20.79201 | -51.65762 | 2025-03-04 04:06:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 0cf877a2-1e40-3571-884f-5479970e2efb | -20.7952 | -51.656 | 2025-03-04 04:06:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4d0a88f1-30e2-3c40-a781-74da400e660c | -23.34017 | -46.77283 | 2025-03-04 04:06:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 889c7e1d-8269-3bc6-b80e-80e767bea1a7 | -20.09454 | -43.99749 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fc1a8337-5360-37a8-bf1b-ec806bb450d8 | -20.09637 | -43.98617 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 42002c2d-d9c5-3f02-8695-14665a99d243 | -23.4073 | -46.55672 | 2025-03-04 04:06:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7564a5a-a636-3b92-83db-ebe3807e9eb8 | -21.4476 | -53.8508 | 2025-03-04 04:06:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b836fcb3-96e4-3a43-b187-c6396fa7fa3a | -21.6275 | -43.46606 | 2025-03-04 04:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c50eb3e-f983-3eec-b4de-b5d1521cfdfc | -21.97248 | -45.72506 | 2025-03-04 04:06:00 | NPP-375D | SILVIANÓPOLIS | MINAS GERAIS | Brasil | 3167400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b9df24e8-833b-345a-9c86-2b9fbf6d1e25 | -21.26737 | -48.72179 | 2025-03-04 04:06:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f626b5e3-8f0c-3173-b0fa-b371efaace30 | -22.85509 | -42.98019 | 2025-03-04 04:06:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 59334fc3-5274-3d6e-afa8-2c0c7ad48901 | -20.76583 | -45.57163 | 2025-03-04 04:06:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4eecd30-e41e-33ed-8df6-421e22b4d10d | -20.96837 | -46.46311 | 2025-03-04 04:06:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f18e9622-38ac-39f4-9788-4eaef888a8f9 | -20.83817 | -44.66842 | 2025-03-04 04:06:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 960a2d6b-c0e6-3128-a13e-d4a659abc5ac | -21.17893 | -44.27303 | 2025-03-04 04:06:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1148bfdd-e0eb-3eda-89fd-9d557c99b46a | -23.11976 | -46.60686 | 2025-03-04 04:06:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6dcf659c-3c09-3dd5-931e-55780abcfa26 | -20.74341 | -48.54261 | 2025-03-04 04:06:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 586c4d17-3f01-3ca0-8eaa-768e1606dfc7 | -20.4159 | -43.55392 | 2025-03-04 04:06:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4eecbbd0-6830-3791-b264-4409b37541ba | -22.78999 | -42.80836 | 2025-03-04 04:06:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c2fb293-0d69-3df9-b816-c8135281b2eb | -23.33665 | -46.77214 | 2025-03-04 04:06:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 157e74e1-ecfd-3ea3-9ea2-581bf6ca7732 | -23.5054 | -51.68656 | 2025-03-04 04:06:00 | NPP-375D | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fd829b69-fa9c-308e-b1e0-cae15c9c0973 | -24.86356 | -51.99306 | 2025-03-04 04:06:00 | NPP-375D | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7898889f-7f4c-3669-926b-a61ae277bfdf | -23.40383 | -46.55595 | 2025-03-04 04:06:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6d375236-b7f0-35c4-a4d0-d5bf95f55af4 | -23.09248 | -46.28346 | 2025-03-04 04:06:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a52929f4-33c7-3a81-84e8-eb444e9ae76d | -23.50636 | -51.691 | 2025-03-04 04:06:00 | NPP-375D | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9fec7b5a-0ec8-3f4f-b509-cf4186608855 | -20.09576 | -43.98993 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a41fa0ed-f27e-3f84-883b-c8d2f80ace0b | -20.09849 | -43.99432 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8b5532c0-28e1-39be-a02f-0905a0988045 | -21.43715 | -43.55453 | 2025-03-04 04:06:00 | NPP-375D | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6ddc3022-5719-3f61-861f-585c92747550 | -23.59504 | -47.43975 | 2025-03-04 04:06:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c59cd588-3184-3699-8a90-a02f5364209c | -23.01141 | -50.40566 | 2025-03-04 04:06:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b358fd4a-0fc5-3ae1-b0c3-f43d571243b8 | -21.96013 | -45.40684 | 2025-03-04 04:06:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c7dddbe2-8970-3982-82d5-9a98d81a29d7 | -20.82737 | -48.9209 | 2025-03-04 04:06:00 | NPP-375D | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e315cee0-2e33-37ce-80a0-52bb85f7c720 | -21.63367 | -48.68615 | 2025-03-04 04:06:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44ccbbcf-d13e-34bf-8ce5-a36a70bd8584 | -23.52047 | -47.26817 | 2025-03-04 04:06:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c55c0d41-141b-32d0-99be-2bc244cab02b | -20.73944 | -48.54169 | 2025-03-04 04:06:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d882d1cc-9d15-3923-be92-5c33ed723f95 | -23.50434 | -51.69154 | 2025-03-04 04:06:00 | NPP-375D | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5efe3ee4-7749-32b3-ae77-d45543eef7f5 | -20.7697 | -43.15928 | 2025-03-04 04:06:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 64fe77bf-1908-303b-b1ed-c651f93e9e97 | -20.10121 | -43.99871 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96fd99f3-0248-35f4-8eef-be889d75636d | -19.90647 | -45.239 | 2025-03-04 04:06:00 | NPP-375D | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d2276255-2d80-3de9-9aed-c7f15acb0eea | -23.00953 | -50.40259 | 2025-03-04 04:06:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 677930f8-730f-35eb-ae58-bce12bdd2165 | -20.09787 | -43.99811 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a08fee9-4805-31fe-a8a8-fc07fa630afc | -27.55223 | -51.10748 | 2025-03-04 04:08:00 | NPP-375D | ABDON BATISTA | SANTA CATARINA | Brasil | 4200051 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eaa45e7e-6d56-3e9d-91aa-8fd6f5c58b5b | -26.25975 | -52.81728 | 2025-03-04 04:08:00 | NPP-375D | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 57d36ea2-e77c-39c7-8537-b5e6be8d4010 | -28.62098 | -50.20863 | 2025-03-04 04:08:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7df79996-6864-3ff2-9546-b4f324b8db69 | -27.48466 | -50.66246 | 2025-03-04 04:08:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4de6652e-8007-30b0-a2af-c98f437cd3bf | -27.54974 | -51.10598 | 2025-03-04 04:08:00 | NPP-375D | ABDON BATISTA | SANTA CATARINA | Brasil | 4200051 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ccf900ee-4bd6-3a89-9f8c-90790a1dd283 | -26.83271 | -51.46535 | 2025-03-04 04:08:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6a54d40f-7f28-3200-a107-f89f4a456fde | -29.07997 | -49.61065 | 2025-03-04 04:08:00 | NPP-375D | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 205cb62e-831a-3803-a6a1-94a5304b911a | -26.25514 | -52.81594 | 2025-03-04 04:08:00 | NPP-375D | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 688764a0-6047-3cab-9298-ee9fecb05240 | -7.59955 | -46.45077 | 2025-03-04 04:23:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30513dc8-6f37-340d-ae89-f65a5d49ef4e | -5.33427 | -46.95857 | 2025-03-04 04:23:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| edd282c5-1638-3825-9b32-6fa72b8187df | -7.59901 | -46.45423 | 2025-03-04 04:23:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f484a869-d295-3741-a5b5-9f15e227cd36 | -5.67485 | -45.22758 | 2025-03-04 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24a1acd2-d5d5-3a2a-9686-26152680fbf0 | -5.6743 | -45.23108 | 2025-03-04 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8344eea-54ff-35dc-90f6-7fab0dbd8dca | -5.64212 | -45.99969 | 2025-03-04 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ff90d2e-0c4a-331d-9a8f-438dedb01f78 | -7.25567 | -45.37168 | 2025-03-04 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6d79b06-c8f6-3097-b075-97720e503d9d | -5.66758 | -45.20855 | 2025-03-04 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b6cfa191-c621-36f4-98f5-3c0f6db1cadf | -8.10423 | -43.14036 | 2025-03-04 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c1a95bd3-ece2-3616-9eaf-c77e16d3ea95 | -8.11459 | -43.14636 | 2025-03-04 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 707d998a-20fa-33ed-b6e7-cf3015e3cdd7 | -8.10359 | -43.1447 | 2025-03-04 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a2ded652-3d20-35eb-86d7-4eea1cb170a2 | -2.5851 | -51.92316 | 2025-03-04 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f771581e-9f9e-3049-8fa1-e4b1c04f1b11 | -13.99363 | -45.59057 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41df0ec1-77d2-3bf5-a23c-d96229fbf11b | -10.52913 | -44.66285 | 2025-03-04 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d5af224f-e55e-3506-8cfe-5646e80f3c37 | -13.98841 | -45.57766 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 264a16fb-b280-3164-8a31-e81f9239bb67 | -13.30093 | -44.79828 | 2025-03-04 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0379cc0-7c2d-36fe-8fc8-b020c3d45b09 | -13.47691 | -44.01955 | 2025-03-04 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03566b62-a741-3246-aa71-2f07332fc2a0 | -13.99479 | -45.58268 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02383107-053d-35a5-a320-e4953d495e52 | -14.85631 | -46.79305 | 2025-03-04 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71835e6b-a04f-385a-b758-c7a7ed9af343 | -14.03242 | -45.6408 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30472712-4344-395c-9fee-fcd078c59036 | -14.03012 | -45.63242 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f441732-5dfa-32b3-b089-98d4443652be | -14.10211 | -44.1306 | 2025-03-04 04:25:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 513bc9f5-478a-36b6-962a-6e4852be4a20 | -13.98958 | -45.59397 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e02da6e-2624-3eb7-bf19-57e88ff1d4d4 | -13.99537 | -45.57872 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9ab3183-65ca-36c1-88b1-aa48e26fcb2b | -13.99016 | -45.59003 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c6bf76c-0b63-3ecc-91d7-428ddd5001ec | -13.98899 | -45.5737 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 617caa47-38c4-3f93-8bd8-999bb9c8a2ec | -14.01275 | -45.62973 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1eecc93e-f7d9-350d-bed7-811a40300170 | -13.99131 | -45.58214 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a59f1f0-4e6d-387e-b88a-6cfcaf487b92 | -14.01391 | -45.62188 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef63d497-7d1e-3c4f-a1ac-85917353ec5a | -14.00059 | -45.59164 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd1938b1-bd6b-3af7-beb6-7d9dcb6e5c97 | -13.99769 | -45.58716 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10904bd8-30cc-34ca-a620-dfc111c4291a | -11.46107 | -48.0087 | 2025-03-04 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 814a1a16-0ca1-3715-bf13-3a4b5f455b9c | -14.02837 | -45.6442 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72ce66f5-3eec-3116-8764-baee255dc702 | -14.02028 | -45.62688 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20020d02-6b7b-3c37-a33d-42e735c9bbf4 | -13.98668 | -45.58949 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3d016cf-55dc-32c5-951a-d83b862779fe | -13.99248 | -45.59844 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f854903-5de6-3f23-b599-03b3e39a91e4 | -14.02084 | -45.64705 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0aa935a4-ff6a-3027-b428-0ed7425c3790 | -14.00001 | -45.59558 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90f0ceac-cfcf-312f-bee1-c04f3804353c | -14.01737 | -45.64651 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c174e494-d6e8-3110-b316-a5f42d45f3b7 | -14.01795 | -45.64259 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87df7de9-4811-34e1-ada4-c4d912570906 | -13.99943 | -45.59952 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README5.md)
