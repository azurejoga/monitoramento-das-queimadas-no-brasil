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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fce45a69-5f86-3b41-9dd3-130b30096ecd | -9.66758 | -46.53356 | 2026-09-02 11:51:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 3da64ae6-0aa0-32dd-b681-9ad0a6256729 | -11.05434 | -51.53254 | 2026-09-02 11:51:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 79cc1b6f-1eb7-3793-943c-6c28d8fb4392 | -9.21954 | -47.97723 | 2026-09-02 11:51:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6647bcca-2567-33eb-949f-1040da1359f4 | -8.11852 | -54.94936 | 2026-09-02 11:51:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 3a70a48f-7f42-3070-9dd6-f1b711658111 | -10.57133 | -47.73179 | 2026-09-02 11:51:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8fa947d0-61c0-39fe-8e5e-a7f9a6068051 | -13.39494 | -43.01126 | 2026-09-02 11:51:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 29bd4253-fece-3ab0-90b4-305d33e7dbd8 | -11.37757 | -45.41264 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| eb75cebf-c2c6-3e28-831a-14ffbd226514 | -12.3836 | -48.14496 | 2026-09-02 11:51:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4266bb02-4d53-385b-aa46-38a13a6eade5 | -11.34616 | -50.6334 | 2026-09-02 11:51:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fcb0e7aa-d7d5-3804-9e71-902e47838c3a | -10.77808 | -44.73559 | 2026-09-02 11:51:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 7f55949a-e1c7-3090-b508-0f488dfb16a0 | -10.78551 | -44.76482 | 2026-09-02 11:51:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5acfc3db-7b62-3ef5-b333-ea005a094c0c | -12.06102 | -44.99857 | 2026-09-02 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 830948aa-30a4-36e7-9282-69a7cb2934c3 | -11.5412 | -45.48465 | 2026-09-02 11:51:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f65bd911-056a-324e-ad3d-34e8cdb223a6 | -10.38882 | -49.9894 | 2026-09-02 11:51:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 15290640-9cc2-38a9-bf49-18f7f5ec6eb3 | -10.96345 | -50.47523 | 2026-09-02 11:51:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2e8abc52-00b4-3b87-9d4b-af853d304e44 | -11.27325 | -45.13408 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 019ef345-56a4-3084-93aa-1f35dd61edb1 | -11.36875 | -45.39861 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c6b57ac2-a9bf-36f0-b443-0a429a23c04a | -10.44078 | -46.7245 | 2026-09-02 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4f016d14-15d1-358f-909d-665818d18b4a | -10.77637 | -44.74935 | 2026-09-02 11:51:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 543f37c1-1b98-3079-8718-1167cdb2cfc3 | -11.67845 | -50.50737 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4192daff-1515-3a9e-9f96-487e7890798a | -8.47076 | -54.7198 | 2026-09-02 11:51:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 70de84ee-73a5-33b0-8643-c9d127fe8033 | -10.43939 | -46.73488 | 2026-09-02 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c656c3e1-06dc-3c9e-9f54-4dbbd95c9501 | -11.30931 | -45.14549 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ada1cfb8-6da5-31f4-b5a6-d1990b063fd3 | -11.69252 | -46.73837 | 2026-09-02 11:51:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 84374cac-c240-3337-a481-dfb1a7e2ea11 | -11.66324 | -50.48618 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 4e1c13bc-7b55-3a30-a0c7-c82ec11e1aed | -13.39725 | -42.99099 | 2026-09-02 11:51:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| e7d2adc6-77e6-3b85-b201-8a2555dca7c0 | -10.42583 | -49.98547 | 2026-09-02 11:51:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| e89dade1-e390-38f0-bb7d-42f8bdb31b34 | -12.14263 | -47.13482 | 2026-09-02 11:51:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 340b145b-83a1-359b-9e08-9eafd90848b0 | -10.57004 | -47.74118 | 2026-09-02 11:51:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cc0f87d7-0bfc-319b-85d2-a8fe84350fa2 | -12.96481 | -43.23779 | 2026-09-02 11:51:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 946673e9-12c7-306e-a703-c9f19ba14c05 | -11.6829 | -46.73725 | 2026-09-02 11:51:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 219c9bab-7d9e-3f57-9c06-e1e952aad6dc | -8.46132 | -54.69943 | 2026-09-02 11:51:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 213.9 |
| 4d411fe9-d489-3a96-8638-ca544f3ebd81 | -11.35672 | -45.40961 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9e6a16f5-0fd2-3d94-8772-9638a6e67a77 | -8.77991 | -46.4362 | 2026-09-02 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 55ae0bee-d7a7-3765-b696-6703f21fe941 | -11.30767 | -45.15839 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| fccec488-631e-338e-970e-c11dc3ead1e2 | -11.36713 | -45.41121 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 3f5905e7-4105-3db6-8705-b83d85556188 | -8.11871 | -54.95545 | 2026-09-02 11:51:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8cf45b3c-4521-3c5d-82f7-02c57021094e | -10.44216 | -46.71407 | 2026-09-02 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 692fb6b5-6b5e-36f5-8c80-7130621aa2f2 | -11.33633 | -50.57449 | 2026-09-02 11:51:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1eaff610-c336-384c-85d8-6f5a6167d4ea | -11.09991 | -51.54989 | 2026-09-02 11:51:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fa010420-7062-358e-840c-77263d73d4d8 | -13.96984 | -58.67756 | 2026-09-02 11:51:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| f7160dca-c685-3d14-be29-2c5e22c8dcaf | -11.3557 | -50.63129 | 2026-09-02 11:51:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ee491631-22b8-3940-a868-c325fb1f2ae7 | -10.60122 | -40.5231 | 2026-09-02 11:51:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 783b0a4e-b83f-3f13-a7f1-0e18e7e6488a | -11.12939 | -51.51904 | 2026-09-02 11:51:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ed3fa2d1-3c55-362e-a995-76b2a5c6d967 | -10.31813 | -50.02894 | 2026-09-02 11:51:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 20cbef5c-093e-31f0-8369-0390ef76eb7b | -14.56613 | -43.81964 | 2026-09-02 11:51:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6f5b7e60-ebcb-3c75-a4e6-3c1351c4305d | -12.8733 | -45.828 | 2026-09-02 11:51:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| d5725d7c-9cb0-314f-8766-abc53d3c4dab | -11.5461 | -45.4463 | 2026-09-02 11:51:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 5a019211-9c45-3ff4-9688-ffc0b2969f2b | -11.65289 | -50.49412 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| f04e4441-9113-38c3-8b22-05e7f51138fa | -15.02156 | -46.8912 | 2026-09-02 11:51:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f41547ac-9cdc-301f-840b-91482ea05b00 | -11.12783 | -51.52924 | 2026-09-02 11:51:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a97a6df5-8990-3a63-b157-7c1ee9c0b26d | -11.66187 | -50.49545 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| cb2504a9-3c53-3cef-8221-2a858c23bf84 | -8.77851 | -46.4464 | 2026-09-02 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e9d82514-4a0f-368d-a2ba-707f52e6a281 | -8.47369 | -54.7012 | 2026-09-02 11:51:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| e3227ffb-0f27-3ccd-8212-325ca84e5234 | -11.85306 | -46.07231 | 2026-09-02 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 2b63543a-9191-3ffb-8eca-b57cf1988a3a | -8.43147 | -54.70679 | 2026-09-02 11:51:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| ff07f44a-ac2f-33b6-a1c8-b68b71818709 | -14.564 | -43.83853 | 2026-09-02 11:51:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 3942bc01-01c8-3de7-90fa-7ce3ec93b4c2 | -9.00969 | -50.77849 | 2026-09-02 11:51:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d6ccb112-f2f3-3de3-95d7-a89fdda0acad | -12.87491 | -45.81529 | 2026-09-02 11:51:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f3f2617a-3840-39f1-b9c7-0b2273a6fd70 | -11.6693 | -50.18948 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ac284ee7-522d-3afe-a6d3-5cafa2f0b6ee | -10.05373 | -46.68351 | 2026-09-02 11:51:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 859d35c5-a8ca-31e3-985b-724e52ff0eb4 | -11.5477 | -45.43379 | 2026-09-02 11:51:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| c9971d87-6db4-3c64-8c4e-b3c3cec2959e | -11.67358 | -50.47824 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6d8ffea4-c3b1-398b-a257-4a5c574a4c13 | -12.11977 | -47.0514 | 2026-09-02 11:51:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c1823ee2-4d63-3237-9eb2-c28aa70f85c7 | -9.66897 | -46.52325 | 2026-09-02 11:51:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| eb591ab3-5fcc-33b3-a5a5-5ef886244d62 | -11.86001 | -46.09708 | 2026-09-02 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 318.0 |
| dfa6cf2e-5534-3868-a08f-31958e2caded | -11.85152 | -46.08405 | 2026-09-02 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 956.4 |
| 49acc46a-38d3-3d07-9d69-6226bc9d687e | -10.3092 | -50.02764 | 2026-09-02 11:51:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 9cc90ca2-2bad-3498-b886-80362d46b423 | -12.37455 | -48.14368 | 2026-09-02 11:51:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 6160666b-def6-353a-8571-7c20fddaa22b | -11.54283 | -45.47188 | 2026-09-02 11:51:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 62201b02-540c-3807-abf4-422cc2df3608 | -11.12331 | -51.52198 | 2026-09-02 11:51:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 99c4ef81-cdbf-3c6f-a733-d3135e01a00f | -11.84998 | -46.09583 | 2026-09-02 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 707.0 |
| 57f98c46-de73-324e-bfae-6c5e8df56a87 | -14.56173 | -43.83167 | 2026-09-02 11:51:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 6aca2389-b140-3b25-80b4-969b967837de | -12.05916 | -45.01349 | 2026-09-02 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f5e82eec-9ecc-3d79-9d20-1cf88d865c82 | -11.46362 | -44.55688 | 2026-09-02 11:51:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2e2c4aed-766b-3348-bfb2-a363bce2dffd | -10.95444 | -50.4739 | 2026-09-02 11:51:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| ed394aee-8ec1-32f0-bbcf-d76781bc93b1 | -21.257 | -44.95267 | 2026-09-02 11:53:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 4276c7d4-e991-3836-836c-5eb970535361 | -21.25486 | -44.97265 | 2026-09-02 11:53:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 276b97a6-9fb2-384c-b71b-99f336a75690 | -22.77412 | -47.01203 | 2026-09-02 11:53:00 | TERRA_M-M | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 087f9675-b19b-3ac8-b6ee-d62bf4d29305 | -16.86737 | -43.24358 | 2026-09-02 11:53:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3ae73d89-595f-37f1-a917-c063de3c3fd4 | -21.34229 | -51.64849 | 2026-09-02 11:53:00 | TERRA_M-M | NOVA GUATAPORANGA | SÃO PAULO | Brasil | 3533106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| eab54b83-b55a-3b2d-a478-76894b24753d | -8.4671 | -54.7035 | 2026-09-02 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 517.7 |
| 5ec22331-e0ba-3d64-98ef-65ce44b5b918 | -8.7819 | -46.4399 | 2026-09-02 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 66959544-95ff-37f7-b78d-8f147cc32b7c | -11.5483 | -45.4446 | 2026-09-02 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 9c87f5b5-ccf1-323d-9db2-6c3765903b22 | -11.3579 | -45.4027 | 2026-09-02 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 0e6afb47-2fc7-3263-95a5-3ef5527b2daf | -8.4669 | -54.7237 | 2026-09-02 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| c6575f50-a5c9-3719-af35-e2b21eb022cd | -9.423 | -37.8286 | 2026-09-02 12:00:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 52665800-31ee-36e2-903c-9b26e067ad31 | -8.4858 | -54.7023 | 2026-09-02 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 264.1 |
| d9dc2ee3-38cd-3742-b74b-4a1064bf89c7 | -10.3196 | -50.0211 | 2026-09-02 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ad8955b9-4be9-3e47-9de1-a269ecff8bc3 | -11.3048 | -45.1575 | 2026-09-02 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4cd0626a-440f-3338-95a1-dde0f1670e1e | -8.4485 | -54.7048 | 2026-09-02 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |
| d6a948d2-ffe9-337c-8d2b-b04ece3247f0 | -8.4673 | -54.6833 | 2026-09-02 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 458.4 |
| ad21e1c4-56ed-38eb-a440-576feefb0e6f | -11.3579 | -45.4027 | 2026-09-02 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 71ac5fd2-31f5-361f-beae-caade6bd7ca1 | -8.4669 | -54.7237 | 2026-09-02 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| d435c069-1787-30b7-a1d5-63316a3da79f | -8.4671 | -54.7035 | 2026-09-02 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 290.9 |
| 99a5764d-bbae-3156-ba77-2e37c19b47dc | -9.423 | -37.8286 | 2026-09-02 12:10:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 85b829cb-607b-3993-8c16-402ec1be528e | -9.4349 | -45.625 | 2026-09-02 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ac7259e6-36bb-398b-8353-da2b58a70302 | -11.3044 | -45.1805 | 2026-09-02 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 08572eda-b9dd-328f-aefd-e703f6ddcea7 | -8.4485 | -54.7048 | 2026-09-02 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 75cd6841-9284-34ec-8901-d11a56b2f607 | -10.9562 | -50.4884 | 2026-09-02 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |


[Clique aqui para ver as próximas entradas](README70.md)
