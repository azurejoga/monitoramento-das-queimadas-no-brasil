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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a31945c3-2d75-39fe-b62a-764ad30cb082 | -10.25884 | -44.05084 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f6dc129-ba60-3907-a12c-3764e10d8e7a | -8.2584 | -44.06988 | 2025-10-17 05:10:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bf57648-2dca-3a23-ad34-3e9550c2d068 | -9.14094 | -62.30042 | 2025-10-17 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad0458da-264f-3d8f-aebb-3ce93ef7b0e6 | -9.13706 | -46.63853 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 84a5abac-0dfd-33be-b13f-2afbdcbb8da7 | -10.22385 | -57.68371 | 2025-10-17 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1c63ce5-a446-3c07-ad87-4b01899e377c | -8.33319 | -46.23764 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ea3d1d8c-8029-3c56-b476-fb82ed75b794 | -12.71451 | -48.63308 | 2025-10-17 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33c7eedc-ddc5-3764-b648-ab518e1c30e1 | -10.11074 | -44.5703 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a56196d-1ac8-35b7-bf48-85669b66548c | -10.2934 | -44.04237 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 66ce8634-6b33-3e88-ac6b-dafe52bb4aac | -9.44972 | -56.65418 | 2025-10-17 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 929592b4-245a-391b-bc50-7f7e2c0caa65 | -10.26449 | -44.04 | 2025-10-17 05:10:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47a84f18-2c48-316f-85b8-4e03820df920 | -8.73804 | -63.78936 | 2025-10-17 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b06872a6-eff0-3045-8a71-ac356b0aa894 | -9.71345 | -59.26555 | 2025-10-17 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36d8d447-4390-3eaf-aa6f-184cd465e661 | -7.23913 | -60.64502 | 2025-10-17 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32f35549-62ea-3e40-ac2a-a5e620ab1bbd | -7.7157 | -47.8488 | 2025-10-17 05:10:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d31809e3-ceaa-37ee-af86-2e014b5a7f4b | -9.34513 | -46.91538 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5833fe65-7447-3aa2-b1ff-736998ea012c | -10.57134 | -47.44338 | 2025-10-17 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29b7d5ba-7f68-3328-babb-26cf485785cd | -12.45399 | -51.32818 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40db9272-7a58-346c-9592-4884884d2ef5 | -7.9492 | -44.12809 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 49b53e34-7f05-32c4-9c67-a9f7d650cc8c | -10.00412 | -56.11459 | 2025-10-17 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d38401e5-2b7e-399f-b43d-4ff7faf04860 | -12.28292 | -47.11243 | 2025-10-17 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0518d00-d7e7-3ad0-95ab-8139508697fb | -7.62127 | -47.83947 | 2025-10-17 05:10:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c13337c2-0c6f-349c-9e23-4b8e76582c17 | -9.35112 | -46.91619 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c5e02e0-0d13-3364-b87a-82fa5a3d9fd6 | -9.39829 | -62.5625 | 2025-10-17 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91c2a55b-396c-3973-ba5f-7f866e438c35 | -10.95468 | -49.77887 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a151bfc-a11c-3633-bd8c-a4bc6f42b1a7 | -9.70381 | -44.56757 | 2025-10-17 05:10:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9100c697-7ebe-37fa-94e1-7db7213f67f7 | -9.50664 | -47.27024 | 2025-10-17 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf09e133-f5b6-319e-8ee4-3cab71e41a6f | -9.13074 | -46.62975 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10ee9032-83a2-3a5a-8b4b-acefaa88ff6f | -8.39551 | -46.23818 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bbc99aae-9dd6-3569-9664-4fd07f1f5b37 | -10.97947 | -47.91776 | 2025-10-17 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3790cbe8-f0cf-34ad-abc0-7de466539d40 | -8.39084 | -46.32174 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00636868-37ef-3946-9793-18a71478eb3f | -10.52581 | -49.54989 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 055e0ff4-9922-3aa0-8df1-86c94f7cc740 | -9.30276 | -46.93772 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a21b8e3d-394a-34f6-9d0e-5c4e11691dd2 | -9.45307 | -56.65469 | 2025-10-17 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f02660b9-fb70-34e2-a318-1a85aeb2e6b7 | -10.25961 | -44.04387 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2032509-2692-3ab9-9a9a-8edcfaa332ac | -13.43774 | -47.9682 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6bf1cb2-a503-3211-bdd5-56d3228bc719 | -7.17447 | -46.93227 | 2025-10-17 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7902ccbb-96f8-3314-919d-1927fddfdb1b | -8.40753 | -46.28989 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7eefa9e2-39ea-3ea5-a711-0b88d9ba6acd | -9.14722 | -46.64537 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5ae30581-43e9-34eb-814a-bfe5ec890595 | -11.17605 | -49.80171 | 2025-10-17 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4746969-e721-35d4-b6e1-e7b67bdffcc8 | -10.28859 | -44.04559 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 651ffbaa-0f9b-3f4d-9ffb-9965d7c4cdb4 | -10.149 | -44.53516 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| febfea6c-fd73-32b5-a0ec-4e4cd4ee50be | -9.13014 | -46.6343 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 326a2604-be41-3abd-a1b5-8ad2030ad5c0 | -7.1739 | -46.93637 | 2025-10-17 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 727ba149-c6ff-309d-8283-f25b86347dda | -12.42467 | -51.29898 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 867701be-9d0d-3607-aa08-a15e4fd87b14 | -10.6556 | -45.28858 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a56afa6b-e05e-3d60-80ac-dd27e4c15cde | -10.13647 | -44.59113 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f191e3a-7009-3311-a7a2-3e64293a0184 | -8.19742 | -46.93513 | 2025-10-17 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24f5d3fe-7224-3260-9dc5-4ae404bff1eb | -12.14943 | -49.68001 | 2025-10-17 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 459cdb0c-7369-3360-a5b3-dbaedab94158 | -9.24481 | -44.36689 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e106845e-fa9e-35a8-a046-2fd2cb673aba | -7.95006 | -44.12143 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a9da00f2-6db1-3963-b2ac-b8826eaa44f6 | -7.61576 | -47.83873 | 2025-10-17 05:10:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 500ddb39-134b-3156-aa04-e5279e64b991 | -8.08851 | -45.44131 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98105625-c7ad-34e7-baec-3bc4ff314e47 | -8.48913 | -49.0468 | 2025-10-17 05:10:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c26bb7c-7dbd-3dc4-9756-ea5be2367454 | -8.33245 | -46.24069 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef669b44-f945-350c-9da2-42274daa0605 | -10.1552 | -44.54273 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8432f137-280b-3518-821c-048beae0f374 | -8.55897 | -44.58342 | 2025-10-17 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61a16935-ab0c-3ba3-80c1-0fc7454e3121 | -13.43515 | -47.95197 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8ea7e8f-59e8-3172-8d88-de8c6660f2bb | -7.62175 | -47.83588 | 2025-10-17 05:10:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50a58093-a6c1-330f-a813-92aba5712400 | -13.43731 | -47.97199 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09432aa3-9a9c-3eb7-80f8-6c2a4216c286 | -7.94575 | -44.14952 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dd43ee9-33a2-3ce8-b92a-62b92a21688f | -9.36661 | -63.22821 | 2025-10-17 05:10:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ad88784-9b89-3f04-93b3-0fd38f204d0c | -9.29121 | -46.90864 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d80c6f36-ce07-38be-ad1f-afa4b1e0141a | -8.40235 | -46.23384 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05977658-5a6c-3aa0-80c9-2e0ec41e153d | -7.22037 | -58.60251 | 2025-10-17 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c04bead-3c76-30ad-baa5-c5280c32748d | -8.39489 | -46.2429 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd1306d6-184f-38ab-9410-de939db7a09f | -10.11923 | -44.55854 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c47cc6c-7c1e-30d3-be90-4e483a969510 | -8.46095 | -44.17574 | 2025-10-17 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0dc9123f-e7cf-3d92-929b-fb330ead3655 | -7.00103 | -46.99064 | 2025-10-17 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2430e1bd-e93f-3cdc-b185-6a34b6dddfff | -11.97439 | -46.5645 | 2025-10-17 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b029c4c0-4dab-31d7-95c4-9d13fba863d3 | -9.01491 | -46.61757 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ee901ca-b174-3ff8-9d26-97dcbce6cf61 | -6.53662 | -55.05025 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a803b0d-dbad-3e10-8fcc-41fbaa8d8030 | -9.5731 | -49.11311 | 2025-10-17 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e297bda2-267d-33d5-be1d-8cc41e711237 | -8.49521 | -48.49335 | 2025-10-17 05:10:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa0f8e74-0ba3-3bc0-ae55-c83ea1566aa4 | -11.57397 | -48.56133 | 2025-10-17 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e32dc1c-c58c-306c-926d-c7e0aa6a799a | -9.71256 | -44.5593 | 2025-10-17 05:10:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e89bae5-5fd2-302f-89b3-896f51a7610d | -11.37909 | -61.21307 | 2025-10-17 05:10:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05042682-d6f2-3d16-b3e8-715bca27b156 | -9.30332 | -46.93343 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b169704f-2bcb-3049-8074-70ba226a158a | -10.98035 | -47.91043 | 2025-10-17 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39369c9b-73fb-3b94-8906-c5b74332cb1f | -9.88404 | -55.91161 | 2025-10-17 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcbf1b94-5faa-3cb7-af00-4a6d543b08bf | -8.08268 | -45.4357 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd95d662-f636-3514-8296-94282ce2ab0f | -13.42442 | -48.59016 | 2025-10-17 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b39f2dfb-0799-37a6-b4a1-a55f868cff84 | -7.17476 | -46.9318 | 2025-10-17 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0816cedc-d527-33dd-bd6a-a8ec95eef25a | -9.29996 | -46.93628 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c30172e7-5d78-396d-b1cf-51dec46e5926 | -9.71147 | -44.56233 | 2025-10-17 05:10:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e45d251e-1563-3295-87cb-e212b565b513 | -10.10305 | -44.57537 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fda0db4d-2869-3261-8de3-0acae9b7cb9e | -8.72886 | -43.87172 | 2025-10-17 05:10:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a81bb8d0-2df4-3536-887c-c26f0859b103 | -8.41478 | -46.27809 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57760f6e-0c41-316f-bc9c-6ec82648a164 | -11.57351 | -48.56502 | 2025-10-17 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b03aad36-5be9-3e2a-9d10-45492c242d35 | -13.43321 | -47.95534 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9ddfce2-68ae-3f0f-bdb8-b79fe19ccdca | -8.56505 | -44.59048 | 2025-10-17 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c7b1e9b-e72a-3911-800e-827eb727b5a7 | -7.48671 | -47.03054 | 2025-10-17 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e322b56-1fb9-3eaa-a766-9e3bfbaa084a | -10.64884 | -45.25231 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d00b8c1-ba4d-3786-b329-d5d1af1469e3 | -8.72467 | -43.87886 | 2025-10-17 05:10:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fef6a720-af8f-35c1-9e66-b213cb07f37f | -9.61856 | -49.1292 | 2025-10-17 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82a7cc9d-b822-32a5-b8e2-e5a7fa8e8290 | -10.28548 | -44.04758 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5068d3f7-c188-3bd0-b1db-c8e27e991dc4 | -8.55788 | -44.58126 | 2025-10-17 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d757298-9000-3d07-ae77-351ac3af788e | -8.41496 | -46.28102 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e72038f1-4cbf-36ca-8730-06566286517c | -11.75398 | -61.07424 | 2025-10-17 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84babf98-ac67-3542-964c-d729a5ec8ffd | -11.57442 | -48.55762 | 2025-10-17 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README111.md)
