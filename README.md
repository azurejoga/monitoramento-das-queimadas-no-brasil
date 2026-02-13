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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f8f70cf-64b2-3355-9767-617b0fec01b8 | -18.6941 | -54.98281 | 2026-02-13 01:04:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 36c2a1aa-96f9-31b8-b33d-bb2e24e8de98 | 3.75657 | -60.93003 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7a669948-64c9-3c54-81a5-3dc6d7189057 | 0.95717 | -60.51826 | 2026-02-13 01:09:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| be751d27-316c-3259-92d3-ab4be5b555dd | 3.76981 | -60.90224 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 69792251-6809-34ac-8031-3a358aefa909 | 3.94379 | -61.03357 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c5757c41-9dab-3bfd-8db7-83c0fd41b593 | 3.86845 | -60.90832 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2e9bc024-f878-361b-80a2-1014cc66940e | 2.623 | -60.53486 | 2026-02-13 01:09:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1ab58d27-7350-3e77-abee-2da2da088b5a | 3.86079 | -60.9112 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f90fd326-950b-304e-a66d-fab6c60c9b6e | 1.90065 | -60.82267 | 2026-02-13 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 927042ef-1c2c-3137-a53a-a51174bf287f | 3.78817 | -60.89125 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 16383ddc-31e8-33d5-8fb8-8a59e99711f8 | 3.75924 | -60.91066 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9b30a935-0d1d-3bc3-a793-6ff1bad21e49 | 3.80391 | -60.70322 | 2026-02-13 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ebdb36c-bed5-36da-8064-e3dff5dab5c9 | 3.78561 | -60.98 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0108ae41-f2ab-37a1-a13a-4321040fadf1 | 3.79348 | -60.92168 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| e379c9db-c94f-34c0-88b5-31163eb4d8c1 | 3.7579 | -60.92035 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2407dabd-6056-3bbd-9961-f53699e4eb4e | 3.79217 | -60.93138 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e4c0b9d8-d008-38bb-8f61-6de6850b846d | 3.9425 | -61.04318 | 2026-02-13 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e01e1636-0db1-33bf-8a65-d9617b165592 | 3.9493 | -61.0334 | 2026-02-13 01:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| eab0b5e0-48d1-33d1-aea8-d6d0f6ee7b36 | -6.5631 | -51.1126 | 2026-02-13 03:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 0991c854-9bfe-3872-b8df-08fccf9d729c | -16.29162 | -40.77788 | 2026-02-13 03:02:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1eb7d901-06c9-3665-b6c9-f3c5d80fbf5e | -16.28462 | -40.77637 | 2026-02-13 03:02:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 61df0bee-fe65-33df-a52f-d236ffbd0fc7 | -7.63929 | -37.4673 | 2026-02-13 03:49:00 | NOAA-21 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 14f324b2-aab2-3c9a-8541-92fad81602e7 | -10.86503 | -40.37679 | 2026-02-13 03:49:00 | NOAA-21 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54888326-859e-3f03-b77e-625faf8dfb20 | -10.86851 | -40.37737 | 2026-02-13 03:49:00 | NOAA-21 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0e956bd-1726-3ae2-b9b1-7a6c29f1cc2c | -11.52133 | -39.08989 | 2026-02-13 03:49:00 | NOAA-21 | BARROCAS | BAHIA | Brasil | 2903276 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd58fddc-3e19-3baa-b554-7370c5e57448 | -9.7564 | -37.073 | 2026-02-13 03:49:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 50088d21-6941-3a5c-8033-a44cd145ccec | -10.86917 | -40.37337 | 2026-02-13 03:49:00 | NOAA-21 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c17a37e4-3cce-360e-8c4c-913ec59fb985 | -9.75364 | -37.06898 | 2026-02-13 03:49:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a11c3267-217b-3234-bf72-edf960df6991 | -10.91917 | -39.48771 | 2026-02-13 03:49:00 | NOAA-21 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49ee08e7-b57b-3c57-8472-3265d67bfe33 | -9.4839 | -37.02987 | 2026-02-13 03:49:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9098d640-94f1-3674-96f7-0bcfcf0166e7 | -10.68633 | -40.31149 | 2026-02-13 03:49:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d58ae747-704c-3349-8cd6-0c8eda0b7788 | -10.6898 | -40.31209 | 2026-02-13 03:49:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9c88b5f2-59b1-354d-ac67-484caa9c73b0 | -9.75695 | -37.0695 | 2026-02-13 03:49:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 8.4 |
| cf963817-ad26-3608-8868-25c80f7b7cb1 | -8.17074 | -34.98074 | 2026-02-13 03:49:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5b8ea098-a937-3e41-a335-031183a6a249 | -8.62354 | -36.28288 | 2026-02-13 03:49:00 | NOAA-21 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a701e9bd-85b6-3a7e-9191-68ef70212f56 | -9.67881 | -37.08955 | 2026-02-13 03:49:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65473527-725e-3bda-a1c9-7e64139f0b78 | -10.69044 | -40.30818 | 2026-02-13 03:49:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bcd24982-6f87-3c40-9035-d58df1db7fd9 | -13.39182 | -43.56335 | 2026-02-13 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce38e9ed-a018-3f60-a13d-c8272115b811 | -18.54817 | -39.79232 | 2026-02-13 03:51:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5b26b8ce-0625-3246-950c-605209d8d730 | -18.5476 | -39.79593 | 2026-02-13 03:51:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f35a9248-8917-333c-bbaa-0fdb8e2f2050 | -17.3369 | -39.68155 | 2026-02-13 03:51:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c9ed31de-fab0-3030-8d04-eb668f048cc1 | -17.34624 | -39.68684 | 2026-02-13 03:51:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a23da8a4-6159-3e9d-9d1c-b277c5941f65 | -18.71586 | -43.01057 | 2026-02-13 03:51:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 405affe5-4998-3a13-a58c-e0676d0bc75a | -18.70556 | -40.19511 | 2026-02-13 03:51:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 25944bf6-a7c2-3a54-b29f-5be8efd48214 | -17.73902 | -39.52808 | 2026-02-13 03:51:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d6178bca-0845-3287-82d4-20b34466da3f | -12.14963 | -38.06615 | 2026-02-13 03:51:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 36950dbd-5fd6-3cfb-9057-4d3382b03de6 | -11.01987 | -45.07103 | 2026-02-13 03:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97a4273c-84a3-3abc-8e48-30ae8cfc2b36 | -14.94527 | -48.22607 | 2026-02-13 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a5579b5-b28d-359f-927b-49dcf5b1b278 | -11.42702 | -41.46677 | 2026-02-13 03:51:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b168c547-af2e-36cf-b42a-5fdbe581ef03 | -10.93107 | -44.66825 | 2026-02-13 03:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce9c3b89-5518-3e54-b114-c014538cab2c | -19.44645 | -44.64349 | 2026-02-13 03:53:00 | NOAA-21 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb9c5150-0cdf-3f17-ae13-57344cd090db | -21.13558 | -41.24277 | 2026-02-13 03:53:00 | NOAA-21 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bc65e464-b0e8-3fce-9910-04a23d2c407b | -22.85558 | -42.06116 | 2026-02-13 03:53:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6fb32bac-2cf4-358f-8f7b-4f360f1b4a08 | -27.65358 | -50.81676 | 2026-02-13 03:55:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 784305fe-cda3-3b22-ac94-8bff11a85fa4 | -27.65832 | -50.81318 | 2026-02-13 03:55:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 88d19efa-c2e4-344c-a43e-78350e763b6a | -27.65355 | -50.81189 | 2026-02-13 03:55:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e6012412-0310-39e8-9d0e-5567b20d420c | -27.65489 | -50.81077 | 2026-02-13 03:55:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 83f3f596-44f6-3a3e-b324-055f1b4a8cc6 | -27.68935 | -48.75079 | 2026-02-13 03:55:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04845657-472d-36b6-8c1a-97577b0f4018 | -27.70558 | -51.15799 | 2026-02-13 03:55:00 | NOAA-21 | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f5d9b1c6-6cea-30e2-9ef7-f651bef80ff8 | -2.90233 | -46.68024 | 2026-02-13 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d47e9804-4c70-3f00-9b89-146b2b7e5bd9 | -2.90186 | -46.67825 | 2026-02-13 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54ac9a61-cc14-323e-9109-2f336d1fcb2f | -5.65913 | -47.51828 | 2026-02-13 04:21:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f4656c7-0347-3877-9a5b-84d75fe81198 | -5.66385 | -47.51398 | 2026-02-13 04:21:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e913b171-4f51-3e17-96cb-8b6ce9899c01 | -11.18457 | -43.56595 | 2026-02-13 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27388c62-0805-3975-9e22-4ee08b994af5 | -11.01992 | -45.0705 | 2026-02-13 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e9a79ee-a452-3d99-b196-a82c656808ae | -11.4261 | -41.4679 | 2026-02-13 04:21:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ddee3387-3ebb-362d-8d23-62ecab65083c | -5.66305 | -47.51888 | 2026-02-13 04:21:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ab7df2-58c0-3845-a673-a720eec98f50 | -11.17789 | -43.56488 | 2026-02-13 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 555ee357-fb02-3da3-9216-ffb50c606d4e | -10.93203 | -44.66743 | 2026-02-13 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c71a2599-42da-37d3-94da-14b6e745ab5d | -9.75819 | -37.07182 | 2026-02-13 04:21:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6e53c9bb-3f0d-37a3-92c8-2fb9ec71bcbe | -9.7536 | -37.07121 | 2026-02-13 04:21:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 5b2fc713-6f7a-35d7-bc37-81ee0d042f1f | -11.18847 | -43.56293 | 2026-02-13 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a613a48-86f9-3eee-b33f-92eddaecd854 | -11.18123 | -43.56541 | 2026-02-13 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cb09f66-4373-3c8a-a590-c6bf4c108a87 | -10.9348 | -44.6715 | 2026-02-13 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8c28540-56df-3bbd-adae-e96781607f2e | -18.55039 | -39.78977 | 2026-02-13 04:23:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2cf264c9-9980-35fa-b7ff-b329b7c912c8 | -23.42919 | -46.75859 | 2026-02-13 04:23:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f1642af4-597e-34a9-9126-f29f1dd4bb14 | -17.21365 | -41.81476 | 2026-02-13 04:23:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7aba0777-e017-38ad-8c20-307799a92a06 | -15.41805 | -41.44108 | 2026-02-13 04:23:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 28e65ea5-bc6a-37b7-bbd1-f519dbbeec34 | -12.53339 | -47.54352 | 2026-02-13 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8acb1df9-1265-3687-bdfe-6014457dd7f8 | -18.54606 | -39.78915 | 2026-02-13 04:23:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| faa58c42-ceac-3619-bbf7-df7eb575d92a | -11.84581 | -49.21868 | 2026-02-13 04:23:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 316b4a4f-5102-3292-bf3d-a30dfd6243f7 | -11.84491 | -49.22386 | 2026-02-13 04:23:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96436c09-051e-3cc1-a7cc-05496a0d11db | -17.25494 | -43.4651 | 2026-02-13 04:23:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 03b66417-f9c0-3433-b754-6f9cc6bbff4c | -17.21302 | -41.81928 | 2026-02-13 04:23:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 501fd4a8-9b8c-3a43-b835-5a07b46affb2 | -11.84401 | -49.22904 | 2026-02-13 04:23:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25e78e94-a0ee-34e4-95e5-73cc61c7324a | -11.84887 | -49.22456 | 2026-02-13 04:23:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e717fd5-64f9-3771-ba1a-d991a2bc4b29 | -18.54986 | -39.79404 | 2026-02-13 04:23:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e43afc52-7f35-3a16-8a2b-b86bf80dc3bc | -18.54554 | -39.79342 | 2026-02-13 04:23:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 95169fe0-c803-3307-8ce2-4ef38c92c1bc | -11.84095 | -49.22318 | 2026-02-13 04:23:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abcbf167-b6c2-3c73-9f4b-3e96eb7ba818 | -14.94353 | -48.22549 | 2026-02-13 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e01f04a-96a9-3002-8a69-dc08dda00424 | -18.71555 | -43.01291 | 2026-02-13 04:23:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 37a2ca09-bc39-37bf-ad76-0d81f3773a89 | -27.65584 | -50.81547 | 2026-02-13 04:25:00 | NPP-375D | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2564dd96-ff6c-3216-9460-ed9fa4ae0e4e | -29.72985 | -53.873 | 2026-02-13 04:25:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 73413f59-ea6b-32d3-be07-c181ab8c4392 | -28.62253 | -50.43082 | 2026-02-13 04:25:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fd1ac93f-4572-3f77-a745-041dce6a63aa | -21.13796 | -41.24207 | 2026-02-13 04:25:00 | NPP-375D | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5c27f432-81dc-3795-8728-37caca3ef3ef | -25.17161 | -49.65875 | 2026-02-13 04:25:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5cc0ca50-0801-3209-83fa-72679d87de7f | 3.34654 | -59.91547 | 2026-02-13 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c5ab2b9-b8d4-3dd6-bec5-0b24fee5ea60 | 3.36068 | -59.9193 | 2026-02-13 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfb91164-098b-3253-9e15-87d2cecea6d8 | 3.36731 | -59.91824 | 2026-02-13 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0507f9ae-979e-3673-987c-783f2e15a85e | 3.33665 | -59.94053 | 2026-02-13 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README2.md)
