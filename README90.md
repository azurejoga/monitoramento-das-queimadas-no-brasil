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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9e41ca9-ab8a-397c-a535-cddc737600fa | -3.5015 | -53.4432 | 2026-09-20 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07efa7aa-88b4-3820-b86e-4e5ff5062520 | -11.09256 | -48.29504 | 2026-09-20 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ebafce08-2ec8-34d6-abc4-9ab0a9e66b1d | -2.88677 | -57.82076 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be3517ed-f0f9-3c01-ab1d-7adb96fe5b22 | -8.80142 | -60.79342 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4907d94-ee8a-3af2-9fe3-07c7bc0fd8f1 | -9.18666 | -60.7646 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c6feb04-b6c3-3b0d-9fb9-4c9cdbaf6120 | -9.34813 | -61.17257 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfb41bac-d302-3db5-b0ba-169c7225b0c0 | -10.32022 | -50.21171 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d85e4945-81ea-3180-9c84-cf11d95b872d | -10.30912 | -50.25374 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14745c14-e069-3526-bc1a-403f86e3d2c9 | -7.55818 | -61.32785 | 2026-09-20 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7652eaeb-e46f-31c0-b44a-552e506e0248 | -3.51965 | -56.91152 | 2026-09-20 05:23:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d8f400e-1a01-3a4b-afa9-6b2794173d4b | -3.01879 | -51.19572 | 2026-09-20 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7bc1733-5389-3e91-9d4f-cb571ef19e25 | -8.11986 | -54.82007 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 536f7f33-a124-3122-bc50-152f33a6bfcc | -2.5888 | -59.99625 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be0b1034-3c33-30d1-a329-b8d5e813ee2e | -8.62063 | -55.22963 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89f81208-d345-3ac6-840c-200298cd6b4f | -8.64341 | -62.49207 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 909f6e73-3c93-3d2a-aa3e-c10ef373d18a | -8.23699 | -61.36146 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d47bbac9-3ce7-31b9-922f-c0bca41d4d54 | -9.57632 | -55.10595 | 2026-09-20 05:23:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 487d18f4-9c80-31aa-b925-4799582b5440 | 2.3175 | -60.92026 | 2026-09-20 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6b668f0f-2090-3155-b7fe-8875a6d56ab3 | -3.12012 | -61.25335 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aa556a6-639a-3b1e-af89-32772a878d47 | -10.7815 | -50.87359 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a4e44107-092f-3429-bb8d-314b09290398 | -6.36772 | -58.30894 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fd1b6b0-0281-3e65-a89d-3f6f10208ac5 | -2.8828 | -57.80094 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cb9a23fb-ea64-3454-b8cf-0983e3dee22a | -3.35045 | -59.86942 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4609812b-166e-3830-8416-55a209043d23 | -3.1913 | -60.42881 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b613e180-fb70-38dd-bb53-1f55397b78c5 | -3.04303 | -61.26323 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79d9a501-04a2-3266-bcb1-94753d4b7e91 | -10.28948 | -50.2076 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b823d74f-5b8e-32c6-a781-1473c770eb69 | -2.31193 | -58.13778 | 2026-09-20 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 44f7cae5-f4c4-3e90-907d-2143d3f067af | -9.04773 | -48.72423 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b62ab6ee-0c9b-307e-adee-e7539a2d5eb5 | -9.19446 | -60.75866 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 035bff12-b724-3438-be39-4c5dce8ade6b | -9.39655 | -60.34966 | 2026-09-20 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b5d57ea-b38e-3b05-9926-500c132424ce | -3.17124 | -48.61618 | 2026-09-20 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4cf3699-699b-3b34-90a6-b2a7430be8b3 | 0.77934 | -59.49287 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6e42799-dd93-3a31-8a06-e4fb9d187dd9 | -7.87912 | -62.54698 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 674b2c11-5b1f-3a58-8e45-a79798c0967b | -6.44921 | -59.97477 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38813558-c76c-3e70-82c9-b6b106ce8954 | -3.01336 | -54.16727 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e2ba71f-f342-3a9b-8b0e-a6e285f68566 | -3.33971 | -58.15837 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccb61a8b-3216-3a64-8459-a68055974a23 | -3.04306 | -46.92955 | 2026-09-20 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5eaa9948-593b-381a-b7f1-9cbf7f58281b | -7.55709 | -61.33478 | 2026-09-20 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcca6aa2-1f70-3cd9-a69b-c11442254ce9 | -2.88391 | -57.81649 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 180879c3-a200-3647-a072-6be5f757585b | -2.87171 | -56.51767 | 2026-09-20 05:23:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 285fa3cd-2806-3bb2-9166-4a277517ca08 | -9.58014 | -55.1109 | 2026-09-20 05:23:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11f228df-5974-323e-b3e1-1241a8ff9b78 | -2.88105 | -57.81221 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4e62807a-0e9b-32ad-a7ff-d54fb9f2842c | -3.89576 | -49.0635 | 2026-09-20 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7441dffc-2faa-39d5-a873-8bde16c94549 | -10.30968 | -50.24899 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ec486920-b65c-3c22-a1a2-a3e5c6dd85a4 | -9.81118 | -48.32572 | 2026-09-20 05:23:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5377ec8f-c1c7-3df1-8dfd-4935fea864c9 | -10.78205 | -50.86922 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8bac062d-3f60-309e-8744-3c748ea23084 | -10.31301 | -50.22038 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ee317737-3dd5-3e93-9b81-760a994759dd | -9.18557 | -60.77159 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c96809ba-64c4-3326-9bcf-3c44d2a825ec | -8.23645 | -61.36493 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 029d0fba-81fd-3ef8-997b-60f5e64182d4 | 0.30556 | -60.44573 | 2026-09-20 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d75f319a-caf9-366d-b5dd-ce9b4ca0db42 | -7.5864 | -55.70654 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7463aec-6ef3-3e89-9f55-f2bcd7aa175f | -3.74039 | -51.81464 | 2026-09-20 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f841e90-82e1-3df4-83db-021013a840e5 | -3.19791 | -60.42983 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39f17122-c5c0-3321-89e0-49d1d0a1ce61 | -1.51632 | -49.47428 | 2026-09-20 05:23:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1deaff5-1f1a-34c0-88d0-41d464765b04 | -2.56534 | -57.87969 | 2026-09-20 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8d6fe55-17c1-36d7-b981-f63face322d5 | -3.11176 | -61.40868 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d372a450-07b5-38ff-8602-51fceeab7214 | -9.27853 | -60.63178 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 423d5b54-e0b3-3852-a9e1-93ad5f18d683 | -7.57281 | -57.68749 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffb2979f-c451-3d8a-8135-c7226fa8983c | -1.21846 | -55.72466 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02100738-f993-3b03-a033-529ffe9c804a | -8.17063 | -54.74414 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31d4e82a-6985-3354-9ac9-49b96b6a2d35 | -9.06496 | -61.37291 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42ffaaea-da49-33a4-ab87-e075df2c86f6 | -3.31731 | -59.38113 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52390e14-e85b-39ee-9e17-d91efb55dba3 | -2.12712 | -59.5969 | 2026-09-20 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6df0e087-1e49-3078-b084-83dcef41f955 | -10.31904 | -50.22126 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 79d5b971-17f7-368f-9847-0783210b8463 | -10.78041 | -50.88232 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 53d09470-fc19-3ab0-be1e-b6b3df6ecd42 | -8.17944 | -54.7454 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8659cc78-cca0-3b88-bd16-89523e3babb7 | -2.82821 | -50.4784 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b977c72-d406-39da-9b0a-dcdd44d0de18 | -9.81227 | -48.3168 | 2026-09-20 05:23:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1062cb0e-0c88-36ac-a118-85c33866f528 | -9.93723 | -53.98674 | 2026-09-20 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c516780e-daf6-3de9-8d78-6538b3ebd904 | -3.00913 | -54.16655 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aaa1623b-fe34-315f-9d72-cd295b29b95b | -6.45444 | -58.14567 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e5247b3-0807-39e6-ad87-23dc413f2d67 | -9.27479 | -48.23898 | 2026-09-20 05:23:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c61124b6-6e70-396a-83f7-7e745b28db0e | -3.3999 | -54.06918 | 2026-09-20 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 733fe7b9-0f3d-3cf5-8fd9-c1bb153e35b1 | 1.22209 | -50.98321 | 2026-09-20 05:23:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60083083-1e02-3aa3-b0b9-2fdfa19cdfd1 | -9.04345 | -60.45789 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b423435-7a33-357b-b421-7c1ed6a9fe2e | 4.52324 | -60.91117 | 2026-09-20 05:23:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4894f5a-caa5-3cfc-a8f9-00e5c5981766 | -2.4259 | -60.12147 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b66db93-2842-342d-9baa-35e921e80440 | -4.07606 | -52.11615 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6439a4ef-0a0d-397f-baa9-393be77d83a5 | -8.17003 | -54.74846 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96153f0e-b4c4-39e3-af7b-85e943f77c88 | -9.70874 | -54.82882 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af3ece68-9dda-363b-bfe3-28f985c044b1 | -6.72836 | -55.08192 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 911fc7cc-8149-31df-8824-34e8f0251d4f | -3.04582 | -61.2673 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 879818ea-77e8-33aa-a5ee-58fe2e8f5e8b | -2.86094 | -58.28439 | 2026-09-20 05:23:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30b0b6b8-bc0f-38ae-8219-36b91c1978c8 | -9.67144 | -54.31847 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91d82a02-9ac9-3b23-b55e-878b08944e5a | -6.34335 | -58.30522 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 844c3fdd-26c9-35d3-b735-cfb397f9cd71 | -2.172 | -48.32536 | 2026-09-20 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97597593-4953-3217-8332-9c23b5fed515 | -6.49084 | -58.37802 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a25ed38-70d3-371e-b6b4-649016bd77df | -6.49779 | -58.37905 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d34d84d7-9648-3aaf-93f3-9d428cc9765b | -3.04154 | -51.37394 | 2026-09-20 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e9b3295-ff85-3d35-aca5-5da1492d3299 | -3.37512 | -50.43975 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d8678947-af90-3f7f-a3c2-e1535a2ccd52 | -3.34354 | -59.84381 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 429d038b-5383-3345-a40d-2f4ad9aa18d7 | -6.81523 | -59.1905 | 2026-09-20 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 030ed912-d312-3658-b50f-1e47e1c0ec7f | -7.75723 | -49.20264 | 2026-09-20 05:23:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f12311b8-92d5-393e-83e2-ac2d4c48bd61 | -6.36365 | -58.31227 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7e954c4-612b-312b-a71f-3327fdb811d4 | -8.14848 | -54.80695 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cfef2236-9ab4-347f-81f7-86c1d5ebe8b2 | -3.59559 | -47.35589 | 2026-09-20 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f223658-04b3-3881-88b1-8b2ad37fe833 | -2.45955 | -49.21449 | 2026-09-20 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 906592d5-540f-3a57-afa0-56d238f014ff | -3.11063 | -61.41581 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f352a2f-d48d-37e0-b353-cb554130208a | -8.20565 | -62.85323 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d37bd433-5bb4-3bba-a71d-7b2c91c98f59 | -3.13268 | -61.2551 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README91.md)
